# 01 — EU AI Act Risk Classification Guide

**EU AI Act Reference:** Articles 5, 6, 50 | Annexes I, II, III
**Applies to:** Providers, Deployers, Importers, Distributors
**Last Updated:** April 2026

---

## Purpose

This guide helps organisations classify their AI systems under the EU AI Act four-tier risk framework. Classification determines which obligations apply and when compliance must be achieved.

---

## Part 0 — FRIA Scoping: Do You Need a Fundamental Rights Impact Assessment?

Before proceeding with risk classification, deployers should determine whether Article 27 mandates a Fundamental Rights Impact Assessment (FRIA).

### FRIA Scoping Decision Table

| Question | Answer | FRIA Obligation |
|---|---|---|
| Is your organisation a **body governed by public law** (Art. 4(8) of Directive 2014/24/EU)? | YES | **MANDATORY** — FRIA required before deploying any High-Risk AI system |
| Is your organisation a **private body providing public-interest services** in banking, insurance, healthcare, or education? | YES | **MANDATORY** — FRIA required before deploying any High-Risk AI system |
| Is your organisation a private body NOT providing public-interest services? | YES | **VOLUNTARY** — recommended for governance best practice, not legally required |
| Does the AI system fall outside the High-Risk tier after completing Steps 1-3? | YES | **NOT REQUIRED** — FRIA applies only to High-Risk AI systems |

> **Key Rule (Article 27(1)):** The FRIA obligation applies to the **deployer**, not the provider. Even if the system is provided by a third party, the deploying organisation bears the FRIA obligation if it meets the criteria above.

### FRIA Scoping Outcome

Complete Steps 1-3 below first. If the system is classified High-Risk **AND** the deployer meets the public/public-service body criteria, proceed to **03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md** before deployment.

---

## Step 1: Is It an AI System?

Under Article 3(1), an AI system is a machine-based system designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers from the input it receives how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments.

| Question | If YES | If NO |
|---|---|---|
| Does it infer outputs from inputs using ML, logic, or statistical approaches? | Continue to Step 2 | Not in scope |
| Is it rule-based only (no learning/inference)? | Not an AI system | — |

---

## Step 2: Is It Prohibited? (Unacceptable Risk)

Article 5 prohibits the following AI practices. If your system does ANY of the following, it is BANNED in the EU:

| # | Prohibited Practice | Description |
|---|---|---|
| 1 | Subliminal manipulation | Techniques beyond conscious awareness to distort behaviour harmfully |
| 2 | Exploitation of vulnerabilities | Targeting vulnerable groups (age, disability, social/economic situation) |
| 3 | Social scoring by public authorities | Evaluating or classifying persons based on social behaviour or personal characteristics |
| 4 | Real-time remote biometric ID in public (law enforcement) | Except for specific, authorised exemptions |
| 5 | Biometric categorisation inferring sensitive attributes | Race, political opinions, trade union membership, religion, sexual orientation |
| 6 | Emotion recognition in workplace/education | With limited exceptions |
| 7 | Untargeted facial scraping for databases | Building face recognition databases from internet/CCTV |
| 8 | AI to predict criminal offences based on profiling | Predictive policing based on personality traits |

**If prohibited: STOP. System cannot be placed on EU market.**

---

## Step 3: Is It High Risk?

High-risk AI systems are defined under Article 6 and fall into two categories:

### Category A — AI as Safety Component (Article 6(1))

AI systems that are a safety component of, or are themselves, products covered by EU harmonisation legislation listed in Annex I (e.g. machinery, medical devices, aviation, vehicles).

### Category B — Standalone High-Risk Use Cases (Article 6(2) + Annex III)

| Annex III Area | Examples |
|---|---|
| 1. Biometrics | Remote biometric identification, emotion recognition (non-prohibited) |
| 2. Critical infrastructure | AI in water, gas, heating, electricity, traffic management |
| 3. Education & vocational training | Systems determining access, evaluating students |
| 4. Employment & workers management | CV screening, promotion decisions, task allocation, monitoring |
| 5. Essential private/public services | Credit scoring, insurance risk assessment, benefit eligibility |
| 6. Law enforcement | Polygraphs, risk assessment, evidence reliability |
| 7. Migration, asylum, border control | Risk assessment, document examination, applications |
| 8. Administration of justice | Research/interpretation of facts/law, dispute resolution |

---

### Article 6(3) Exclusion Decision Tree

Even if a system falls within an Annex III category, it is **NOT high-risk** if it satisfies one of the four exclusion conditions under Article 6(3). Apply this decision tree sequentially:

**START: Does the system appear in Annex III?**

If YES, work through the four questions:

**Q1:** Does it ONLY perform a **narrow procedural task** (e.g., routing a form, converting a format, scheduling)?
- YES => NOT High-Risk — document exclusion basis and proceed to Step 4
- NO => proceed to Q2

**Q2:** Does it ONLY **improve the result of a previously completed human activity** (post-hoc support, not primary decision driver)?
- YES => NOT High-Risk — document exclusion basis and proceed to Step 4
- NO => proceed to Q3

**Q3:** Does it ONLY **detect decision-making patterns** (analytics/reporting) with NO influence on any individual-level decision?
- YES => NOT High-Risk — document exclusion basis and proceed to Step 4
- NO => proceed to Q4

**Q4:** Does it ONLY perform a **preparatory task** to a human assessment (data gathering, pre-processing) with NO direct output influencing an individual?
- YES => NOT High-Risk — document exclusion basis and proceed to Step 4
- NO => **HIGH RISK confirmed** — full Chapter III Section 2 obligations apply

> **Important (Recital 53):** The exclusion must be assessed conservatively. If in doubt, treat the system as High-Risk and document reasoning. Seek legal opinion before relying on an exclusion in a regulated sector.

#### Article 6(3) Exclusion Checklist

| Criterion | Assessment | Evidence / Justification |
|---|---|---|
| Narrow procedural task only? | Yes / No | |
| Improves previously completed human activity only? | Yes / No | |
| Detects patterns only, no individual influence? | Yes / No | |
| Preparatory task only, no direct individual output? | Yes / No | |
| **Exclusion conclusion** | Applies / Does Not Apply | |
| Exclusion documented and approved by | Name / Date | |

---

## Step 4: Is It Limited Risk?

Article 50 requires transparency when:

| System Type | Obligation |
|---|---|
| Chatbots & conversational AI | Must disclose it is an AI system |
| Deepfake content | Must label content as artificially generated |
| AI-generated text on matters of public interest | Must be marked as AI-generated |
| Emotion recognition / biometric categorisation | Must inform individuals |

---

## Step 5: Minimal Risk

All AI systems not falling into the above categories are **minimal risk**. No mandatory obligations apply, but operators are encouraged to follow voluntary codes of conduct.

Examples: AI in video games, spam filters, AI-assisted grammar checkers.

---

## Risk Classification Decision Tree

```
START
 |
 +-- Is it an AI system (Article 3)?
      +-- NO  --> Out of scope
      +-- YES --> Is it prohibited (Article 5)?
                  +-- YES --> UNACCEPTABLE RISK
                  +-- NO  --> Safety component of Annex I (Art. 6(1))?
                              +-- YES --> HIGH RISK
                              +-- NO  --> Listed in Annex III (Art. 6(2))?
                                          +-- YES --> Art. 6(3) exclusion?
                                          |            +-- NO  --> HIGH RISK
                                          |            +-- YES --> LIMITED/MINIMAL
                                          +-- NO  --> Art. 50 transparency?
                                                      +-- YES --> LIMITED RISK
                                                      +-- NO  --> MINIMAL RISK
```

---

## Risk Classification Register Entry

Complete this for each AI system:

| Field | Entry |
|---|---|
| System Name | |
| System ID | |
| Version / Build | |
| Provider / Owner | |
| Primary Use Case | |
| Intended Users | |
| Geography of Deployment | |
| Is it an AI system per Article 3? | Yes / No |
| Prohibited under Article 5? | Yes / No |
| High-Risk — Annex I product? | Yes / No |
| High-Risk — Annex III use case? | Yes / No (specify area) |
| Article 6(3) exclusion claimed? | Yes / No |
| Exclusion basis (if claimed) | Procedural / Post-hoc / Pattern / Preparatory |
| Exclusion documented and approved? | Yes / No — Reference: |
| FRIA required? | Yes / No (see Part 0 above) |
| FRIA Status | Not started / In progress / Completed |
| FINAL RISK CLASSIFICATION | Unacceptable / High / Limited / Minimal |
| Classification Date | |
| Classified By | |
| Next Review Date | |

---

## Compliance Obligations by Tier

| Tier | Key Obligations |
|---|---|
| Unacceptable | System must not be placed on market or put into service |
| High Risk | Risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy, conformity assessment, EU registration |
| Limited Risk | Transparency disclosures to users; deepfake labelling |
| Minimal Risk | No mandatory obligations; voluntary codes of conduct encouraged |

---

*Part of the EU AI Act Compliance Toolkit*
*This document does not constitute legal advice. Seek qualified legal counsel for binding compliance determinations.*
