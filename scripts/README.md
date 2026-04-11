# /scripts — GRC Engineering Automation

> **Bridging EU AI Act Policy and Engineering** — turning regulatory requirements into executable, repeatable checks.

This folder contains automation scripts that operationalise EU AI Act compliance controls. Rather than treating the regulation as a static document exercise, these scripts enable **continuous compliance monitoring** — a core principle of GRC Engineering.

---

## Scripts

| Script | Purpose | EU AI Act Reference |
|--------|---------|---------------------|
| `risk_classifier.py` | Classifies AI systems by EU AI Act risk tier from a CSV inventory | Articles 5, 6, 50 | Annexes I, III |
| `sample_ai_inventory.csv` | Sample 15-system AI inventory covering all risk tiers | Input for risk_classifier.py |

---

## risk_classifier.py

### What it does

Reads a CSV inventory of AI systems and applies the EU AI Act's four-tier risk classification framework to each system:

| Risk Tier | Classification Logic | Key Obligations |
|-----------|---------------------|----------------|
| **UNACCEPTABLE RISK** | Matches Article 5 prohibited practices | System banned — immediate action required |
| **HIGH RISK** | Annex I safety component OR Annex III use case | Full conformity obligations (Articles 9–17, 43–49) |
| **LIMITED RISK** | Transparency obligation or GPAI model | Disclosure obligations (Articles 50, 53) |
| **MINIMAL RISK** | None of the above | Voluntary codes of conduct |

The script also:
- Lists the specific obligations triggered for each system
- Saves a full classification report to file
- Exits with code `1` if any UNACCEPTABLE RISK (prohibited) systems are detected — enabling CI/CD pipeline enforcement

### Requirements

- Python 3.9+
- No external dependencies (standard library only)

### Usage

```bash
# Basic run with the sample inventory
python scripts/risk_classifier.py

# Custom input file
python scripts/risk_classifier.py --input path/to/your/inventory.csv

# Custom output report
python scripts/risk_classifier.py --input scripts/sample_ai_inventory.csv --output reports/q2_risk_report.txt
```

### CSV Format

Your inventory CSV must contain the following columns:

| Column | Description | Values |
|--------|-------------|--------|
| `system_id` | Unique identifier | e.g. `AI-EU-001` |
| `system_name` | System name | Text |
| `owner` | Accountable team/person | Text |
| `use_case_category` | Plain-text description of use case | Text (scanned for Article 5 keywords) |
| `annex_iii_area` | Annex III area number (1–8) if applicable | `1` to `8` or blank |
| `annex_i_product` | Is it a safety component of an Annex I product? | `yes` / `no` |
| `transparency_obligation` | Does Article 50 apply (chatbot, deepfake, etc.)? | `yes` / `no` |
| `gpai_model` | Is it a General-Purpose AI model? | `yes` / `no` |
| `provider_or_deployer` | Role of your organisation | `provider` / `deployer` / `both` |

**Annex III Area Reference:**

| Area | Use Case Category |
|------|-----------------|
| 1 | Biometrics |
| 2 | Critical Infrastructure |
| 3 | Education & Vocational Training |
| 4 | Employment & Workers Management |
| 5 | Essential Private/Public Services (credit, insurance, benefits) |
| 6 | Law Enforcement |
| 7 | Migration, Asylum & Border Control |
| 8 | Administration of Justice |

### Sample Output

```
================================================================================
  EU AI Act — AI System Risk Classification Report
  Run Date  : 2026-04-11
  Regulation: (EU) 2024/1689 — EU Artificial Intelligence Act
================================================================================

  ID            System Name                     Owner                   Risk Tier            Reason
  ---------------------------------------------------------------------------------------------------------------
  AI-EU-001     Resume Screening Engine         HR Technology           [HIGH  ] HIGH RISK   Annex III Area 4 — Employment
  AI-EU-003     Customer Support Chatbot        CX Technology           [LTD   ] LIMITED RISK  Transparency obligation (Article 50)
  AI-EU-007     Real-time Biometric ID CCTV     Security Ops            [BANNED] UNACCEPTABLE  Prohibited: 'real-time biometric...'
  AI-EU-009     LLM Foundation Model            AI Platform             [LTD   ] LIMITED RISK  GPAI model (Article 53)
  AI-EU-014     Spam Filter                     IT Security             [MIN   ] MINIMAL RISK  No triggers identified

──────────────────────────────────────────────────────────────────────
  SUMMARY
  Total AI Systems  : 15
  [BANNED] Unacceptable : 1
  [HIGH  ] High Risk    : 7
  [LTD   ] Limited Risk : 4
  [MIN   ] Minimal Risk : 3
──────────────────────────────────────────────────────────────────────
```

---

## CI/CD Integration

Integrate into GitHub Actions to automatically flag prohibited AI systems in your inventory on every push or scheduled run:

```yaml
# .github/workflows/eu-ai-act-risk-check.yml
name: EU AI Act Risk Classification Check

on:
  push:
    paths:
      - 'scripts/sample_ai_inventory.csv'
  schedule:
    - cron: '0 8 * * 1'   # Every Monday 08:00 UTC
  workflow_dispatch:

jobs:
  classify-ai-systems:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Run EU AI Act Risk Classifier
        run: |
          python scripts/risk_classifier.py \
            --input scripts/sample_ai_inventory.csv \
            --output scripts/risk_classification_report.txt

      - name: Upload Risk Report
        uses: actions/upload-artifact@v4
        with:
          name: eu-ai-act-risk-report
          path: scripts/risk_classification_report.txt
```

> **Note:** The workflow will **fail** (exit code 1) if any UNACCEPTABLE RISK (prohibited) systems are found in the inventory — preventing prohibited AI systems from remaining undetected.

---

## EU AI Act Alignment

| Script Feature | EU AI Act Reference | How It Helps |
|----------------|---------------------|-------------|
| Article 5 prohibited practice detection | Article 5 | Immediately flags banned AI systems |
| Annex I product classification | Article 6(1) | Identifies safety-critical product AI |
| Annex III use case classification | Article 6(2) | Maps systems to high-risk categories |
| Transparency obligation detection | Article 50 | Flags limited-risk disclosure requirements |
| GPAI model identification | Article 53 | Surfaces GPAI-specific obligations |
| Obligation list per system | Articles 9–17, 26, 27, 43–49, 72, 73 | Actionable compliance requirements |
| CI/CD integration | — | Continuous compliance — not point-in-time |

---

*Part of the [EU AI Act Compliance Toolkit](../README.md)*
