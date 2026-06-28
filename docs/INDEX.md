# Toolkit Index — Coverage Map

A single at-a-glance map of every document, the EU AI Act provisions it covers,
the role(s) it serves, and where it sits in the compliance lifecycle. Use this
to confirm an obligation is covered or to find the right document fast. For a
role-based walkthrough, see the **"Which Documents Apply to Me?"** table in the
main [README](../README.md).

> **New to the EU AI Act?** Start with **[QUICKSTART.md](QUICKSTART.md)** — a plain-language, 10-minute orientation.

> This index is a navigation aid. It does not constitute legal advice.

## Documents

| Doc | Title | Primary Article(s) / Annex | Role(s) | Lifecycle stage |
|-----|-------|----------------------------|---------|-----------------|
| 01 | Risk Classification Guide | Art. 5, 6, 50; Annex I, III | All | Classify |
| 02 | Conformity Assessment Checklist | Art. 43–48; Annex IV, VI, VII | Provider | Place on market |
| 03 | Fundamental Rights Impact Assessment (FRIA) | Art. 27 | Deployer | Build |
| 04 | Technical Documentation Template | Art. 11; Annex IV | Provider | Build |
| 05 | AI System Register | Art. 49, 71 | All | Operate |
| 06 | Transparency Obligations Checklist | Art. 50, 53 | All | Operate |
| 07 | Human Oversight Framework | Art. 14 | Both | Build / Operate |
| 08 | Incident Reporting Procedure | Art. 73 (tiered 2/10/15-day deadlines) | Both | Operate |
| 09 | Post-Market Monitoring Plan | Art. 72 | Provider | Operate |
| 10 | Provider & Deployer Responsibilities | Art. 16, 26 | All | Classify |
| 11 | GPAI Technical Documentation | Art. 51, 53–55; Annex XI, XII | GPAI provider | Build |
| 12 | EU Declaration of Conformity | Art. 47; Annex V | Provider | Place on market |
| 13 | Authorised Representative | Art. 22 | Non-EU provider | Place on market |
| 14 | CE Marking Guide | Art. 48; Annex I | Provider | Place on market |
| 15 | Importer & Distributor Checklists | Art. 23–24 | Importer / Distributor | Place on market |
| 16 | Quality Management System | Art. 17 | Provider | Build |
| 17 | AI Literacy & Competency Framework | Art. 4, 14(3) | All | Build / Operate |
| 18 | GDPR × EU AI Act Intersection Map | Art. 9, 10, 13, 26, 27, 86 + GDPR | All | Build / Operate |
| 19 | Master Compliance Scorecard | All Articles | All | Screen / Classify |
| 20 | Notified Body Engagement Guide | Art. 43–46; Annex VII | Provider | Place on market |
| 21 | Legitimate Interest Assessment (LIA) | GDPR Art. 6(1)(f); AI Act Art. 10 | All | Build |
| 22 | Worker Information Notice | Art. 26(7) | Deployer | Operate |
| 23 | Annex VII Assessment Criteria Checklist | Annex VII; Art. 43–44 | Provider | Place on market |
| 24 | Worked Example: Credit Scoring AI | All Articles | All | Reference |
| 25 | Prohibited Practices Assessment | Art. 5; Recitals 28–45 | All | Screen |
| 26 | Risk Management System | Art. 9 | Provider | Build |
| 27 | GPAI Systemic Risk Compliance Guide | Art. 51, 55–56, 88–94; Annex XIII | GPAI provider | Build |
| 28 | Market Surveillance & Regulatory Response | Art. 74–99 (incl. 88–94 for GPAI); Art. 18 | All | Operate |

## Guides

| File | Purpose |
|------|---------|
| QUICKSTART.md | Plain-language 10-minute orientation to the EU AI Act |
| INDEX.md | This coverage map |

## Worked Examples

| File | Scenario |
|------|----------|
| WORKED-EXAMPLE-HR-SCREENING-SYSTEM.md | CV screening AI (Annex III Area 4, Employment) |
| 24-WORKED-EXAMPLE-CREDIT-SCORING-AI.md | Credit scoring AI (Annex III Area 5), provider/deployer split |

## Automation

| File | Purpose |
|------|---------|
| scripts/risk_classifier.py | CLI risk-tier classifier v2.2 (txt / json / csv output; GPAI handled as a parallel regime) |
| scripts/sample_ai_inventory.csv | Sample inventory covering all tiers |
| scripts/sample_ai_inventory_TEMPLATE.csv | Header-only template for your own inventory |
| scripts/test_risk_classifier.py | Unit tests for the classifier |

## Lifecycle stages

- **Screen** — rule out prohibited practices and establish your position before anything else (Docs 25, 19).
- **Classify** — determine risk tier and role (Docs 01, 10).
- **Build** — implement the controls a high-risk system needs before placement (Docs 03, 04, 07, 16, 26, etc.).
- **Place on market** — conformity, declaration, CE marking, supply-chain steps (Docs 02, 12, 13, 14, 15, 20, 23).
- **Operate** — ongoing monitoring, incidents, registration, enforcement readiness (Docs 05, 06, 08, 09, 22, 28).
- **Reference** — worked examples and supporting material.

---

*Part of the EU AI Act Compliance Toolkit. This document does not constitute legal advice.*
