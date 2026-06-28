#!/usr/bin/env python3
"""
risk_classifier.py - UPGRADED v2.2
EU AI Act Compliance Toolkit -- GRC Engineering Automation

Upgrades in v2.2:
- GPAI is treated as an ORTHOGONAL regime, not a "Limited Risk" sub-tier.
  A GPAI model embedded in a high-risk system now correctly retains BOTH the
  high-risk system obligations AND the GPAI model obligations (Arts. 53-55).
- Added 'gpai_systemic' CSV flag (>10^25 FLOP or designated) -> Art. 55 obligations.
- Corrected Article reference comments.

Upgrades in v2.1:
- --format txt|json|csv: machine-readable output for GRC platforms / CI pipelines
- --version flag
- Input validation: warns on invalid annex_iii_area and non yes/no field values

Upgrades in v2.0:
- Article 6(3) exclusion logic: structured CSV fields prevent incorrect high-risk classification
- Dedicated 'prohibited_practice' CSV field: reduces reliance on brittle keyword matching
- Warning system: flags keyword-matched prohibited practices for human review
- GPAI model flag triggers reference to document 11
- Disclaimer: output is a triage aid, not a legal determination
"""

import csv
import json
import argparse
import sys
import os
from datetime import datetime

__version__ = "2.2.0"

ARTICLE_5_KEYWORDS = [
    "subliminal manipulation", "subliminal technique",
    "social scoring", "social credit",
    "real-time biometric identification public", "real-time remote biometric",
    "emotion recognition workplace", "emotion recognition education",
    "untargeted facial scraping", "facial database scraping",
    "predict criminal", "predictive policing profiling",
    "exploitation of vulnerabilities",
    "biometric categorisation",
]

ANNEX_III_AREAS = {
    "1": "Biometrics",
    "2": "Critical Infrastructure",
    "3": "Education and Vocational Training",
    "4": "Employment and Workers Management",
    "5": "Essential Private and Public Services",
    "6": "Law Enforcement",
    "7": "Migration, Asylum, and Border Control",
    "8": "Administration of Justice",
}

OBLIGATIONS = {
    "UNACCEPTABLE": [
        "IMMEDIATE ACTION: do NOT place/keep on EU market",
        "Withdraw system if already deployed",
        "Notify authorities if harm has occurred",
    ],
    "HIGH": [
        "Risk management system (Article 9)",
        "Data governance (Article 10)",
        "Technical documentation Annex IV (Article 11)",
        "Automatic logging (Article 12)",
        "Transparency and instructions for use (Article 13)",
        "Human oversight (Article 14)",
        "Accuracy, robustness, cybersecurity (Article 15)",
        "Quality management system (Article 17)",
        "Conformity assessment: Annex VI (internal) or Annex VII (Notified Body) (Articles 43-48)",
        "EU database registration (Article 49)",
        "EU Declaration of Conformity (Article 47) -- see 12-EU-DECLARATION-OF-CONFORMITY.md",
        "Post-market monitoring (Article 72)",
        "Serious incident reporting: immediately, max 15/2/10 days (Article 73)",
        "FRIA if deployer in public/public-service or credit/insurance context (Article 27)",
        "Inform workers before deployment in workplace (Article 26(7))",
    ],
    "LIMITED": [
        "Disclose AI to users (Article 50(1)) -- if chatbot/conversational",
        "Mark AI-generated/manipulated outputs machine-readably (Article 50(2))",
        "Inform persons of emotion recognition / biometric categorisation (Article 50(3))",
        "Disclose deepfakes / AI-generated public-interest text (Article 50(4))",
    ],
    "MINIMAL": [
        "No mandatory obligations under EU AI Act",
        "Consider voluntary codes of conduct (Article 95)",
        "Maintain good AI governance practices",
    ],
    # GPAI is a separate, parallel regime (Arts. 51-56), appended regardless of the
    # system risk tier above. It is NOT a sub-tier of LIMITED.
    "GPAI": [
        "GPAI: Technical documentation Annex XI (Article 53(1)(a)-(b)) -- see 11-GPAI-TECHNICAL-DOCUMENTATION.md",
        "GPAI: Information/documentation to downstream providers (Article 53(1)(b))",
        "GPAI: Copyright compliance policy (Article 53(1)(c))",
        "GPAI: Publish training-content summary (Article 53(1)(d))",
    ],
    "GPAI_SYSTEMIC": [
        "GPAI SYSTEMIC: Model evaluation / adversarial testing (Article 55(1)(a))",
        "GPAI SYSTEMIC: Assess and mitigate systemic risks (Article 55(1)(b))",
        "GPAI SYSTEMIC: Report serious incidents to AI Office without undue delay (Article 55(1)(c))",
        "GPAI SYSTEMIC: Adequate cybersecurity protection (Article 55(1)(d))",
        "GPAI SYSTEMIC: Cooperate with AI Office/Commission (Articles 88, 91-93) -- see 27-GPAI-SYSTEMIC-RISK-COMPLIANCE.md",
    ],
}


def check_article_6_3_exclusion(row):
    """
    Check Article 6(3) exclusions. A system listed in Annex III is NOT
    high-risk if it meets any of the four exclusions AND does not perform
    profiling of natural persons. Returns (excluded, reason).
    Requires CSV columns: exclusion_narrow_task, exclusion_human_result,
    exclusion_no_individual, exclusion_preparatory (values: yes/no).
    The 'profiling' column, if "yes", overrides any exclusion (always high-risk).
    """
    # Art. 6(3) final subparagraph: profiling of natural persons => always high-risk.
    if row.get("profiling", "").strip().lower() == "yes":
        return False, ""
    exclusions = {
        "exclusion_narrow_task": "Art. 6(3)(a): narrow procedural task only",
        "exclusion_human_result": "Art. 6(3)(b): improves result of prior human activity only",
        "exclusion_no_individual": "Art. 6(3)(c): detects patterns without influencing individuals",
        "exclusion_preparatory": "Art. 6(3)(d): preparatory task to human assessment only",
    }
    for field, reason in exclusions.items():
        if row.get(field, "").strip().lower() == "yes":
            return True, reason
    return False, ""


def gpai_obligations(row):
    """Return GPAI obligations (orthogonal to the system risk tier), or []."""
    obs = []
    if row.get("gpai_model", "").strip().lower() == "yes":
        obs.extend(OBLIGATIONS["GPAI"])
        if row.get("gpai_systemic", "").strip().lower() == "yes":
            obs.extend(OBLIGATIONS["GPAI_SYSTEMIC"])
    return obs


def classify_system(row):
    use_case = row.get("use_case_category", "").strip().lower()
    annex_iii_area = row.get("annex_iii_area", "").strip()
    annex_i_product = row.get("annex_i_product", "").strip().lower()
    transparency_obligation = row.get("transparency_obligation", "").strip().lower()
    gpai_model = row.get("gpai_model", "").strip().lower()
    prohibited_practice = row.get("prohibited_practice", "").strip().lower()

    warnings = []
    exclusion = ""
    gpai_obs = gpai_obligations(row)
    if gpai_obs:
        warnings.append(
            "GPAI model detected: GPAI obligations (Arts. 53-55) apply IN ADDITION "
            "to the system risk tier below. GPAI is a separate regime, not 'Limited Risk'."
        )

    # Step 1: Article 5 prohibited practices
    is_prohibited = prohibited_practice == "yes"
    prohibited_keyword = ""
    if not is_prohibited:
        for kw in ARTICLE_5_KEYWORDS:
            if kw in use_case:
                is_prohibited = True
                prohibited_keyword = kw
                warnings.append(
                    f"REVIEW REQUIRED: keyword '{kw}' matched -- "
                    f"confirm this is actually an Article 5 prohibited practice"
                )
                break

    if is_prohibited:
        return {
            "tier": "UNACCEPTABLE",
            "reason": (
                "Prohibited (explicit flag)"
                if prohibited_practice == "yes"
                else f"Prohibited (keyword: '{prohibited_keyword}') -- REVIEW"
            ),
            "obligations": OBLIGATIONS["UNACCEPTABLE"],
            "exclusion": "",
            "warnings": warnings,
        }

    # Step 2: Article 6(1) -- Annex I safety component
    if annex_i_product == "yes":
        return {
            "tier": "HIGH",
            "reason": "HIGH -- Annex I safety component (Article 6(1))",
            "obligations": OBLIGATIONS["HIGH"] + gpai_obs,
            "exclusion": "",
            "warnings": warnings,
        }

    # Step 3: Article 6(2) -- Annex III + Article 6(3) exclusion check
    if annex_iii_area and annex_iii_area in ANNEX_III_AREAS:
        area_name = ANNEX_III_AREAS[annex_iii_area]
        excluded, excl_reason = check_article_6_3_exclusion(row)
        if excluded:
            exclusion = excl_reason
            warnings.append(
                f"Article 6(3) exclusion claimed: '{excl_reason}'. "
                f"Register the exclusion in the EU database (Art. 49(2)) and "
                f"document justification in 05-AI-SYSTEM-REGISTER.md. "
                f"Misapplication creates regulatory risk."
            )
            # Fall through to LIMITED/MINIMAL (still apply any GPAI obligations)
        else:
            return {
                "tier": "HIGH",
                "reason": f"HIGH -- Annex III Area {annex_iii_area}: {area_name} (Art. 6(2))",
                "obligations": OBLIGATIONS["HIGH"] + gpai_obs,
                "exclusion": "",
                "warnings": warnings,
            }

    # Step 4: Article 50 transparency / GPAI -- Limited Risk (transparency overlay)
    if transparency_obligation == "yes" or gpai_model == "yes":
        parts = []
        if transparency_obligation == "yes":
            parts.append("transparency obligation (Article 50)")
        if gpai_model == "yes":
            parts.append("GPAI model (Arts. 53-55) -- see 11-GPAI-TECHNICAL-DOCUMENTATION.md")
        base = OBLIGATIONS["LIMITED"] if transparency_obligation == "yes" else []
        return {
            "tier": "LIMITED",
            "reason": "LIMITED -- " + "; ".join(parts),
            "obligations": base + gpai_obs,
            "exclusion": exclusion,
            "warnings": warnings,
        }

    # Step 5: Minimal Risk
    return {
        "tier": "MINIMAL",
        "reason": "MINIMAL -- no Article 5, 6, or 50 triggers",
        "obligations": OBLIGATIONS["MINIMAL"] + gpai_obs,
        "exclusion": exclusion,
        "warnings": warnings,
    }


REQUIRED_COLUMNS = {
    "system_id", "system_name", "owner", "use_case_category",
    "annex_iii_area", "annex_i_product", "transparency_obligation",
    "gpai_model", "provider_or_deployer",
}

ART_63_COLUMNS = {
    "exclusion_narrow_task", "exclusion_human_result",
    "exclusion_no_individual", "exclusion_preparatory", "prohibited_practice",
    "profiling", "gpai_systemic",
}

YES_NO_COLUMNS = [
    "annex_i_product", "transparency_obligation", "gpai_model", "gpai_systemic",
    "prohibited_practice", "profiling", "exclusion_narrow_task", "exclusion_human_result",
    "exclusion_no_individual", "exclusion_preparatory",
]

TIER_LABELS = {
    "UNACCEPTABLE": "[BANNED]",
    "HIGH": "[HIGH  ]",
    "LIMITED": "[LTD   ]",
    "MINIMAL": "[MIN   ]",
}


def validate_row(row):
    """Return a list of validation warnings for a single CSV row."""
    issues = []
    sid = row.get("system_id", "?").strip() or "?"
    area = row.get("annex_iii_area", "").strip()
    if area and area not in ANNEX_III_AREAS:
        issues.append(
            f"[{sid}] invalid annex_iii_area '{area}' (expected 1-8 or blank) -- treated as blank"
        )
    for field in YES_NO_COLUMNS:
        val = row.get(field, "").strip().lower()
        if val not in ("", "yes", "no"):
            issues.append(
                f"[{sid}] field '{field}'='{val}' is not yes/no -- treated as 'no'"
            )
    return issues


def generate_report(results, input_file):
    sep = "=" * 88
    thin = "-" * 88
    lines = [
        sep,
        "EU AI Act -- AI System Risk Classification Report (v2.2)",
        f"Run Date   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Input File : {input_file}",
        "Regulation : (EU) 2024/1689 -- EU Artificial Intelligence Act",
        "DISCLAIMER : Triage aid only. Human compliance review is mandatory.",
        sep, "",
        f"{'ID':<12} {'System Name':<35} {'Owner':<20} {'Tier':<10} Reason",
        thin,
    ]

    for r in results:
        label = TIER_LABELS.get(r["tier"], r["tier"])
        lines.append(
            f"{r['system_id']:<12} {r['system_name'][:34]:<35} {r['owner'][:19]:<20} "
            f"{label} {r['reason']}"
        )

    lines.extend(["", thin])

    exclusions = [r for r in results if r.get("exclusion")]
    if exclusions:
        lines.extend(["", "ARTICLE 6(3) EXCLUSIONS (require documented justification + Art. 49(2) registration):"])
        for r in exclusions:
            lines.append(f"  {r['system_id']} {r['system_name']}: {r['exclusion']}")

    all_warnings = [(r["system_id"], r["system_name"], w)
                    for r in results for w in r.get("warnings", [])]
    if all_warnings:
        lines.extend(["", "WARNINGS (require human review):"])
        for sid, sname, w in all_warnings:
            lines.append(f"  [{sid}] {sname}: {w}")

    tier_counts = {"UNACCEPTABLE": 0, "HIGH": 0, "LIMITED": 0, "MINIMAL": 0}
    for r in results:
        tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1

    lines.extend([
        "", thin, "SUMMARY",
        f"  Total    : {len(results)}",
        f"  [BANNED] : {tier_counts['UNACCEPTABLE']}",
        f"  [HIGH  ] : {tier_counts['HIGH']}",
        f"  [LTD   ] : {tier_counts['LIMITED']}",
        f"  [MIN   ] : {tier_counts['MINIMAL']}",
        thin, "",
    ])

    return "\n".join(lines)


def write_json(results, path):
    payload = {"generated": datetime.now().isoformat(), "systems": results}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def write_csv(results, path):
    cols = ["system_id", "system_name", "owner", "tier", "reason", "exclusion"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols + ["warnings"])
        for r in results:
            w.writerow([r.get(c, "") for c in cols] + [" | ".join(r.get("warnings", []))])


def main():
    parser = argparse.ArgumentParser(
        description="EU AI Act Risk Classifier v2.2 -- exits with code 1 on BANNED systems"
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument(
        "--input",
        default=os.path.join(os.path.dirname(__file__), "sample_ai_inventory.csv"),
    )
    parser.add_argument("--output", default=None)
    parser.add_argument(
        "--format", choices=["txt", "json", "csv"], default="txt",
        help="Output format (default: txt)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(2)

    ext = {"txt": ".txt", "json": ".json", "csv": ".csv"}[args.format]
    output_file = args.output or os.path.join(
        os.path.dirname(args.input), "risk_classification_report" + ext
    )

    results = []
    with open(args.input, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = list(reader.fieldnames or [])
        missing_req = REQUIRED_COLUMNS - set(headers)
        if missing_req:
            print(f"ERROR: Missing required columns: {missing_req}", file=sys.stderr)
            sys.exit(2)
        missing_63 = ART_63_COLUMNS - set(headers)
        if missing_63:
            print(
                f"WARNING: Missing Art. 6(3)/prohibited/GPAI columns: {sorted(missing_63)}. "
                f"Add to inventory for complete classification.",
                file=sys.stderr,
            )
        for row in reader:
            for issue in validate_row(row):
                print(f"WARNING: {issue}", file=sys.stderr)
            c = classify_system(row)
            results.append({
                "system_id": row.get("system_id", "").strip(),
                "system_name": row.get("system_name", "").strip(),
                "owner": row.get("owner", "").strip(),
                **c,
            })

    if not results:
        print("WARNING: No systems found.", file=sys.stderr)
        sys.exit(0)

    if args.format == "json":
        write_json(results, output_file)
    elif args.format == "csv":
        write_csv(results, output_file)
    else:
        report = generate_report(results, args.input)
        print(report)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report saved: {output_file}")

    banned = sum(1 for r in results if r["tier"] == "UNACCEPTABLE")
    if banned > 0:
        print(
            f"\nCI/CD GATE: {banned} BANNED system(s) detected -- exit code 1",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
