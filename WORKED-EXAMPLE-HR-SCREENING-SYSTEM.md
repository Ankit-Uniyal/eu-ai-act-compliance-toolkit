# Worked Example: CV Screening AI System (TalentFilter Pro)

**Purpose:** Completed example showing how to apply toolkit documents 01-10.
**System:** TalentFilter Pro - AI-powered CV screening and candidate shortlisting
**Organisation:** HireRight GmbH (fictional EU-based HR technology provider)
**Last Updated:** April 2026

> All organisation names, data, and metrics are fictional.

---

## Step 1: Risk Classification (Document 01)

**Is it an AI system?** TalentFilter Pro uses ML trained on hiring data to infer candidate scores. YES.

**Is it prohibited?** No Article 5 prohibited practices apply. NO.

**High-Risk check:**
- Annex I (Article 6(1)): Standalone software, not safety component of Annex I product. NOT Annex I.
- Annex III (Article 6(2)): CV screening for employment = Annex III Area 4: Employment.
- Article 6(3) exclusions: System makes substantive shortlisting decisions influencing which candidates humans see. Exclusions do NOT apply.

**CLASSIFICATION: HIGH RISK - Annex III Area 4, Employment (Article 6(2))**

| Field | Entry |
|---|---|
| System ID | AI-EU-001 |
| Version | v3.2.1 |
| Provider | HireRight GmbH |
| Risk Classification | HIGH RISK |
| Classified By | Maria Weber, AI Governance Lead |
| Date | 19 April 2026 |
| Next Review | 19 April 2027 |

---

## Step 2: Conformity Assessment (Document 02) - Excerpt

**Section A - Risk Management:** PASS. Risk management system documented Jan 2026. Risk register RR-TF-2026-01 covers all intended uses and foreseeable misuses.

**Section B - Data and Data Governance:** PARTIAL.
- B4 (Bias examination): Gender gap identified (female candidates 8% less likely shortlisted in engineering). Recalibrated in v3.2.1. Follow-up audit Q3 2026.
- B7 (Data gaps): Candidates over 50 underrepresented. Expanded dataset in progress.

**Section F - Human Oversight:** PASS. Override and stop mechanisms implemented and tested.

**Section G - Accuracy and Robustness:** PASS. Precision 0.81, Recall 0.74 (both above thresholds).

**Overall Result: CONDITIONAL - Remediation plan approved for B4 and B7. Deploy with enhanced oversight pending remediation Q3 2026.**

---

## Step 3: FRIA (Document 03)

Note: Article 27 FRIA is a DEPLOYER obligation (public bodies/public services). HireRight provides a FRIA template to deployers and conducts a voluntary FRIA.

**Selected Rights Impact:**

| Right | Charter | Impact | Mitigation |
|---|---|---|---|
| Non-discrimination | Art. 21 | High | Mandatory human review; quarterly bias audit; override logging |
| Effective remedy | Art. 47 | Medium | Candidate disclosure; complaints procedure; right to human review |
| Freedom to choose occupation | Art. 15 | Medium | Human final decision mandatory; AI output advisory only |

**Bias Assessment:**
- Gender (Sex): HIGH - 8% shortlisting gap remediated in v3.2.1. Mandatory human review of engineering roles.
- Age (50+): MEDIUM - Underrepresented in training data. Expanded dataset; monitoring in PMM.

**FRIA Result: APPROVED WITH CONDITIONS**
1. Gender bias remediation complete by Q3 2026
2. All AI recommendations require human review before hiring decisions
3. Candidates must be informed AI screening was used
4. Deployers must offer right to request human review

---

## Step 4: Technical Documentation (Document 04) - Key Fields

| Field | Value |
|---|---|
| Architecture | Fine-tuned BERT classifier + ranking model |
| Training data | 2.3M anonymised CV-outcome pairs, 2018-2024 |
| Languages | German, English, Dutch |
| Personal data in training | Yes - anonymised; not retained in model |
| Special category data | No - sensitive attributes excluded |
| Precision | 0.81 (threshold >0.75) - PASS |
| Recall | 0.74 (threshold >0.70) - PASS |
| Gender parity ratio | 1.08 (threshold <1.15) - PASS (remediated from 1.19) |
| Age parity (50+) | 1.14 (threshold <1.20) - PASS |

---

## Step 5: AI System Register Entry (Document 05)

| Field | Entry |
|---|---|
| System ID | AI-EU-001 |
| Risk Tier | HIGH RISK |
| Annex III Category | Area 4 - Employment and Workers Management |
| EU DB Registration | Pending (mandatory before market placement Aug 2026) |
| Conformity Assessment | Conditional - remediation in progress |
| Status | In Development / Pre-Market |

---

## Step 6: Human Oversight (Document 07) - Decision Workflow

1. Recruiter uploads job description and CV pool
2. System generates ranked shortlist with scores and rationale
3. **Output is ADVISORY ONLY** - recruiter reviews all recommendations
4. Recruiter actively confirms or overrides each recommendation (UI requires explicit action)
5. All decisions logged in audit trail
6. No candidate may be rejected solely on AI output

**Automation Bias Mitigations:**
- 2-hour mandatory recruiter training on automation bias
- UI requires active confirmation - no passive acceptance
- Override rate target: >15%. Alert if <10% (possible automation bias signal)

---

## Step 7: Post-Market Monitoring (Document 09) - Key Metrics

| Metric | Baseline | Alert Threshold | Critical Threshold |
|---|---|---|---|
| Precision | 0.81 | <0.75 | <0.68 |
| Gender parity ratio | 1.08 | >1.15 | >1.25 |
| Age parity (50+) | 1.14 | >1.20 | >1.30 |
| Human override rate | 18% | <10% | <5% |

---

## Key Lessons for Practitioners

1. **Bias in training data is the primary high-risk for HR AI.** Always conduct pre-deployment bias audits with specific demographic parity metrics. Post-deployment monitoring is not sufficient alone.

2. **Article 6(3) exclusions rarely apply to decision-support systems.** A CV screener that generates shortlists and influences which candidates humans see has direct individual impact. Document why exclusions do not apply.

3. **The FRIA is a deployer obligation, not a provider obligation.** Providers should prepare FRIA templates and support materials to enable deployers to complete their FRIA - but cannot do it for them.

4. **Conditional conformity is a realistic, valid outcome.** Few complex AI systems pass every requirement at first assessment. Document the remediation plan clearly with specific deadlines and owners.

5. **Automation bias monitoring is critical and commonly missed.** Set concrete override rate targets. A <5% override rate almost certainly means humans are rubber-stamping AI recommendations, not genuinely reviewing them.

6. **EU database registration is mandatory BEFORE market placement.** Plan the timeline: build, test, conform, register, then deploy. Do not start the clock only at deployment.

---

*Part of the EU AI Act Compliance Toolkit - Worked Example*
