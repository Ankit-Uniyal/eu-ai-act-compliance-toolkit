# /scripts — GRC Engineering Automation

**Bridging EU AI Act Policy and Engineering** — turning regulatory requirements into executable, repeatable checks.

This folder contains automation scripts that operationalise EU AI Act compliance controls. Rather than treating the regulation as a static document exercise, these scripts enable continuous compliance monitoring — a core principle of GRC Engineering.

## Scripts

| Script | Purpose | EU AI Act Reference |
|--------|---------|---------------------|
| `risk_classifier.py` | Classifies AI systems by EU AI Act risk tier from a CSV inventory | Articles 5, 6, 50 |
| `sample_ai_inventory.csv` | Sample 16-system AI inventory covering all risk tiers | Input for risk_classifier.py |
| `sample_ai_inventory_TEMPLATE.csv` | Header-only template (with guidance comments) for your own inventory | Input template |
| `test_risk_classifier.py` | Unit tests for the classifier (stdlib unittest) | — |

## risk_classifier.py

### What it does

Reads a CSV inventory of AI systems and applies the EU AI Act's four-tier risk classification framework to each system:

| Risk Tier | Classification Logic | Key Obligations |
|-----------|----------------------|-----------------|
| **UNACCEPTABLE RISK** | Explicit `prohibited_practice` flag OR Article 5 keyword match | System banned — immediate action required |
| **HIGH RISK** | Annex I safety component OR Annex III use case (unless an Art. 6(3) exclusion applies) | Full conformity obligations (Articles 9–17, 43–49) |
| **LIMITED RISK** | Transparency obligation or GPAI model | Disclosure obligations (Articles 50, 53) |
| **MINIMAL RISK** | None of the above | Voluntary codes of conduct |

The script also:

- Applies **Article 6(3) exclusion logic** to downgrade Annex III systems that qualify (with a documented-justification warning)
- Lists the specific obligations triggered for each system
- Saves a full classification report to file (txt, json, or csv)
- **Exits with code 1** if any UNACCEPTABLE RISK (prohibited) systems are detected — enabling CI/CD pipeline enforcement

> **DISCLAIMER:** Classifier output is a **triage aid**, not a legal determination. Human compliance review is mandatory before acting on any classification.

### Requirements

- Python 3.9+
- No external dependencies (standard library only)

### Usage

```bash
# Basic run with the sample inventory
python scripts/risk_classifier.py

# Custom input file
python scripts/risk_classifier.py --input path/to/your/inventory.csv

# Machine-readable output for GRC platforms / dashboards
python scripts/risk_classifier.py --format json
python scripts/risk_classifier.py --format csv

# Custom output report
python scripts/risk_classifier.py --input scripts/sample_ai_inventory.csv --output reports/q2_risk_report.txt

# Version
python scripts/risk_classifier.py --version
```

### CSV Format

Your inventory CSV must contain the following **required** columns:

| Column | Description | Values |
|--------|-------------|--------|
| `system_id` | Unique identifier | e.g. AI-EU-001 |
| `system_name` | System name | Text |
| `owner` | Accountable team/person | Text |
| `use_case_category` | Plain-text description of use case | Text (scanned for Article 5 keywords) |
| `annex_iii_area` | Annex III area number (1–8) if applicable | 1 to 8 or blank |
| `annex_i_product` | Is it a safety component of an Annex I product? | yes / no |
| `transparency_obligation` | Does Article 50 apply (chatbot, deepfake, etc.)? | yes / no |
| `gpai_model` | Is it a General-Purpose AI model? | yes / no |
| `provider_or_deployer` | Role of your organisation | provider / deployer / both |

The following columns are **strongly recommended** (v2.0+). If absent, the script still runs but prints a warning and falls back to keyword-only prohibited-practice detection:

| Column | Description | Values |
|--------|-------------|--------|
| `prohibited_practice` | Explicit Article 5 prohibited-practice flag | yes / no |
| `exclusion_narrow_task` | Art. 6(3)(a): narrow procedural task only | yes / no |
| `exclusion_human_result` | Art. 6(3)(b): improves prior human result only | yes / no |
| `exclusion_no_individual` | Art. 6(3)(c): no individual influence | yes / no |
| `exclusion_preparatory` | Art. 6(3)(d): preparatory task only | yes / no |

> Set `exclusion_*` to `yes` only with a documented Art. 6(3) justification (record it in `05-AI-SYSTEM-REGISTER.md`). Misapplication creates regulatory risk.

**Annex III Area Reference:**

| Area | Use Case Category |
|------|-------------------|
| 1 | Biometrics |
| 2 | Critical Infrastructure |
| 3 | Education & Vocational Training |
| 4 | Employment & Workers Management |
| 5 | Essential Private/Public Services (credit, insurance, benefits) |
| 6 | Law Enforcement |
| 7 | Migration, Asylum & Border Control |
| 8 | Administration of Justice |

### Sample Output (txt)

```
========================================================================================
EU AI Act -- AI System Risk Classification Report (v2.1)
Run Date   : 2026-04-29 09:14:22
Input File : scripts/sample_ai_inventory.csv
Regulation : (EU) 2024/1689 -- EU Artificial Intelligence Act
DISCLAIMER : Triage aid only. Human compliance review is mandatory.
========================================================================================

ID           System Name                         Owner                Tier       Reason
----------------------------------------------------------------------------------------
AI-EU-001    Resume Screening Engine             HR Technology        [HIGH ]    HIGH -- Annex III Area 4: Employment...
AI-EU-003    Customer Support Chatbot            CX Technology        [LTD ]     LIMITED -- transparency obligation (Article 50)
AI-EU-007    Real-time Biometric ID CCTV         Security Ops         [BANNED]   Prohibited (explicit flag)
AI-EU-009    LLM Foundation Model                AI Platform          [LTD ]     LIMITED -- GPAI model (Article 53)
AI-EU-014    Spam Filter                         IT Security          [MIN ]     MINIMAL -- no Article 5, 6, or 50 triggers
AI-EU-016    Interview Scheduler Assistant       HR Technology        [MIN ]     MINIMAL -- no Article 5, 6, or 50 triggers

ARTICLE 6(3) EXCLUSIONS (require documented justification):
  AI-EU-016 Interview Scheduler Assistant: Art. 6(3)(a): narrow procedural task only

----------------------------------------------------------------------------------------
SUMMARY
  Total    : 16
  [BANNED] : 1
  [HIGH ]  : 7
  [LTD ]   : 4
  [MIN ]   : 4
----------------------------------------------------------------------------------------
```

The `--format json` and `--format csv` options produce machine-readable output for ingestion into GRC platforms, the AI System Register (Doc 05), the Master Scorecard (Doc 19), or BI dashboards.

## CI/CD Integration

A ready-to-run workflow ships in [`.github/workflows/eu-ai-act-risk-check.yml`](../.github/workflows/eu-ai-act-risk-check.yml). It runs the unit tests, classifies the sample inventory on every push to `scripts/` and weekly, and uploads the report as an artifact.

> The classifier exits with code 1 when an UNACCEPTABLE RISK (prohibited) system is found. The shipped workflow marks that step `continue-on-error` because the **sample** inventory intentionally contains one banned system for demonstration. When you point the workflow at a **real** inventory, remove `continue-on-error` so the gate actually blocks the pipeline.

## Running the tests

```bash
python -m unittest discover -s scripts -p "test_*.py"
```

## EU AI Act Alignment

| Script Feature | EU AI Act Reference | How It Helps |
|----------------|---------------------|--------------|
| Explicit + keyword prohibited-practice detection | Article 5 | Immediately flags banned AI systems |
| Annex I product classification | Article 6(1) | Identifies safety-critical product AI |
| Annex III use case classification | Article 6(2) | Maps systems to high-risk categories |
| Article 6(3) exclusion logic | Article 6(3) | Downgrades qualifying Annex III systems, with justification warning |
| Transparency obligation detection | Article 50 | Flags limited-risk disclosure requirements |
| GPAI model identification | Article 53 | Surfaces GPAI-specific obligations |
| Obligation list per system | Articles 9–17, 26, 27, 43–49, 72, 73 | Actionable compliance requirements |
| CI/CD integration | — | Continuous compliance — not point-in-time |

---

*Part of the EU AI Act Compliance Toolkit*
