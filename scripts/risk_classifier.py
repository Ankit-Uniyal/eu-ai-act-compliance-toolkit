#!/usr/bin/env python3
"""
risk_classifier.py
------------------
EU AI Act Compliance Toolkit — GRC Engineering Automation

Purpose:
    Reads a CSV inventory of AI systems and classifies each one under the
    EU AI Act risk framework (Regulation (EU) 2024/1689):
        - UNACCEPTABLE RISK  (Article 5  — prohibited)
        - HIGH RISK          (Article 6  — Annex I or Annex III)
        - LIMITED RISK       (Article 50 — transparency obligations)
        - MINIMAL RISK       (no mandatory obligations)

    Outputs a formatted console report and saves a classification report file.
    CI/CD-friendly: exits with code 1 if any UNACCEPTABLE RISK systems are found.

Usage:
    python scripts/risk_classifier.py
    python scripts/risk_classifier.py --input scripts/sample_ai_inventory.csv
    python scripts/risk_classifier.py --input scripts/sample_ai_inventory.csv --output reports/risk_report.txt

Expected CSV columns:
    system_id, system_name, owner, use_case_category, annex_iii_area,
    transparency_obligation, gpai_model, provider_or_deployer

Author:  Ankit Uniyal
Toolkit: EU AI Act Compliance Toolkit
Version: 1.0.0
"""

import csv
import argparse
import sys
from datetime import date
from pathlib import Path


# ── Constants ─────────────────────────────────────────────────────────────────
DATE_FORMAT = "%Y-%m-%d"

RISK_UNACCEPTABLE = "UNACCEPTABLE RISK"
RISK_HIGH         = "HIGH RISK"
RISK_LIMITED      = "LIMITED RISK"
RISK_MINIMAL      = "MINIMAL RISK"

# Annex III high-risk use case areas (Article 6(2))
ANNEX_III_AREAS = {
    "1": "Biometrics",
    "2": "Critical Infrastructure",
    "3": "Education & Vocational Training",
    "4": "Employment & Workers Management",
    "5": "Essential Private/Public Services",
    "6": "Law Enforcement",
    "7": "Migration, Asylum & Border Control",
    "8": "Administration of Justice",
}

# Obligations by risk tier
OBLIGATIONS = {
    RISK_UNACCEPTABLE: [
        "System is PROHIBITED under Article 5",
        "Must NOT be placed on EU market or put into service",
        "Immediate cessation of development/deployment required",
        "Notify legal/compliance team immediately",
    ],
    RISK_HIGH: [
        "Risk management system (Article 9)",
        "Data governance (Article 10)",
        "Technical documentation — Annex IV (Article 11)",
        "Automatic logging / record-keeping (Article 12)",
        "Transparency & instructions for use (Article 13)",
        "Human oversight measures (Article 14)",
        "Accuracy, robustness & cybersecurity (Article 15)",
        "Quality management system (Article 17)",
        "Conformity assessment before market placement (Article 43)",
        "EU database registration (Article 49 / Article 71)",
        "CE marking (where applicable)",
        "Post-market monitoring (Article 72)",
        "Serious incident reporting (Article 73)",
        "Fundamental Rights Impact Assessment if deployer (Article 27)",
    ],
    RISK_LIMITED: [
        "Disclose to users they are interacting with an AI (Article 50(1)) — chatbots",
        "Label AI-generated content / deepfakes (Article 50(4)&(5))",
        "Inform individuals of emotion recognition / biometric categorisation (Article 50(3))",
        "GPAI model: technical documentation & training data summary (Article 53)",
    ],
    RISK_MINIMAL: [
        "No mandatory EU AI Act obligations",
        "Voluntary codes of conduct encouraged",
        "Best practice: maintain internal AI governance standards",
    ],
}


# ── Classification logic ───────────────────────────────────────────────────────

def classify_risk(row: dict) -> tuple[str, str, list[str]]:
    """
    Classify an AI system's risk tier based on CSV fields.

    Returns:
        (risk_tier, classification_reason, obligations_list)
    """
    use_case   = row.get("use_case_category", "").strip().lower()
    annex3     = row.get("annex_iii_area", "").strip()
    trans_obl  = row.get("transparency_obligation", "").strip().lower()
    gpai       = row.get("gpai_model", "").strip().lower()
    annex1     = row.get("annex_i_product", "").strip().lower()

    # Step 1 — Check for prohibited use cases (Article 5)
    prohibited_keywords = [
        "social scoring", "subliminal manipulation", "real-time biometric",
        "emotion recognition workplace", "facial scraping", "predictive policing",
        "exploit vulnerability", "biometric categorisation sensitive",
        "remote biometric identification public"
    ]
    for keyword in prohibited_keywords:
        if keyword in use_case:
            return (
                RISK_UNACCEPTABLE,
                f"Matches prohibited practice (Article 5): '{keyword}'",
                OBLIGATIONS[RISK_UNACCEPTABLE]
            )

    # Step 2 — Check for Annex I product (safety component) → High Risk
    if annex1 in ("yes", "true", "1", "y"):
        return (
            RISK_HIGH,
            "Safety component of Annex I product (Article 6(1))",
            OBLIGATIONS[RISK_HIGH]
        )

    # Step 3 — Check for Annex III use case → High Risk
    if annex3 and annex3 in ANNEX_III_AREAS:
        area_name = ANNEX_III_AREAS[annex3]
        return (
            RISK_HIGH,
            f"Annex III Area {annex3} — {area_name} (Article 6(2))",
            OBLIGATIONS[RISK_HIGH]
        )

    # Step 4 — Check for transparency obligation or GPAI → Limited Risk
    if trans_obl in ("yes", "true", "1", "y") or gpai in ("yes", "true", "1", "y"):
        reason = "GPAI model (Article 53)" if gpai in ("yes", "true", "1", "y") else "Transparency obligation (Article 50)"
        return (
            RISK_LIMITED,
            reason,
            OBLIGATIONS[RISK_LIMITED]
        )

    # Step 5 — Minimal risk
    return (
        RISK_MINIMAL,
        "No prohibited, high-risk, or transparency triggers identified",
        OBLIGATIONS[RISK_MINIMAL]
    )


# ── Core logic ────────────────────────────────────────────────────────────────

def classify_inventory(csv_path: str) -> list[dict]:
    """Read CSV and classify each AI system."""
    results = []
    path = Path(csv_path)

    if not path.exists():
        print(f"[ERROR] File not found: {csv_path}")
        sys.exit(1)

    required_cols = {
        "system_id", "system_name", "owner",
        "use_case_category", "annex_iii_area",
        "transparency_obligation", "gpai_model"
    }

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = required_cols - set(reader.fieldnames or [])
        if missing:
            print(f"[ERROR] CSV missing required columns: {missing}")
            sys.exit(1)

        for row in reader:
            risk_tier, reason, obligations = classify_risk(row)
            results.append({
                "system_id":   row["system_id"].strip(),
                "system_name": row["system_name"].strip(),
                "owner":       row["owner"].strip(),
                "risk_tier":   risk_tier,
                "reason":      reason,
                "obligations": obligations,
                "annex_iii":   ANNEX_III_AREAS.get(row.get("annex_iii_area", "").strip(), ""),
            })
    return results


# ── Reporting ─────────────────────────────────────────────────────────────────

def print_report(results: list[dict]) -> None:
    """Print formatted console report."""
    today = date.today().isoformat()
    total          = len(results)
    unacceptable   = sum(1 for r in results if r["risk_tier"] == RISK_UNACCEPTABLE)
    high           = sum(1 for r in results if r["risk_tier"] == RISK_HIGH)
    limited        = sum(1 for r in results if r["risk_tier"] == RISK_LIMITED)
    minimal        = sum(1 for r in results if r["risk_tier"] == RISK_MINIMAL)

    print("\n" + "=" * 80)
    print("  EU AI Act — AI System Risk Classification Report")
    print(f"  Run Date  : {today}")
    print(f"  Regulation: (EU) 2024/1689 — EU Artificial Intelligence Act")
    print("=" * 80)

    # Tier colour indicators
    tier_icons = {
        RISK_UNACCEPTABLE: "[BANNED]",
        RISK_HIGH:         "[HIGH  ]",
        RISK_LIMITED:      "[LTD   ]",
        RISK_MINIMAL:      "[MIN   ]",
    }

    print(f"\n  {'ID':<12}  {'System Name':<30}  {'Owner':<22}  {'Risk Tier':<18}  Reason")
    print("  " + "-" * 110)

    for r in results:
        icon = tier_icons.get(r["risk_tier"], "")
        print(
            f"  {r['system_id']:<12}  {r['system_name'][:29]:<30}  "
            f"{r['owner'][:21]:<22}  {icon} {r['risk_tier']:<18}  {r['reason'][:55]}"
        )

    print(f"\n{'─' * 70}")
    print("  SUMMARY")
    print(f"  Total AI Systems  : {total}")
    print(f"  [BANNED] Unacceptable : {unacceptable}")
    print(f"  [HIGH  ] High Risk    : {high}")
    print(f"  [LTD   ] Limited Risk : {limited}")
    print(f"  [MIN   ] Minimal Risk : {minimal}")
    print(f"{'─' * 70}\n")

    # Detail blocks for non-minimal systems
    for r in results:
        if r["risk_tier"] != RISK_MINIMAL:
            print(f"  ▶ [{r['system_id']}] {r['system_name']}")
            print(f"    Risk Tier : {r['risk_tier']}")
            print(f"    Reason    : {r['reason']}")
            print(f"    Key Obligations:")
            for obl in r["obligations"][:6]:
                print(f"      • {obl}")
            if len(r["obligations"]) > 6:
                print(f"      ... and {len(r['obligations']) - 6} more obligations")
            print()


def save_report(results: list[dict], output_path: str) -> None:
    """Save classification report to text file."""
    today = date.today().isoformat()
    lines = [
        "EU AI Act — AI System Risk Classification Report",
        f"Run Date  : {today}",
        f"Regulation: (EU) 2024/1689",
        "",
        f"{'ID':<12}  {'System Name':<30}  {'Owner':<22}  {'Risk Tier':<20}  Reason",
        "-" * 115,
    ]
    for r in results:
        lines.append(
            f"{r['system_id']:<12}  {r['system_name'][:29]:<30}  "
            f"{r['owner'][:21]:<22}  {r['risk_tier']:<20}  {r['reason']}"
        )

    lines += ["", "OBLIGATION DETAILS:", "-" * 60]
    for r in results:
        lines.append(f"\n[{r['system_id']}] {r['system_name']} — {r['risk_tier']}")
        lines.append(f"  Reason: {r['reason']}")
        lines.append("  Obligations:")
        for obl in r["obligations"]:
            lines.append(f"    - {obl}")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"  Report saved to: {output_path}\n")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="EU AI Act GRC Engineering — AI System Risk Classifier"
    )
    parser.add_argument(
        "--input", "-i",
        default="scripts/sample_ai_inventory.csv",
        help="Path to AI system inventory CSV (default: scripts/sample_ai_inventory.csv)"
    )
    parser.add_argument(
        "--output", "-o",
        default="scripts/risk_classification_report.txt",
        help="Path for output report file (default: scripts/risk_classification_report.txt)"
    )
    args = parser.parse_args()

    results = classify_inventory(args.input)
    print_report(results)
    save_report(results, args.output)

    # Exit code 1 if any UNACCEPTABLE RISK systems found (CI/CD pipeline support)
    prohibited = sum(1 for r in results if r["risk_tier"] == RISK_UNACCEPTABLE)
    sys.exit(1 if prohibited > 0 else 0)


if __name__ == "__main__":
    main()
