# 01 — EU AI Act Risk Classification Guide

**EU AI Act Reference:** Articles 5, 6, 50 | Annexes I, II, III
**Applies to:** Providers, Deployers, Importers, Distributors
**Last Updated:** April 2026

---

## Purpose

This guide helps organisations classify their AI systems under the EU AI Act four-tier risk framework. Classification determines which obligations apply and when compliance must be achieved.

> **New here? Read [docs/QUICKSTART.md](docs/QUICKSTART.md) first** for a plain-language, 10-minute overview of the four tiers, the real deadlines, and the three things to do first.

---

## Part 0 — FRIA Scoping: Do You Need a Fundamental Rights Impact Assessment?

Before proceeding with risk classification, deployers should determine whether Article 27 mandates a Fundamental Rights Impact Assessment (FRIA).

### FRIA Scoping Decision Table

| Question | Answer | FRIA Obligation |
|---|---|---|
| Is your organisation a **body governed by public law**, or a private entity providing **public services**? | YES | **MANDATORY** — FRIA required before deploying a High-Risk AI system (Art. 27(1)) |
| Is the High-Risk system used for **creditworthiness/credit scoring** (except fraud detection) or for **risk assessment and pricing in life and health insurance**? | YES | **MANDATORY** — FRIA required regardless of public/private status (Art. 27(1), second subparagraph) |
| Is your organisation a private body NOT providing public services and NOT in the two use-cases above? | YES | **VOLUNTARY** — recommended for governance best practice, not legally required |
| Does the AI system fall outside the High-Risk tier after completing Steps 1-3? | YES | **NOT REQUIRED** — FRIA applies only to High-Risk AI systems |

> **Key Rule (Article 27(1)):** The FRIA obligation applies to the **deployer**, not the provider. Even if the system is provided by a third party, the deploying organisation bears the FRIA obligation if it meets the criteria above. Where a DPIA already covers some elements, the FRIA may complement it (Art. 27(4)).

### FRIA Scoping Outcome

Complete Steps 1-3 below first. If the system is classified High-Risk **AND** the deployer meets the criteria above, proceed to **03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md** before deployment.

---

## Step 1: Is It an AI System?

Under Article 3(1), an AI system is a machine-based system designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers from the input it receives how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments.

| Question | If YES | If NO |
|---|---|---|
| Does it infer outputs from inputs using ML, logic, or statistical approaches? | Continue to Step 2 | Not in scope |
| Is it rule-based only (no learning/inference)? | Not an AI system | — |

---

## Step 2: Is It Prohibited? (Unacceptable Risk)

Article 5(1) prohibits the following AI practices. If your system does ANY of the following, it is BANNED in the EU. (Sub-letters below match the enacted Regulation (EU) 2024/1689 — see Doc 25 for the full assessment.)

| # | Prohibited Practice | Article | Description |
|---|---|---|---|
| 1 | Subliminal / manipulative / deceptive techniques | 5(1)(a) | Techniques that materially distort behaviour by impairing informed decision-making, causing significant harm |
| 2 | Exploitation of vulnerabilities | 5(1)(b) | Exploiting age, disability, or social/economic situation to distort behaviour harmfully |
| 3 | Social scoring | 5(1)(c) | Evaluating/classifying persons over time on social behaviour or personal traits, leading to unjustified detrimental treatment (applies to public **and** private actors) |
| 4 | Predictive policing based on profiling | 5(1)(d) | Assessing risk of committing a criminal offence based **solely** on profiling or personality traits |
| 5 | Untargeted facial scraping | 5(1)(e) | Building/expanding face recognition databases by untargeted scraping from the internet or CCTV |
| 6 | Emotion recognition in workplace/education | 5(1)(f) | Inferring emotions in workplaces or education institutions (medical/safety exceptions) |
| 7 | Biometric categorisation by protected characteristics | 5(1)(g) | Inferring race, political opinions, trade union membership, religion, sex life, or sexual orientation from biometric data |
| 8 | Real-time remote biometric ID in public (law enforcement) | 5(1)(h) | Subject to narrow Art. 5(2)–(7) exemptions |

**If prohibited: STOP. System cannot be placed on EU market.** Use **Doc 25** for the full prohibited-practices assessment and clearance certificate.

---

## Step 3: Is It High Risk?

High-risk AI systems are defined under Article 6 and fall into two categories:

### Category A — AI as Safety Component (Article 6(1))

AI systems that are themselves products, or are a safety component of products, covered by the EU harmonisation legislation listed in **Annex I**, and that are required to undergo a third-party conformity assessment under that legislation (e.g. machinery, medical devices, in-vitro diagnostics, aviation, vehicles, toys, radio equipment).

### Category B — Standalone High-Risk Use Cases (Article 6(2) + Annex III)

| Annex III Area | Examples |
|---|---|
| 1. Biometrics | Remote biometric identification; biometric categorisation; emotion recognition (non-prohibited) |
| 2. Critical infrastructure | Safety components in water, gas, heating, electricity, road traffic management |
| 3. Education & vocational training | Systems determining access/admission, evaluating learning outcomes, monitoring exams |
| 4. Employment & workers management | CV screening, promotion/termination decisions, task allocation, monitoring |
| 5. Essential private/public services | Credit scoring, benefit eligibility, life/health insurance pricing, emergency dispatch |
| 6. Law enforcement | Risk assessment of offending/re-offending, evidence reliability, profiling |
| 7. Migration, asylum, border control | Risk assessment, document verification, examination of applications |
| 8. Administration of justice | Assisting judicial authorities in researching/interpreting facts and law |

---

### Article 6(3) Exclusion Decision Tree

Even if a system falls within an Annex III category, it is **NOT high-risk** if it does not pose a significant risk of harm to health, safety, or fundamental rights — including by not materially influencing the outcome of decision-making — and it meets at least one of the four conditions under Article 6(3). Apply this decision tree sequentially:

**START: Does the system appear in Annex III?**

If YES, work through the four questions:

**Q1:** Does it ONLY perform a **narrow procedural task** (e.g., routing a form, converting a format, scheduling)?
- YES => may be excluded — go to the override check below
- NO => proceed to Q2

**Q2:** Does it ONLY **improve the result of a previously completed human activity**?
- YES => may be excluded — go to the override check below
- NO => proceed to Q3

**Q3:** Does it ONLY **detect decision-making patterns or deviations from prior patterns** and is NOT meant to replace or influence the previously completed human assessment without proper human review?
- YES => may be excluded — go to the override check below
- NO => proceed to Q4

**Q4:** Does it ONLY perform a **preparatory task** to an assessment relevant to an Annex III use case?
- YES => may be excluded — go to the override check below
- NO => **HIGH RISK confirmed** — full Chapter III Section 2 obligations apply

**Override check (Article 6(3), final subparagraph):** An Annex III system is **ALWAYS high-risk** if it performs **profiling of natural persons**, regardless of the four conditions above.

> **Important (Recital 53):** The exclusion must be assessed conservatively. If in doubt, treat the system as High-Risk and document reasoning. Seek legal opinion before relying on an exclusion in a regulated sector.

> **Registration still required (Article 49(2)):** A provider that concludes its Annex III system is **NOT** high-risk under Art. 6(3) must still **register the system (and the exclusion grounds) in the EU database** before placing it on the market or putting it into service. Excluded systems must also still be checked against the **Article 50 transparency** obligations in Step 4.

#### Article 6(3) Exclusion Checklist

| Criterion | Assessment | Evidence / Justification |
|---|---|---|
| Narrow procedural task only? | Yes / No | |
| Improves previously completed human activity only? | Yes / No | |
| Detects patterns/deviations only, with proper human review? | Yes / No | |
| Preparatory task only? | Yes / No | |
| Does the system perform profiling of natural persons? (if Yes → always High-Risk) | Yes / No | |
| **Exclusion conclusion** | Applies / Does Not Apply | |
| Art. 49(2) database registration of exclusion completed | Yes / No — Reference: | |
| Exclusion documented and approved by | Name / Date | |

---

## Step 4: Is It Limited Risk? (Transparency — Article 50)

Article 50 imposes transparency obligations (these apply **in addition to** any tier above — a high-risk or excluded system can also carry Art. 50 duties):

| System Type | Obligation | Reference |
|---|---|---|
| Chatbots & conversational AI | Inform the natural person they are interacting with an AI system | Art. 50(1) |
| AI-generated/manipulated audio, image, video, text | Mark outputs as artificially generated in a machine-readable format | Art. 50(2) |
| Emotion recognition / biometric categorisation | Inform the natural persons exposed to it | Art. 50(3) |
| Deep fakes | Disclose that content has been artificially generated or manipulated | Art. 50(4) |
| AI-generated text published to inform the public on matters of public interest | Disclose that the text is artificially generated | Art. 50(4) |

---

## Step 5: Minimal Risk

All AI systems not falling into the above categories are **minimal risk**. No mandatory obligations apply, but operators are encouraged to follow voluntary codes of conduct (Art. 95).

Examples: AI in video games, spam filters, AI-assisted grammar checkers.

---

## Risk Classification Decision Tree

```
START
|
+-- Is it an AI system (Article 3)?
+-- NO --> Out of scope
+-- YES --> Is it prohibited (Article 5)?
+-- YES --> UNACCEPTABLE RISK (stop)
+-- NO --> Safety component / product under Annex I requiring 3rd-party CA (Art. 6(1))?
+-- YES --> HIGH RISK (+ check Art. 50)
+-- NO --> Listed in Annex III (Art. 6(2))?
+-- YES --> Art. 6(3) exclusion AND no profiling?
| +-- NO --> HIGH RISK (+ check Art. 50)
| +-- YES --> NOT High-Risk: register exclusion (Art. 49(2)) --> check Art. 50
+-- NO --> Art. 50 transparency applies?
+-- YES --> LIMITED RISK
+-- NO --> MINIMAL RISK
```

> Article 50 transparency is an **overlay**, not a separate exclusive tier: always run the Art. 50 check even for High-Risk and 6(3)-excluded systems.

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
| Prohibited under Article 5? | Yes / No (specify sub-letter) |
| High-Risk — Annex I product? | Yes / No |
| High-Risk — Annex III use case? | Yes / No (specify area) |
| Article 6(3) exclusion claimed? | Yes / No |
| Exclusion basis (if claimed) | Procedural / Post-hoc / Pattern / Preparatory |
| Profiling of natural persons? (if Yes → always High-Risk) | Yes / No |
| Art. 49(2) exclusion registered in EU database? | Yes / No — Reference: |
| Article 50 transparency obligations apply? | Yes / No (specify) |
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
| High Risk | Risk management (Art. 9), data governance (Art. 10), technical documentation (Art. 11), logging (Art. 12), transparency to deployers (Art. 13), human oversight (Art. 14), accuracy/robustness/cybersecurity (Art. 15), QMS (Art. 17), conformity assessment (Arts. 43-48), EU registration (Art. 49), + Art. 50 where applicable |
| Limited Risk | Article 50 transparency disclosures |
| Minimal Risk | No mandatory obligations; voluntary codes of conduct encouraged (Art. 95) |

---

*Part of the EU AI Act Compliance Toolkit*
*This document does not constitute legal advice. Seek qualified legal counsel for binding compliance determinations.*
