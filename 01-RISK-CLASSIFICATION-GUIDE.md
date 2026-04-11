# 01 — EU AI Act Risk Classification Guide

**EU AI Act Reference:** Articles 5, 6, 50 | Annexes I, II, III  
**Applies to:** Providers, Deployers, Importers, Distributors  
**Last Updated:** April 2026

---

## Purpose

This guide helps organisations classify their AI systems under the EU AI Act's four-tier risk framework. Classification determines which obligations apply and when compliance must be achieved.

---

## Step 1: Is It an AI System?

Under Article 3(1), an AI system is:
> *"A machine-based system designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments."*

| Question | If YES | If NO |
|----------|--------|-------|
| Does it infer outputs from inputs using ML, logic, or statistical approaches? | Continue to Step 2 | Not in scope |
| Is it rule-based only (no learning/inference)? | Not an AI system | — |

---

## Step 2: Is It Prohibited? (Unacceptable Risk)

**Article 5** prohibits the following AI practices. If your system does ANY of the following, it is **BANNED** in the EU:

| # | Prohibited Practice | Description |
|---|---------------------|-------------|
| 1 | Subliminal manipulation | Techniques beyond conscious awareness to distort behaviour harmfully |
| 2 | Exploitation of vulnerabilities | Targeting vulnerable groups (age, disability, social/economic situation) |
| 3 | Social scoring by public authorities | Evaluating or classifying persons based on social behaviour or personal characteristics |
| 4 | Real-time remote biometric ID in public (law enforcement) | Except for specific, authorised exemptions |
| 5 | Biometric categorisation inferring sensitive attributes | Race, political opinions, trade union membership, religion, sexual orientation |
| 6 | Emotion recognition in workplace/education | (with limited exceptions) |
| 7 | Untargeted facial scraping for databases | Building face recognition databases from internet/CCTV |
| 8 | AI to predict criminal offences based on profiling | Predictive policing based on personality traits |

**➜ If prohibited: STOP. System cannot be placed on EU market.**

---

## Step 3: Is It High Risk?

High-risk AI systems are defined under **Article 6** and fall into two categories:

### Category A — AI as Safety Component (Article 6(1))
AI systems that are a safety component of, or are themselves, products covered by EU harmonisation legislation listed in **Annex I** (e.g. machinery, medical devices, aviation, vehicles).

### Category B — Standalone High-Risk Use Cases (Article 6(2) + Annex III)

| Annex III Area | Examples |
|----------------|---------|
| **1. Biometrics** | Remote biometric identification, emotion recognition (non-prohibited) |
| **2. Critical infrastructure** | AI in water, gas, heating, electricity, traffic management |
| **3. Education & vocational training** | Systems determining access, evaluating students |
| **4. Employment & workers management** | CV screening, promotion decisions, task allocation, monitoring |
| **5. Essential private/public services** | Credit scoring, insurance risk assessment, benefit eligibility |
| **6. Law enforcement** | Polygraphs, risk assessment, evidence reliability |
| **7. Migration, asylum, border control** | Risk assessment, document examination, applications |
| **8. Administration of justice** | Research/interpretation of facts/law, dispute resolution |

**Exclusion (Article 6(3)):** A system in Annex III is NOT high-risk if:
- It performs a narrow procedural task
- It improves the result of a previously completed human activity
- It detects decision-making patterns without individual influence
- It performs a preparatory task to a human assessment

---

## Step 4: Is It Limited Risk?

**Article 50** requires transparency when:

| System Type | Obligation |
|-------------|-----------|
| Chatbots & conversational AI | Must disclose it is an AI system |
| Deepfake content | Must label content as artificially generated |
| AI-generated text on matters of public interest | Must be marked as AI-generated |
| Emotion recognition / biometric categorisation | Must inform individuals |

---

## Step 5: Minimal Risk

All AI systems not falling into the above categories are **minimal risk**. No mandatory obligations apply, but operators are encouraged to follow voluntary codes of conduct.

**Examples:** AI in video games, spam filters, AI-assisted grammar checkers.

---

## Risk Classification Decision Tree

```
START
  │
  ▼
Is it an AI system (Article 3)?
  │
  ├── NO → Out of scope
  │
  └── YES
        │
        ▼
      Is it prohibited (Article 5)?
        │
        ├── YES → ⛔ UNACCEPTABLE RISK — Banned
        │
        └── NO
              │
              ▼
            Safety component of Annex I product (Article 6(1))?
              │
              ├── YES → 🔴 HIGH RISK — Full obligations apply
              │
              └── NO
                    │
                    ▼
                  Listed in Annex III use cases (Article 6(2))?
                    │
                    ├── YES → Does exclusion apply (Article 6(3))?
                    │           ├── NO  → 🔴 HIGH RISK
                    │           └── YES → 🟡 LIMITED or ⚪ MINIMAL RISK
                    │
                    └── NO
                          │
                          ▼
                        Transparency obligation (Article 50)?
                          │
                          ├── YES → 🟡 LIMITED RISK
                          │
                          └── NO → ⚪ MINIMAL RISK
```

---

## Risk Classification Register Entry

Complete this for each AI system:

| Field | Entry |
|-------|-------|
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
| Article 6(3) exclusion applies? | Yes / No (justify) |
| **FINAL RISK CLASSIFICATION** | Unacceptable / High / Limited / Minimal |
| Classification Date | |
| Classified By | |
| Next Review Date | |

---

## Compliance Obligations by Tier

| Tier | Key Obligations |
|------|----------------|
| **Unacceptable** | System must not be placed on market or put into service |
| **High Risk** | Risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy, conformity assessment, EU registration |
| **Limited Risk** | Transparency disclosures to users; deepfake labelling |
| **Minimal Risk** | No mandatory obligations; voluntary codes of conduct encouraged |

---

*Part of the [EU AI Act Compliance Toolkit](README.md)*
