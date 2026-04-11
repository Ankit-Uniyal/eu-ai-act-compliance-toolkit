# EU AI Act Compliance Toolkit

> **A practical, practitioner-built compliance toolkit for the EU Artificial Intelligence Act (Regulation (EU) 2024/1689)**

![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-2024%2F1689-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![GRC Engineering](https://img.shields.io/badge/GRC-Engineering-orange?style=flat-square)

---

## Overview

The **EU AI Act** (entered into force 1 August 2024) is the world's first comprehensive legal framework for artificial intelligence. It applies a **risk-based approach**, imposing obligations proportional to the potential harm an AI system can cause — to providers, deployers, importers, and distributors operating in or supplying to the EU market.

This toolkit translates the Act's 113 Articles and 13 Annexes into **actionable templates, checklists, and automation scripts** that GRC professionals, AI governance practitioners, and compliance teams can use immediately.

---

## Compliance Timeline

| Milestone | Date |
|---|---|
| EU AI Act enters into force | **1 August 2024** |
| Prohibited AI systems banned | **2 February 2025** |
| GPAI model rules apply | **2 August 2025** |
| High-risk AI systems (Annex I) obligations | **2 August 2026** |
| All remaining provisions fully applicable | **2 August 2027** |

---

## Risk Tier Framework

The EU AI Act classifies AI systems into four risk tiers:

```
┌─────────────────────────────────────────────────────────────┐
│  UNACCEPTABLE RISK  │  Prohibited — banned outright         │
│  (Article 5)        │  e.g. social scoring, subliminal AI   │
├─────────────────────────────────────────────────────────────┤
│  HIGH RISK          │  Strict obligations — conformity      │
│  (Articles 6-51,    │  assessment, registration, oversight  │
│   Annexes I & III)  │  e.g. CV screening, credit scoring    │
├─────────────────────────────────────────────────────────────┤
│  LIMITED RISK       │  Transparency obligations only        │
│  (Articles 50, 52)  │  e.g. chatbots, deepfakes             │
├─────────────────────────────────────────────────────────────┤
│  MINIMAL RISK       │  Voluntary codes of conduct           │
│                     │  e.g. spam filters, AI in games       │
└─────────────────────────────────────────────────────────────┘
```

---

## Toolkit Structure

| # | Document | Purpose | EU AI Act Reference |
|---|----------|---------|---------------------|
| 01 | [Risk Classification Guide](01-RISK-CLASSIFICATION-GUIDE.md) | Classify your AI system by risk tier | Articles 5, 6, 50 + Annexes I, III |
| 02 | [Conformity Assessment Checklist](02-CONFORMITY-ASSESSMENT-CHECKLIST.md) | Pre-market conformity checklist for high-risk AI | Articles 43–48 |
| 03 | [Fundamental Rights Impact Assessment](03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md) | FRIA template for deployers of high-risk AI | Article 27 |
| 04 | [Technical Documentation Template](04-TECHNICAL-DOCUMENTATION-TEMPLATE.md) | Annex IV-compliant technical documentation | Article 11 + Annex IV |
| 05 | [AI System Register](05-AI-SYSTEM-REGISTER.md) | Inventory of AI systems with risk classification | Articles 49, 71 |
| 06 | [Transparency Obligations Checklist](06-TRANSPARENCY-OBLIGATIONS.md) | Obligations for limited-risk and GPAI systems | Articles 50, 53 |
| 07 | [Human Oversight Framework](07-HUMAN-OVERSIGHT-FRAMEWORK.md) | Design and operational human oversight controls | Article 14 |
| 08 | [Incident Reporting Procedure](08-INCIDENT-REPORTING-PROCEDURE.md) | Serious incident reporting to market surveillance | Article 73 |
| 09 | [Post-Market Monitoring Plan](09-POST-MARKET-MONITORING-PLAN.md) | Ongoing monitoring and logging obligations | Article 72 |
| 10 | [Provider & Deployer Responsibilities](10-PROVIDER-DEPLOYER-RESPONSIBILITIES.md) | Role-based obligation matrix | Articles 16, 26 |

---

## GRC Engineering — Automation Scripts

| Script | Purpose | Automates |
|--------|---------|-----------|
| [scripts/risk_classifier.py](scripts/risk_classifier.py) | CLI tool to classify AI systems by EU AI Act risk tier | Risk classification workflow |
| [scripts/sample_ai_inventory.csv](scripts/sample_ai_inventory.csv) | Sample AI system inventory | Input for risk_classifier.py |

---

## Who This Is For

- **GRC professionals** building AI compliance programmes
- **AI governance practitioners** mapping systems to regulatory requirements
- **Legal & compliance teams** preparing for EU AI Act obligations
- **AI product teams** understanding what their systems must do before deployment
- **Auditors** assessing AI systems against the EU AI Act framework

---

## How to Use This Toolkit

1. **Classify your AI systems** using [01-RISK-CLASSIFICATION-GUIDE.md](01-RISK-CLASSIFICATION-GUIDE.md) or run `scripts/risk_classifier.py`
2. **If High Risk**: complete [02-CONFORMITY-ASSESSMENT-CHECKLIST.md](02-CONFORMITY-ASSESSMENT-CHECKLIST.md) and [04-TECHNICAL-DOCUMENTATION-TEMPLATE.md](04-TECHNICAL-DOCUMENTATION-TEMPLATE.md)
3. **If deploying High Risk AI**: complete the [FRIA](03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md)
4. **For all AI systems**: check [06-TRANSPARENCY-OBLIGATIONS.md](06-TRANSPARENCY-OBLIGATIONS.md) and [07-HUMAN-OVERSIGHT-FRAMEWORK.md](07-HUMAN-OVERSIGHT-FRAMEWORK.md)
5. **Register all systems** in [05-AI-SYSTEM-REGISTER.md](05-AI-SYSTEM-REGISTER.md)
6. **Establish ongoing processes**: [08-INCIDENT-REPORTING-PROCEDURE.md](08-INCIDENT-REPORTING-PROCEDURE.md) and [09-POST-MARKET-MONITORING-PLAN.md](09-POST-MARKET-MONITORING-PLAN.md)

---

## Key Definitions

| Term | Definition |
|------|-----------|
| **Provider** | Entity that develops/places an AI system on the market |
| **Deployer** | Entity that uses an AI system in a professional context |
| **Operator** | Collective term for providers and deployers |
| **GPAI Model** | General-purpose AI model (e.g. foundation models / LLMs) |
| **Notified Body** | Third-party conformity assessment body |
| **FRIA** | Fundamental Rights Impact Assessment |

---

## Related Resources

- [EU AI Act Full Text (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)
- [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office)
- [High-Risk AI Systems List (Annex III)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#anx_III)
- [ISO/IEC 42001:2023 AI Governance Toolkit](https://github.com/Ankit-Uniyal/iso-42001-ai-governance-toolkit) *(companion toolkit)*

---

## Disclaimer

This toolkit is provided for informational and educational purposes. It does not constitute legal advice. Always consult qualified legal counsel for compliance decisions.

---

*Maintained by [Ankit Uniyal](https://github.com/Ankit-Uniyal) | AI Governance & GRC Engineering*
