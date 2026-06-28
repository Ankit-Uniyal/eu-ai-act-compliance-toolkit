# EU AI Act Compliance Toolkit
## Version 3.3.0 | June 2026

A practical, practitioner-built compliance toolkit for the EU Artificial Intelligence Act (Regulation (EU) 2024/1689). Now with **28 compliance documents**, 2 worked examples, and GRC automation scripts — covering every major obligation from risk classification through market surveillance response.

**New here?** Start with **[docs/QUICKSTART.md](docs/QUICKSTART.md)** — a plain-language, 10-minute overview of the four risk tiers, the real compliance deadlines, and the first three things to do.

**New in v3.3.0:** Updated to reflect official EU developments through mid-2026 — the Commission's February 2025 guidelines on prohibited practices and on the AI system definition, the **General-Purpose AI Code of Practice** (published 10 July 2025), and the Code of Practice on marking and labelling AI-generated content (June 2026). See **[Recent Official Guidance & Developments](#recent-official-guidance--developments)** below.

---

## Overview

The EU AI Act (entered into force 1 August 2024) is the world's first comprehensive legal framework for artificial intelligence. It applies a risk-based approach, imposing obligations proportional to the potential harm an AI system can cause — to providers, deployers, importers, and distributors operating in or supplying to the EU market.

This toolkit translates the Act's Articles and Annexes into actionable templates, checklists, and automation scripts that GRC professionals, AI governance practitioners, and compliance teams can use immediately.

---

## Compliance Timeline

| Milestone | Date |
|---|---|
| EU AI Act enters into force | 1 August 2024 |
| Prohibited practices (Art. 5) banned; AI literacy (Art. 4) applies | **2 February 2025** |
| GPAI model obligations + governance/penalties apply | **2 August 2025** |
| Annex III high-risk obligations + most of the Act apply | **2 August 2026** |
| High-risk AI that are Annex I products (embedded safety components) apply (Art. 6(1)) | **2 August 2027** |
| GPAI models already on the market before 2 Aug 2025 must be compliant | 2 August 2027 |

> Note: the 2 August 2026 date covers Annex III high-risk systems (Art. 6(2)); the obligations tied to Art. 6(1) (high-risk AI that are safety components of Annex I regulated products) apply from 2 August 2027. Legacy public-authority high-risk systems have until 2 August 2030. Always verify current dates against EUR-Lex, as delegated/implementing acts may adjust details.

---

## Recent Official Guidance & Developments

The framework is now in force in stages, and the Commission and the European AI Office have published official guidance that this toolkit aligns to. Use these primary sources alongside the templates here:

| Date | Development | What it means for you |
|---|---|---|
| Feb 2025 | **Guidelines on prohibited AI practices** (Art. 5) and **Guidelines on the AI system definition** | Authoritative, example-rich interpretation of the eight bans and of what counts as an "AI system." Read these before completing Doc 25. |
| 10 Jul 2025 | **General-Purpose AI (GPAI) Code of Practice** — three chapters: Transparency, Copyright, and Safety & Security | Voluntary but Commission-endorsed route to demonstrate compliance. Transparency + Copyright chapters map to **Art. 53** (all GPAI providers); the Safety & Security chapter maps to **Art. 55** (GPAI with systemic risk). Includes a Model Documentation Form. Referenced by Docs 06, 11, and 27. |
| 2 Aug 2025 | GPAI obligations, governance, notified bodies, confidentiality, and **penalties** (Arts. 99–100) became applicable | Enforcement architecture is live. National market surveillance authorities and the AI Office now have active powers. |
| Jun 2026 | **Code of Practice on marking and labelling AI-generated content** (Art. 50) | Practical guidance for the transparency/labelling duties that become enforceable 2 August 2026. Relevant to Doc 06. |

Supporting initiatives: the **AI Pact** (voluntary early-compliance pledge), the **AI Act Service Desk** and **Single Information Platform** (official Q&A and help), and the **European AI Office** (GPAI supervision and enforcement coordination). Links in [Related Resources](#related-resources).

> These are the Commission's own materials. They are interpretive guidance, not amendments to the Act — the binding text remains Regulation (EU) 2024/1689 on EUR-Lex.

---

## Risk Tier Framework

The EU AI Act classifies AI **systems** into four risk tiers. **General-purpose AI (GPAI) models are governed by a separate, parallel regime** (Arts. 51–56) and are **not** a sub-tier of "limited risk" — a GPAI model can also be embedded inside a high-risk system.

| Tier | Description | Examples |
|---|---|---|
| Unacceptable Risk (Article 5) | Prohibited — banned outright | Social scoring, manipulative/subliminal AI, untargeted facial scraping, real-time biometric ID in public spaces |
| High Risk (Article 6, Annexes I and III) | Strict obligations: risk management, data governance, conformity assessment, registration, oversight | CV screening, credit scoring, medical devices with AI |
| Limited Risk (Article 50) | Transparency obligations only (overlay — can also apply to higher tiers) | Chatbots, deepfakes, AI-generated content |
| Minimal Risk (Article 95) | Voluntary codes of conduct | Spam filters, AI in games |
| **GPAI models — separate regime (Arts. 51–56)** | **Baseline obligations for all GPAI (Arts. 53–54); additional systemic-risk obligations (Art. 55) if > 10^25 FLOP or designated. The GPAI Code of Practice is the endorsed way to show compliance.** | **Foundation models / LLMs** |

---

## Which Documents Apply to Me?

Use this routing guide to find the documents most relevant to your role and situation:

| I am a... | Start here | Also use |
|---|---|---|
| New to the toolkit | docs/QUICKSTART.md → Worked Examples | 01, 19, 25 |
| Provider building a high-risk AI system | 01 → 25 → 02 → 04 → 26 → 16 | 03, 07, 08, 09, 10, 17, 18, 19, 20, 21, 23, 28 |
| Deployer putting a high-risk AI system into service | 01 → 25 → 10 → 07 → 17 | 03, 08, 09, 18, 19, 22, 28 |
| Both provider and deployer (same organisation) | 01 → 25 → 02 → 04 → 10 → 26 → 16 | All applicable documents |
| Non-EU provider placing on EU market | 01 → 25 → 13 → 02 → 04 | 12, 14, 15, 16, 20, 28 |
| Importer of an AI system | 15 → 01 → 25 | 12, 13, 14 |
| Distributor of an AI system | 15 → 01 → 25 | 12, 13, 14 |
| GPAI / LLM model provider | 11 → 06 | 01, 16, 18, 21, 27 |
| GPAI provider with systemic risk model | 11 → 27 → 06 | 01, 08, 16, 18, 21 |
| Legal/Compliance team doing gap analysis | 19 → 01 → 25 | All documents flagged as gaps |
| Processing personal data in AI | 18 → 21 | 03, 04, 08 |
| Deploying AI in the workplace | 22 → 07 → 17 | 10, 19 |
| Preparing for Notified Body assessment | 20 → 23 → 02 → 04 → 26 → 16 | 12 |
| Preparing for market surveillance inspection | 28 → 19 | All technical documentation |

---

## Toolkit Structure

### Core Compliance Documents (01-10)

| # | Document | Purpose | EU AI Act Reference |
|---|---|---|---|
| 01 | Risk Classification Guide | Classify your AI system by risk tier | Articles 5, 6, 50 + Annexes I, III |
| 02 | Conformity Assessment Checklist | Pre-market conformity checklist for high-risk AI | Articles 43-48, Annexes VI, VII |
| 03 | Fundamental Rights Impact Assessment | FRIA template for deployers of high-risk AI | Article 27 |
| 04 | Technical Documentation Template | Annex IV-compliant technical documentation | Article 11 + Annex IV |
| 05 | AI System Register | Inventory of AI systems with risk classification | Articles 49, 71 |
| 06 | Transparency Obligations Checklist | Obligations for limited-risk and GPAI systems (aligned to the GPAI Code of Practice Transparency chapter and the AI-generated-content labelling Code) | Articles 50, 53 |
| 07 | Human Oversight Framework | Design and operational human oversight controls | Article 14 |
| 08 | Incident Reporting Procedure | Serious incident reporting (tiered 2/10/15-day deadlines) | Article 73 |
| 09 | Post-Market Monitoring Plan | Ongoing monitoring and logging obligations | Article 72 |
| 10 | Provider and Deployer Responsibilities | Role-based obligation matrix | Articles 16, 26 |

### New in v2.0 (Documents 11-15)

| # | Document | Purpose | EU AI Act Reference |
|---|---|---|---|
| 11 | GPAI Technical Documentation | Annex XI/XII template for foundation/LLM model providers (aligned to the GPAI Code of Practice Transparency & Copyright chapters, Art. 53) | Articles 51, 53-55, Annexes XI, XII |
| 12 | EU Declaration of Conformity | Article 47 DoC template with all required fields | Article 47, Annex V |
| 13 | Authorised Representative | Article 22 designation agreement for non-EU providers | Article 22 |
| 14 | CE Marking Guide | When CE marking is required and how to affix it | Article 48, Annex I |
| 15 | Importer and Distributor Checklists | Dedicated checklists for supply chain roles | Articles 23-24 |

### New in v3.0 (Documents 16-20)

| # | Document | Purpose | EU AI Act Reference |
|---|---|---|---|
| 16 | Quality Management System | Article 17 QMS template covering policy, design, data governance, documentation, PMM, incidents, and audit | Article 17 |
| 17 | AI Literacy and Competency Framework | Role-based training programme, competency levels, assessment tool, Article 14(3) oversight person certification | Article 4, Article 14(3) |
| 18 | GDPR × EU AI Act Intersection Map | Systematic mapping of GDPR and AI Act obligations: data governance, automated decisions, DPIA/FRIA, transparency, dual incident reporting | Articles 9, 10, 13, 26, 27, 86 |
| 19 | Master Compliance Scorecard | Consolidated 118-item gap analysis across all documents; executive dashboard; P1-P4 priority tracking | All Articles |
| 20 | Notified Body Engagement Guide | When a Notified Body is required, how to find and select one, assessment process, certificate maintenance | Articles 43-46, Annex VII |

### New in v3.1.0 (Documents 21-24)

| # | Document | Purpose | Reference |
|---|---|---|---|
| 21 | Legitimate Interest Assessment (LIA) | Three-part LIA template for AI training data processing under GDPR Art. 6(1)(f) | GDPR Art. 6(1)(f); AI Act Art. 10 |
| 22 | Worker Information Notice | Art. 26(7) pre-deployment notice template and procedure for workplace AI deployment | AI Act Art. 26(7); labour law |
| 23 | Annex VII Assessment Criteria Checklist | NB review criteria mapped to QMS and technical documentation evidence; provider readiness pre-assessment | Annex VII; Art. 43-44 |
| 24 | Worked Example: Credit Scoring AI | End-to-end compliance walkthrough for Annex III Area 5 credit scoring (provider/deployer split scenario) | All Articles |

### New in v3.2.0 (Documents 25-28)

| # | Document | Purpose | Reference |
|---|---|---|---|
| 25 | Prohibited Practices Assessment | Structured decision framework for all 8 Article 5 prohibitions with exemption tests and clearance certificate (use with the Commission's Feb 2025 prohibited-practices guidelines) | Article 5, Recitals 28-45 |
| 26 | Article 9 Risk Management System | Standalone 8-step RMS: risk identification, estimation, evaluation, treatment, residual risk acceptance, testing, post-market integration | Article 9 |
| 27 | GPAI Systemic Risk Compliance Guide | Adversarial testing (red-teaming), systemic-risk mitigation, incident reporting, cybersecurity, EU supervision/enforcement, post-training measures (aligned to the GPAI Code of Practice Safety & Security chapter, Art. 55) | Articles 51, 55-56, 88-94, Annex XIII |
| 28 | Market Surveillance & Regulatory Response | Document retention schedule, competent authority response protocol, on-site inspection procedure, enforcement readiness checklist | Articles 74-99 (incl. 88-94 for GPAI) |

---

## Worked Examples

| File | Description |
|---|---|
| WORKED-EXAMPLE-HR-SCREENING-SYSTEM.md | Completed example: CV screening AI system (fictional HireRight GmbH / TalentFilter Pro). Shows application of all 10 core documents with realistic data. |
| 24-WORKED-EXAMPLE-CREDIT-SCORING-AI.md | Completed example: Credit scoring AI (fictional RetailBank NV / CreditScore-AI v2.3). Provider/deployer split, Annex III Area 5, GDPR/AI Act joint compliance. |

---

## GRC Engineering — Automation Scripts

| Script | Purpose | Automates |
|---|---|---|
| scripts/risk_classifier.py (v2.2) | CLI tool to classify AI systems by EU AI Act risk tier | Risk classification with Art. 6(3) exclusion logic and GPAI as a parallel regime; txt/json/csv output; CI exit-code gate on banned systems |
| scripts/sample_ai_inventory.csv | Sample 15-system AI inventory covering all risk tiers | Input for risk_classifier.py |

---

## How to Use This Toolkit

**Step 0 — Get oriented**
If you are new, read **docs/QUICKSTART.md** first.

**Step 1 — Screen for prohibited practices**
Before anything else, run every AI system through Doc 25 (Article 5 Prohibited Practices Assessment), alongside the Commission's Feb 2025 guidelines on prohibited practices. Any system that triggers a prohibition without a valid exemption must not proceed.

**Step 2 — Establish your position**
Complete the Master Compliance Scorecard (Doc 19) for an immediate gap analysis across all 118 requirements.

**Step 3 — Classify your AI systems**
Use 01-RISK-CLASSIFICATION-GUIDE.md or run `scripts/risk_classifier.py`

**Step 4 — High-Risk AI providers**
- Confirm your conformity assessment route (Annex VI internal control vs Annex VII Notified Body) in Doc 02 Section 0
- Complete 02-CONFORMITY-ASSESSMENT-CHECKLIST.md and 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md
- Build your Risk Management System using 26-RISK-MANAGEMENT-SYSTEM.md (Article 9 — mandatory, separate from QMS)
- Build your Quality Management System using 16-QUALITY-MANAGEMENT-SYSTEM.md (Article 17)
- If Notified Body is required: follow 20-NOTIFIED-BODY-ENGAGEMENT-GUIDE.md and use 23-ANNEX-VII-ASSESSMENT-CHECKLIST.md to prepare

**Step 5 — Deployers of High-Risk AI**
- Complete the FRIA (Doc 03) — required for public bodies, public-service deployers, and credit/insurance use cases
- Implement the Human Oversight Framework (Doc 07)
- Ensure staff are trained using 17-AI-LITERACY-COMPETENCY-FRAMEWORK.md
- Provide workers with pre-deployment notice using 22-WORKER-INFORMATION-NOTICE.md

**Step 6 — All AI systems**
- Check 06-TRANSPARENCY-OBLIGATIONS.md and 07-HUMAN-OVERSIGHT-FRAMEWORK.md
- Map GDPR obligations using 18-GDPR-AI-ACT-INTERSECTION.md
- If processing personal data under Art. 6(1)(f), complete a LIA per 21-LEGITIMATE-INTEREST-ASSESSMENT.md
- Register all systems in 05-AI-SYSTEM-REGISTER.md

**Step 7 — Establish ongoing processes**
- 08-INCIDENT-REPORTING-PROCEDURE.md and 09-POST-MARKET-MONITORING-PLAN.md
- Prepare for market surveillance with 28-MARKET-SURVEILLANCE-RESPONSE.md

**Step 8 — Supply chain**
- Non-EU providers: complete 13-AUTHORISED-REPRESENTATIVE.md before market placement
- Annex I product providers: follow 14-CE-MARKING-GUIDE.md and complete 12-EU-DECLARATION-OF-CONFORMITY.md
- Importers and Distributors: follow 15-IMPORTER-DISTRIBUTOR-CHECKLISTS.md

**Step 9 — GPAI/LLM model providers**
- Complete 11-GPAI-TECHNICAL-DOCUMENTATION.md and consider signing the GPAI Code of Practice (Transparency & Copyright chapters) to demonstrate Art. 53 compliance
- If systemic risk model: complete 27-GPAI-SYSTEMIC-RISK-COMPLIANCE.md and apply the Code's Safety & Security chapter (Art. 55)

---

## GRC Automation — risk_classifier.py v2.2

```bash
# Basic run with sample inventory
python scripts/risk_classifier.py

# Custom input file
python scripts/risk_classifier.py --input path/to/your/inventory.csv

# Machine-readable output for GRC platforms / CI pipelines
python scripts/risk_classifier.py --format json --output reports/risk.json

# Custom output report
python scripts/risk_classifier.py --input scripts/sample_ai_inventory.csv --output reports/q2_risk_report.txt
```

CSV columns for complete classification:

| Column | Values | Purpose |
|---|---|---|
| prohibited_practice | yes / no | Explicit Article 5 prohibited practice flag |
| exclusion_narrow_task | yes / no | Article 6(3)(a): narrow procedural task only |
| exclusion_human_result | yes / no | Article 6(3)(b): improves result of prior human activity |
| exclusion_no_individual | yes / no | Article 6(3)(c): detects patterns without influencing individuals |
| exclusion_preparatory | yes / no | Article 6(3)(d): preparatory task only |

> **Important:** Classifier output is a triage aid. Human compliance review is mandatory before acting on any classification. The `--format json|csv` outputs and a CI exit-code gate (exit 1 on any banned system) were added in v2.1; GPAI is handled as a parallel regime in v2.2.

---

## Key Definitions

| Term | Definition |
|---|---|
| Provider | Entity that develops or places an AI system on the market |
| Deployer | Entity that uses an AI system in a professional context |
| Importer | EU-established entity placing a non-EU provider's AI on the EU market |
| Distributor | Entity making AI available on market without modifying it |
| Operator | Collective term for provider, deployer, importer, distributor, authorised representative |
| GPAI Model | General-purpose AI model (e.g. foundation models / LLMs) — separate regime (Arts. 51-56) |
| Notified Body | Third-party conformity assessment body |
| FRIA | Fundamental Rights Impact Assessment (Art. 27) |
| LIA | Legitimate Interest Assessment (GDPR Art. 6(1)(f)) |
| RMS | Risk Management System (Article 9) |
| MSA | Market Surveillance Authority (national enforcement body) |
| AI Office | EU body supervising GPAI models and coordinating enforcement |

---

## Related Resources

**Primary EU sources**
- [EU AI Act Full Text (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [AI Act — European Commission overview & Single Information Platform](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office)
- [Guidelines on prohibited AI practices (Feb 2025)](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-prohibited-artificial-intelligence-ai-practices-defined-ai-act)
- [General-Purpose AI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)
- [AI Pact](https://digital-strategy.ec.europa.eu/en/policies/ai-pact)
- [NANDO Database — Notified Bodies](https://ec.europa.eu/growth/tools-databases/nando/)

**Standards**
- [ISO/IEC 42001:2023 AI Governance](https://www.iso.org/standard/81230.html)
- [ISO/IEC 23894:2023 AI Risk Management](https://www.iso.org/standard/77304.html)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

---

## Versioning and Changelog

See CHANGELOG.md for full version history, regulatory coverage tracking, and planned updates.

**Current version: v3.3.0 (June 2026)** — see CHANGELOG.md for what's new.

---

## Disclaimer

This toolkit is provided for informational and educational purposes. It does not constitute legal advice. The official Commission guidance referenced here is interpretive and the binding text remains Regulation (EU) 2024/1689. Always consult qualified legal counsel for compliance decisions, and verify dates and obligations against EUR-Lex.

Maintained by Ankit Uniyal | AI Governance and GRC Engineering

---

## Using the toolkit without Git

You don't need a developer setup to use these templates:

1. Click the green **Code** button at the top of this repository, then **Download ZIP**.
2. Unzip it. Every `NN-*.md` file is a plain-text template you can open in any text editor, or paste into Word / Google Docs to fill in.
3. Start with **docs/QUICKSTART.md**, then the **"Which Documents Apply to Me?"** routing table above, then follow the **"How to Use This Toolkit"** steps. The [docs/INDEX.md](docs/INDEX.md) coverage map shows every document at a glance.
4. The Python script under `scripts/` is **optional** — it automates risk classification, but the documents work fully on their own.

**Prefer editable forms?** The Markdown tables paste cleanly into Word and Excel. Copy a document's table into a spreadsheet to turn a checklist into trackable rows.
