# 21 — Legitimate Interest Assessment (LIA) Template

**GDPR Reference:** Article 6(1)(f) | Recital 47 | Recital 48
**EU AI Act Reference:** Article 10 (data governance) | Article 17 (QMS)
**Applies to:** Organisations processing personal data for AI training, AI system operation, or bias monitoring under the GDPR legitimate interests basis
**Last Updated:** April 2026

## Purpose

Article 6(1)(f) GDPR permits processing of personal data where necessary for the purposes of the legitimate interests pursued by the controller or a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject.

This Legitimate Interest Assessment (LIA) template documents the three-part test required to rely on Art. 6(1)(f):
1. **Purpose test** — Is there a legitimate interest?
2. **Necessity test** — Is the processing necessary for that interest?
3. **Balancing test** — Is the interest overridden by the data subject's interests, rights, or freedoms?

**Relationship to AI Act:** The AI Act does not establish lawful bases for GDPR processing. However, many AI system activities (training data processing, bias monitoring, logging under Art. 12) rely on GDPR Art. 6(1)(f). Where the AI Act imposes processing obligations (e.g. mandatory logging under Art. 12), the appropriate GDPR basis is Art. 6(1)(c) (legal obligation), not Art. 6(1)(f). This LIA applies only to processing not directly mandated by the AI Act.

> **Important:** This template does not constitute legal advice. Seek qualified legal counsel and consult your Data Protection Officer before relying on legitimate interests as a lawful basis.

## Document Control

| Field | Entry |
|---|---|
| LIA Reference Number | LIA-[001] |
| AI System Name | |
| Processing Activity | |
| Controller | |
| DPO Reviewed | Yes / No / N/A |
| DPO Review Date | |
| Approved By | |
| Approval Date | |
| Review Date | |
| Status | Draft / Approved / Under Review |

---

## Part 1 — Processing Activity Description

### 1.1 What personal data is being processed?

| Data Category | Specific Data Elements | Sensitivity Level |
|---|---|---|
| | | Standard / Special Category |

### 1.2 Who are the data subjects?

*Describe the categories of individuals whose data is processed.*

### 1.3 What is the processing activity?

*Describe the specific processing operation, e.g. "Training a credit-scoring AI model on historical loan application data including applicant demographics".*

### 1.4 What is the purpose of the processing?

*State the specific purpose clearly and concisely.*

### 1.5 Is special category data involved?

- [ ] No — proceed with Art. 6(1)(f) LIA
- [ ] Yes — Art. 9(2) GDPR exemption is also required. Document Art. 9(2) basis separately.

---

## Part 2 — Purpose Test (Is There a Legitimate Interest?)

### 2.1 Identifying the Legitimate Interest

The legitimate interest must be lawful, real, and not trivial.

| Question | Response |
|---|---|
| What is the legitimate interest pursued? | |
| Is this interest lawful (not contrary to law or public policy)? | Yes / No — Evidence: |
| Is this a current, real interest (not speculative)? | Yes / No — Evidence: |
| Is the interest specific enough to enable the balancing test? | Yes / No |

**Common legitimate interests in AI contexts:**

| AI Processing Activity | Typical Legitimate Interest |
|---|---|
| Training a commercial AI model on customer data | Commercial innovation; improving products and services for customers |
| Bias auditing using historical personal data | Ensuring fairness; protecting data subjects from discriminatory AI outputs |
| Using a deployed AI system to make risk assessments | Risk management; preventing fraud or financial harm |
| Monitoring AI system performance on real data | Quality assurance; ensuring the AI system continues to function correctly |
| Training data from publicly available sources | Innovation; developing beneficial AI technology |

### 2.2 Purpose Test Assessment

| Criterion | Assessment | Satisfied? |
|---|---|---|
| Legitimate interest clearly identified | | Yes / No |
| Interest is lawful | | Yes / No |
| Interest is not speculative | | Yes / No |
| Interest is sufficiently specific | | Yes / No |

**Purpose Test Conclusion:** PASSED / FAILED / CONDITIONAL

---

## Part 3 — Necessity Test (Is the Processing Necessary?)

### 3.1 Necessity Assessment

Processing is necessary only if it is the minimum required to achieve the purpose. Consider whether the purpose could be achieved by less privacy-intrusive means.

| Question | Response |
|---|---|
| Is the processing necessary to achieve the stated purpose? | Yes / No |
| Could the purpose be achieved without processing personal data? | Yes (purpose fails necessity test) / No |
| Could the purpose be achieved with anonymised or pseudonymised data? | Yes / No — Explain why not: |
| Could the purpose be achieved with synthetic data? | Yes / No — Explain why not: |
| Is the minimum amount of personal data used? | Yes / No — Identify excess: |
| Are retention periods minimised appropriately? | Yes / No |

### 3.2 Data Minimisation and Alternatives Assessment

| Alternative Considered | Why Not Sufficient |
|---|---|
| Fully anonymised data | |
| Synthetic data | |
| Aggregated data | |
| Reduced dataset | |

### 3.3 Necessity Test Assessment

| Criterion | Assessment | Satisfied? |
|---|---|---|
| Processing is necessary (cannot achieve purpose otherwise) | | Yes / No |
| No less intrusive alternative exists | | Yes / No |
| Data is minimised to what is strictly needed | | Yes / No |

**Necessity Test Conclusion:** PASSED / FAILED / CONDITIONAL

---

## Part 4 — Balancing Test (Do Data Subject Interests Override?)

### 4.1 Data Subject's Interests, Rights, and Freedoms

Identify and assess the nature of the data subjects' interests:

| Factor | Assessment | Impact Level (High/Medium/Low) |
|---|---|---|
| Nature of the personal data (sensitivity) | | |
| Reasonable expectations of data subjects | | |
| Likely impact on data subjects | | |
| Whether data subjects would object if asked | | |
| Vulnerability of data subjects | | |
| Possible consequences if data is misused | | |

### 4.2 AI-Specific Risk Factors

In AI processing contexts, the following additional risk factors must be considered:

| AI Risk Factor | Present? | Mitigation |
|---|---|---|
| Automated decision-making with legal / significant effects | Yes / No | |
| Profiling of individuals | Yes / No | |
| Processing of special category data (even if Art. 9 basis exists) | Yes / No | |
| Large-scale processing | Yes / No | |
| Potential for discriminatory AI outputs | Yes / No | |
| Data subjects are in a position of vulnerability (employees, consumers in weaker positions) | Yes / No | |
| Limited transparency to data subjects about AI use of their data | Yes / No | |

### 4.3 Safeguards and Mitigations

Identify the safeguards that reduce the weight given to data subjects' interests:

| Safeguard | Implemented? | How It Reduces Impact |
|---|---|---|
| Data subjects informed (privacy notice updated) | Yes / No | |
| Right to object mechanism in place (Art. 21 GDPR) | Yes / No | |
| Data minimisation implemented | Yes / No | |
| Pseudonymisation / anonymisation applied where possible | Yes / No | |
| Strict access controls | Yes / No | |
| Retention limits imposed | Yes / No | |
| Security measures (ISO 27001 or equivalent) | Yes / No | |
| Bias audit and fairness controls for AI outputs | Yes / No | |
| Human oversight of AI-influenced decisions | Yes / No | |

### 4.4 Balancing Assessment

| Factor | Weight Given | Notes |
|---|---|---|
| Strength of legitimate interest | High / Medium / Low | |
| Necessity of processing | High / Medium / Low | |
| Nature and sensitivity of data | High / Medium / Low | |
| Reasonable expectations | High / Medium / Low | |
| Potential impact on data subjects | High / Medium / Low | |
| Safeguards implemented | High / Medium / Low | |

**Balancing Test Conclusion:**

- [ ] **Legitimate interest prevails** — Data subject interests do not override; processing may proceed
- [ ] **Conditional** — Legitimate interest prevails subject to the safeguards documented above being implemented
- [ ] **Data subject interests override** — Legitimate interest basis cannot be used; identify alternative basis or redesign processing

---

## Part 5 — Overall LIA Conclusion

| Test | Result |
|---|---|
| Purpose test | PASSED / FAILED |
| Necessity test | PASSED / FAILED |
| Balancing test | LI PREVAILS / CONDITIONAL / OVERRIDDEN |
| **Overall LIA result** | **APPROVED / CONDITIONAL APPROVAL / REFUSED** |

### 5.1 Conditions (if Conditional Approval)

List any conditions that must be satisfied before processing proceeds:

| Condition | Owner | Due Date | Status |
|---|---|---|---|
| | | | |

### 5.2 Required Actions Before Processing

| Action | Owner | Due Date |
|---|---|---|
| Update privacy notice to reflect this processing | | |
| Implement right to object mechanism (Art. 21 GDPR) | | |
| Confirm all safeguards in Part 4.3 are operational | | |
| Brief DPO on approved LIA | | |

---

## Part 6 — Ongoing Review

The legitimate interest basis must be kept under review. Review is required when:
- The processing activity or purpose changes
- There is a change in the data subjects affected or their circumstances
- There is new evidence of harm to data subjects
- A data subject objects under Art. 21 GDPR
- At least annually for high-risk AI processing

| Review Date | Reviewer | Changes Made | Approved By |
|---|---|---|---|
| | | | |

---

## Related Documents

| Document | Reference |
|---|---|
| GDPR / AI Act Intersection Map | 18-GDPR-AI-ACT-INTERSECTION.md |
| FRIA Template | 03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md |
| Technical Documentation | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md |
| Human Oversight Framework | 07-HUMAN-OVERSIGHT-FRAMEWORK.md |
| Master Compliance Scorecard | 19-MASTER-COMPLIANCE-SCORECARD.md |

---

*Part of the EU AI Act Compliance Toolkit*

*This document does not constitute legal advice. Seek qualified legal counsel for binding compliance determinations. GDPR guidance from your national Data Protection Authority should also be consulted.*
