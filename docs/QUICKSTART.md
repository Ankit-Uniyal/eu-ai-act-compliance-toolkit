# EU AI Act in 10 Minutes — Quickstart

**New to the EU AI Act? Read this first.** It explains, in plain language, what the law is, who it applies to, the four risk tiers, the real deadlines, and the first three things you should do. When you are ready for detail, follow the links into the full toolkit.

> This is a plain-language orientation, not legal advice. See each linked document and consult qualified counsel for binding decisions.

---

## 1. What is the EU AI Act?

The EU AI Act (Regulation (EU) 2024/1689) is the first comprehensive law governing artificial intelligence. It takes a **risk-based** approach: the more risk an AI system poses to people's health, safety, or fundamental rights, the more obligations apply. It applies to anyone who **provides** (builds/places on the market) or **deploys** (uses professionally) AI in the EU — including organisations outside the EU whose AI is used in the EU.

## 2. Which "hat" are you wearing?

Your obligations depend on your role. You can wear more than one hat.

- **Provider** — you develop an AI system (or have one developed) and put it on the market under your name. Most obligations fall here.
- **Deployer** — you use an AI system in a professional context. Fewer obligations, but real ones (human oversight, transparency to affected people, sometimes a FRIA).
- **Importer / Distributor** — you bring a non-EU provider's AI into the EU, or make it available, without changing it.
- **GPAI model provider** — you build a general-purpose AI model (e.g. a foundation model / LLM). This is a **separate regime** with its own rules.

## 3. The four risk tiers (plus the GPAI regime)

| Tier | What it means | Examples | What you must do |
|---|---|---|---|
| **Unacceptable** | Banned outright | Social scoring, manipulative AI, untargeted face scraping, most real-time public biometric ID | Do not build or use it |
| **High risk** | Allowed, but heavily regulated | CV screening, credit scoring, AI in medical devices, exam scoring | Full compliance programme (see step C below) |
| **Limited risk** | Transparency only | Chatbots, deepfakes, AI-generated content | Tell people they're dealing with AI / AI-generated content |
| **Minimal risk** | No mandatory rules | Spam filters, game AI | Optional good practice |
| **GPAI models** (separate) | Parallel regime (Arts. 51–56) | Foundation models, LLMs | Model documentation, copyright policy, training-data summary; extra duties if "systemic risk" |

**Key idea:** transparency (limited risk) is an **overlay** — a high-risk system can also have transparency duties, and a GPAI model can also be inside a high-risk system. Tiers are not mutually exclusive.

## 4. The deadlines that matter

| Date | What becomes enforceable |
|---|---|
| 2 February 2025 | Prohibited practices banned; AI-literacy duty starts |
| 2 August 2025 | GPAI model rules + governance/penalties |
| 2 August 2026 | Most high-risk (Annex III) obligations |
| 2 August 2027 | High-risk AI embedded in regulated products (Annex I); legacy GPAI models |

*(Dates can be adjusted by later EU acts — verify against EUR-Lex.)*

## 5. Do these three things first

**A. Screen for the bans.** Run every AI system through the **[Prohibited Practices Assessment (Doc 25)](../25-PROHIBITED-PRACTICES-ASSESSMENT.md)**. If a system is prohibited, stop — it cannot go to market.

**B. Classify the system.** Use the **[Risk Classification Guide (Doc 01)](../01-RISK-CLASSIFICATION-GUIDE.md)** (or run `python scripts/risk_classifier.py`) to find its tier. This tells you which obligations apply.

**C. If it is high risk, build the core compliance set.** In order: a **[Risk Management System (Doc 26)](../26-RISK-MANAGEMENT-SYSTEM.md)**, **[Technical Documentation (Doc 04)](../04-TECHNICAL-DOCUMENTATION-TEMPLATE.md)**, a **[Conformity Assessment (Doc 02)](../02-CONFORMITY-ASSESSMENT-CHECKLIST.md)**, a **[Quality Management System (Doc 16)](../16-QUALITY-MANAGEMENT-SYSTEM.md)**, **[Human Oversight (Doc 07)](../07-HUMAN-OVERSIGHT-FRAMEWORK.md)**, and EU database registration. Deployers in the public sector or in credit/insurance also need a **[FRIA (Doc 03)](../03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md)**.

## 6. If you process personal data

GDPR applies **at the same time** as the AI Act. They are separate laws with separate regulators (Data Protection Authorities for GDPR; Market Surveillance Authorities for the AI Act). The **[GDPR × AI Act Intersection Map (Doc 18)](../18-GDPR-AI-ACT-INTERSECTION.md)** shows where one piece of work can satisfy both, and where you need two separate steps.

> **One common trap:** incident-reporting clocks are different. A serious incident under the AI Act has tiered deadlines (immediately, and at most **15 / 2 / 10 days** depending on severity — Art. 73). A personal-data breach under GDPR has a separate **72-hour** clock to the DPA (Art. 33). Don't confuse the two.

## 7. The penalties (why this matters)

- Prohibited practices: up to **€35 million or 7%** of global annual turnover.
- Most other high-risk breaches: up to **€15 million or 3%**.
- Supplying incorrect information: up to **€7.5 million or 1.5%**.
- GPAI-model providers: up to **€15 million or 3%**, enforced by the Commission.

## 8. Where to go next

- Find your role in the **["Which Documents Apply to Me?" table](../README.md)** in the README.
- See every document at a glance in **[docs/INDEX.md](INDEX.md)**.
- Track your overall position with the **[Master Compliance Scorecard (Doc 19)](../19-MASTER-COMPLIANCE-SCORECARD.md)**.
- See a fully worked example: **[HR screening](../WORKED-EXAMPLE-HR-SCREENING-SYSTEM.md)** or **[credit scoring](../24-WORKED-EXAMPLE-CREDIT-SCORING-AI.md)**.

---

*Part of the EU AI Act Compliance Toolkit. This document does not constitute legal advice.*
