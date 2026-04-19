# EU AI Act Compliance Toolkit

**Version 2.0.0 | April 2026**

A practical, practitioner-built compliance toolkit for the EU Artificial Intelligence Act (Regulation (EU) 2024/1689). Upgraded in v2.0 with GPAI documentation, Declaration of Conformity, Authorised Representative, CE Marking, Importer/Distributor checklists, worked examples, and an improved risk classifier.

## Overview

The EU AI Act (entered into force 1 August 2024) is the world's first comprehensive legal framework for artificial intelligence. It applies a risk-based approach, imposing obligations proportional to the potential harm an AI system can cause -- to providers, deployers, importers, and distributors operating in or supplying to the EU market.

This toolkit translates the Act's 113 Articles and 13 Annexes into actionable templates, checklists, and automation scripts that GRC professionals, AI governance practitioners, and compliance teams can use immediately.

## Compliance Timeline

| Milestone | Date |
|---|---|
| EU AI Act enters into force | 1 August 2024 |
| Prohibited AI systems banned | 2 February 2025 |
| GPAI model rules apply | 2 August 2025 |
| High-risk AI systems (Annex I) obligations | 2 August 2026 |
| All remaining provisions fully applicable | 2 August 2027 |

## Risk Tier Framework

The EU AI Act classifies AI systems into four risk tiers:

| Tier | Description | Examples |
|---|---|---|
| Unacceptable Risk (Article 5) | Prohibited -- banned outright | Social scoring, subliminal AI, real-time biometric ID in public |
| High Risk (Articles 6-51, Annexes I and III) | Strict obligations: conformity assessment, registration, oversight | CV screening, credit scoring, medical devices with AI |
| Limited Risk (Articles 50, 52) | Transparency obligations only | Chatbots, deepfakes, GPAI models |
| Minimal Risk | Voluntary codes of conduct | Spam filters, AI in games |

## Toolkit Structure

### Core Compliance Documents (01-10)

| # | Document | Purpose | EU AI Act Reference |
|---|---|---|---|
| 01 | Risk Classification Guide | Classify your AI system by risk tier | Articles 5, 6, 50 + Annexes I, III |
| 02 | Conformity Assessment Checklist | Pre-market conformity checklist for high-risk AI | Articles 43-48 |
| 03 | Fundamental Rights Impact Assessment | FRIA template for deployers of high-risk AI | Article 27 |
| 04 | Technical Documentation Template | Annex IV-compliant technical documentation | Article 11 + Annex IV |
| 05 | AI System Register | Inventory of AI systems with risk classification | Articles 49, 71 |
| 06 | Transparency Obligations Checklist | Obligations for limited-risk and GPAI systems | Articles 50, 53 |
| 07 | Human Oversight Framework | Design and operational human oversight controls | Article 14 |
| 08 | Incident Reporting Procedure | Serious incident reporting to market surveillance | Article 73 |
| 09 | Post-Market Monitoring Plan | Ongoing monitoring and logging obligations | Article 72 |
| 10 | Provider and Deployer Responsibilities | Role-based obligation matrix | Articles 16, 26 |

### New in v2.0 (Documents 11-15)

| # | Document | Purpose | EU AI Act Reference |
|---|---|---|---|
| 11 | GPAI Technical Documentation | Annex XI/XII template for foundation/LLM model providers | Articles 51, 53-56, Annexes XI, XII |
| 12 | EU Declaration of Conformity | Article 47 DoC template with all required fields | Article 47, Annex V |
| 13 | Authorised Representative | Article 22 designation agreement for non-EU providers | Article 22 |
| 14 | CE Marking Guide | When CE marking is required and how to affix it | Article 48, Annex I |
| 15 | Importer and Distributor Checklists | Dedicated checklists for supply chain roles | Articles 23-24 |

### Worked Example

| File | Description |
|---|---|
| WORKED-EXAMPLE-HR-SCREENING-SYSTEM.md | Completed example: CV screening AI system (fictional HireRight GmbH / TalentFilter Pro). Shows application of all 10 core documents with realistic data. |

### GRC Engineering -- Automation Scripts

| Script | Purpose | Automates |
|---|---|---|
| scripts/risk_classifier.py (v2.0) | CLI tool to classify AI systems by EU AI Act risk tier | Risk classification workflow with Art. 6(3) exclusion logic |
| scripts/sample_ai_inventory.csv | Sample 15-system AI inventory covering all risk tiers | Input for risk_classifier.py |

## Who This Is For

- GRC professionals building AI compliance programmes
- AI governance practitioners mapping systems to regulatory requirements
- Legal and compliance teams preparing for EU AI Act obligations
- AI product teams understanding what their systems must do before deployment
- Auditors assessing AI systems against the EU AI Act framework
- Importers and distributors of AI systems needing supply chain due diligence

## How to Use This Toolkit

1. **Classify** your AI systems using 01-RISK-CLASSIFICATION-GUIDE.md or run scripts/risk_classifier.py
2. **If High Risk:** complete 02-CONFORMITY-ASSESSMENT-CHECKLIST.md and 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md
3. **If deploying High Risk AI:** complete the FRIA (03) -- required for public sector and public-service deployers
4. **For all AI systems:** check 06-TRANSPARENCY-OBLIGATIONS.md and 07-HUMAN-OVERSIGHT-FRAMEWORK.md
5. **Register** all systems in 05-AI-SYSTEM-REGISTER.md
6. **Establish ongoing processes:** 08-INCIDENT-REPORTING-PROCEDURE.md and 09-POST-MARKET-MONITORING-PLAN.md
7. **Non-EU providers:** complete 13-AUTHORISED-REPRESENTATIVE.md before market placement
8. **Annex I product providers:** follow 14-CE-MARKING-GUIDE.md and complete 12-EU-DECLARATION-OF-CONFORMITY.md
9. **Importers and Distributors:** follow 15-IMPORTER-DISTRIBUTOR-CHECKLISTS.md
10. **GPAI/LLM model providers:** complete 11-GPAI-TECHNICAL-DOCUMENTATION.md instead of (or in addition to) Document 04

## GRC Automation -- risk_classifier.py v2.0

The upgraded classifier adds Article 6(3) exclusion logic and a structured prohibited_practice field:

```bash
# Basic run with sample inventory
python scripts/risk_classifier.py

# Custom input file
python scripts/risk_classifier.py --input path/to/your/inventory.csv

# Custom output report
python scripts/risk_classifier.py --input scripts/sample_ai_inventory.csv --output reports/q2_risk_report.txt
```

New in v2.0 -- add these columns to your CSV for complete classification:

| New Column | Values | Purpose |
|---|---|---|
| prohibited_practice | yes / no | Explicit Article 5 prohibited practice flag |
| exclusion_narrow_task | yes / no | Article 6(3)(a): narrow procedural task only |
| exclusion_human_result | yes / no | Article 6(3)(b): improves result of prior human activity |
| exclusion_no_individual | yes / no | Article 6(3)(c): no individual influence |
| exclusion_preparatory | yes / no | Article 6(3)(d): preparatory task only |

**Important:** Classifier output is a triage aid. Human compliance review is mandatory before acting on any classification.

## Key Definitions

| Term | Definition |
|---|---|
| Provider | Entity that develops or places an AI system on the market |
| Deployer | Entity that uses an AI system in a professional context |
| Importer | EU-established entity placing a non-EU provider's AI on the EU market |
| Distributor | Entity making AI available on market without modifying it |
| Operator | Collective term for providers and deployers |
| GPAI Model | General-purpose AI model (e.g. foundation models / LLMs) |
| Notified Body | Third-party conformity assessment body |
| FRIA | Fundamental Rights Impact Assessment |

## Related Resources

- [EU AI Act Full Text (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office)
- [High-Risk AI Systems List (Annex III)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#anx3)
- [NANDO Database -- Notified Bodies](https://ec.europa.eu/growth/tools-databases/nando/)
- [ISO/IEC 42001:2023 AI Governance](https://www.iso.org/standard/81230.html)
- [ISO/IEC 23894:2023 AI Risk Management](https://www.iso.org/standard/77304.html)

## Versioning and Changelog

See [CHANGELOG.md](CHANGELOG.md) for full version history, regulatory coverage tracking, and planned updates.

Current version: **v2.0.0** (April 2026) -- see CHANGELOG.md for what's new.

## Disclaimer

This toolkit is provided for informational and educational purposes. It does not constitute legal advice. Always consult qualified legal counsel for compliance decisions.

*Maintained by Ankit Uniyal | AI Governance and GRC Engineering*
