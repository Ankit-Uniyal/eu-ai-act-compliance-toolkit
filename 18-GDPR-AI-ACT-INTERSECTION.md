# 18 — GDPR and EU AI Act Intersection Map

**EU AI Act Reference:** Articles 9, 10, 13, 26, 27, 50
**GDPR Reference:** Articles 5, 6, 9, 13-14, 17, 22, 25, 35
**Applies to:** Providers and Deployers processing personal data in AI systems
**Last Updated:** April 2026

## Purpose

The EU AI Act and GDPR operate in parallel for any AI system that processes personal data. They are separate regulations with different supervisory authorities, but they overlap significantly and must both be complied with simultaneously. This document maps the key intersection points, identifies where joint compliance measures can satisfy both frameworks, and flags where obligations diverge and require separate action.

**Supervisory Authorities:**
- **EU AI Act:** National Market Surveillance Authorities (MSAs); EU AI Office (for GPAI)
- **GDPR:** Data Protection Authorities (DPAs / Supervisory Authorities)

> **Important:** This document is a compliance mapping tool, not legal advice. The intersection of GDPR and the EU AI Act is an evolving area. Always consult qualified legal counsel for decisions in specific deployments.

---

## Part 1 — The Regulatory Relationship

### 1.1 How the Regulations Relate

| Issue | Position |
|---|---|
| Do both regulations apply simultaneously? | Yes — they are independent regulations with separate requirements and supervisory authorities |
| Does the AI Act override GDPR? | No — Recital 9 EU AI Act states that the Act complements GDPR without prejudice to it |
| Can compliance with one satisfy obligations under the other? | In some areas yes (e.g. DPIA and FRIA) — but this must be assessed for each requirement |
| Are there conflicts between the two regulations? | Some tensions exist (e.g. data minimisation vs. need for representative training data) — these are addressed in this document |

### 1.2 Scope Overlap

| AI System Type | GDPR Applies? | EU AI Act Applies? |
|---|---|---|
| AI system processing personal data | Yes | Depends on risk classification |
| High-risk AI system using personal data (HR, credit, healthcare) | Yes | Yes — full Chapter III obligations |
| GPAI model trained on personal data | Yes | Yes — Articles 53-56 |
| AI system with no personal data at any stage | No | Depends on risk classification |
| Automated decision-making affecting individuals | Yes — Article 22 GDPR | May be high-risk — check Annex III |

---

## Part 2 — Data Governance: Article 10 AI Act and GDPR Article 5

AI Act Article 10 requires high-risk AI training, validation, and test data to meet governance requirements. This overlaps heavily with GDPR Article 5 data quality and minimisation principles.

### 2.1 Joint Compliance Map — Data Governance

| Requirement | EU AI Act Reference | GDPR Reference | Joint Compliance Approach |
|---|---|---|---|
| Data is relevant to intended purpose | Art. 10(2) | Art. 5(1)(b) — purpose limitation | Document intended purpose; ensure data is fit for that purpose and not repurposed |
| Data is accurate | Art. 10(3) | Art. 5(1)(d) — accuracy | Implement data quality controls; document in Annex IV (Document 04) |
| Data is minimised | Art. 10(5) — only where strictly necessary | Art. 5(1)(c) — data minimisation | Identify minimum personal data needed; document justification for any special category data use |
| Bias examined | Art. 10(2)(f) | Art. 5(1)(d) — accuracy; Recital 71 GDPR (non-discrimination in profiling) | Conduct pre-market bias audit; document in conformity assessment; ensure outputs do not produce discriminatory results contrary to the accuracy and non-discrimination principles |
| Data integrity and security | Art. 10 (data governance measures) | Art. 5(1)(f) — integrity and confidentiality | Implement technical and organisational measures to protect training data; document security controls |
| Retention limits | Art. 18 — technical docs 10 years | Art. 5(1)(e) — storage limitation | Define retention periods for personal data in training vs. technical documentation; these may differ |

> **Correction note:** GDPR Art. 5(1)(f) covers integrity and confidentiality (security), not bias. Bias and non-discrimination in automated processing is addressed in GDPR Recital 71, the GDPR WP29/EDPB guidance on profiling, and Art. 5(1)(d) accuracy. These have been correctly mapped above.

### 2.2 Special Category Data (Article 9 GDPR / Article 10(5) AI Act)

Both regulations impose heightened requirements for special category personal data (race, ethnicity, health, sexual orientation, religion, trade union membership, biometric data, genetic data).

| Issue | EU AI Act Position | GDPR Position | Action Required |
|---|---|---|---|
| Can special category data be used in training? | Art. 10(5): only where strictly necessary and appropriate safeguards in place | Art. 9 GDPR: prohibited unless explicit exception applies | Identify legal basis (Art. 9(2) GDPR) AND document AI Act necessity justification |
| Bias testing using protected characteristics | Art. 10(2)(f): examine potential biases affecting health, safety, fundamental rights | Recital 71 GDPR: profiling should not lead to discrimination | Use aggregated bias metrics; avoid individual-level profiling for bias testing |
| Biometric data for identification | Prohibited (Art. 5) or high-risk (Annex III Area 1) depending on use | Art. 9 GDPR: biometric data is special category | Requires both GDPR exception AND AI Act conformity assessment |

---

## Part 3 — Automated Decision-Making: GDPR Article 22 and AI Act

### 3.1 The Relationship Between GDPR Article 22 and the AI Act

GDPR Article 22 gives individuals the right not to be subject to solely automated decisions that produce legal or similarly significant effects. Many high-risk AI systems under the EU AI Act involve exactly this type of decision.

| Issue | GDPR Article 22 | EU AI Act | Joint Obligation |
|---|---|---|---|
| Right to not be subject to solely automated decisions | Yes — Article 22(1) | Human oversight required — Articles 14, 26(2) | Human review must be genuine, not nominal — satisfies both if meaningful |
| Exceptions | Art. 22(2): contract necessity, legal authorisation, explicit consent | No equivalent exception in AI Act | GDPR exception does not override AI Act human oversight requirement |
| Right to explanation | Art. 22(3): right to obtain human intervention, express point of view, contest decision | Art. 13 AI Act: transparency to deployers; Art. 26 deployer transparency obligations | Provide explanation of AI role in decision AND human review mechanism |
| Profiling | Art. 4(4) GDPR: automated processing to analyse personal aspects | Risk factor for high-risk classification (Annex III) | Profile-based AI decisions require both GDPR safeguards and AI Act conformity |

### 3.2 Joint Compliance for Automated Decision-Making Systems

Where an AI system makes or materially influences decisions about individuals:

| Action | Satisfies GDPR? | Satisfies AI Act? |
|---|---|---|
| Document that decisions are not solely automated (human has genuine role) | Yes — Art. 22 exception / limitation | Yes — Art. 14 human oversight |
| Inform individuals that AI is used in decision-making | Yes — Art. 13/14 disclosure | Yes — Art. 13 transparency to deployers; Art. 26 user-facing |
| Provide mechanism to request human review | Yes — Art. 22(3) | Yes — Art. 14 override requirement |
| Conduct DPIA (see Part 5 below) | Yes — Art. 35 where high risk | Complementary to FRIA (Art. 27) |

---

## Part 4 — Transparency and Information Rights

### 4.1 Disclosure Obligations Map

| Obligation | GDPR Reference | EU AI Act Reference | Who Must Act | Timing |
|---|---|---|---|---|
| Inform individuals that personal data is processed | Art. 13/14 — privacy notice | — | Data Controller (often Deployer) | At collection / first interaction |
| Inform individuals that AI system is used | Implied in Art. 13/14 if AI affects decisions | Art. 13 (to deployers); Art. 26 (deployer to users) | Provider (to deployers); Deployer (to individuals) | Before interaction or use |
| Disclose AI system interacts with them (chatbot) | Art. 13/14 — processing description | Art. 50(1) — conversational AI disclosure | Provider designs; Deployer discloses | At start of interaction |
| Inform of emotion recognition or biometric categorisation | Art. 13/14 | Art. 50(3) | Deployer | Before processing |
| Disclose deepfake / AI-generated content | Art. 13/14 if personal data involved | Art. 50(4)-(5) | Provider / Deployer | On output |
| Provide meaningful information about automated logic | Art. 22(3) / Art. 13(2)(f) | Art. 13 instructions for use; Art. 26 transparency | Provider + Deployer | On request / proactively |

### 4.2 Privacy Notice Requirements for AI Systems

When deploying an AI system that processes personal data, the privacy notice (GDPR Art. 13/14) should include:

| Item | GDPR Requirement | AI Act Enhancement |
|---|---|---|
| Description of processing | Art. 13(1)(c) | Explain that AI processing is used; describe the AI system's role |
| Automated decision-making | Art. 13(2)(f): meaningful information about logic | Describe AI system type, key parameters used in decision |
| Individual rights | Art. 13(2)(b) | Include right to human review of AI-influenced decisions |
| Profiling | Art. 13(2)(f) | Identify if profiling occurs and its consequences |

---

## Part 5 — DPIA and FRIA: Complementary Assessments

### 5.1 When Are Both Required?

| Assessment | When Required | Who Conducts It |
|---|---|---|
| Data Protection Impact Assessment (DPIA) | GDPR Art. 35: processing likely to result in high risk to individuals, including systematic profiling, large-scale special category data, automated decisions with legal effects | Data Controller (typically Deployer) |
| Fundamental Rights Impact Assessment (FRIA) | AI Act Art. 27: mandatory for certain deployers of high-risk AI (public bodies and private bodies providing public services) | Deployer |

**Key rule:** A DPIA is required whenever the GDPR threshold is met. A FRIA is required whenever the AI Act threshold is met. They are separate assessments, but content overlaps significantly.

### 5.2 DPIA and FRIA — Overlap and Difference

| Element | DPIA (GDPR Art. 35) | FRIA (AI Act Art. 27) |
|---|---|---|
| Scope | Focuses on data protection risks to individuals | Focuses on risks to fundamental rights (broader than just data protection) |
| Mandatory trigger | High risk to natural persons from data processing | Public body or public-service private body deploying high-risk AI |
| Covers fundamental rights? | Partially — privacy and data protection | Fully — all EU Charter rights |
| DPO involvement | Mandatory (GDPR Art. 35(2)) | Recommended (good practice) |
| Outcome | Residual risks accepted / mitigated / DPA consulted | Deployment approved / approved with conditions / deferred / rejected |
| Can they be combined? | Yes — Article 35(10) GDPR permits integration where another EU law requires similar assessment | FRIA template (Document 03) includes GDPR dimensions and can reference DPIA |

### 5.3 Joint DPIA / FRIA Approach

Where both assessments are required, consider a combined document:

| Section | DPIA Satisfied? | FRIA Satisfied? |
|---|---|---|
| System description and intended purpose | Yes | Yes |
| Categories of persons affected | Yes | Yes |
| Personal data processed; special category data | Yes | Partially |
| Automated decision-making assessment | Yes | Yes |
| Fundamental rights assessment (full EU Charter) | Partially (privacy focus) | Yes |
| Bias and discrimination assessment | No (DPIA does not require formal bias audit) | Yes |
| Data subject rights and redress | Yes | Yes |
| Necessity and proportionality | Yes | Yes |
| Risk and mitigation | Yes | Yes |
| Residual risk decision | Yes | Yes |

**Recommended approach:** Use the FRIA template (Document 03) as the primary document and add GDPR-specific sections (lawful basis, data subject rights, DPO consultation, GDPR risk assessment) as appendices or integrated sections.

---

## Part 6 — Lawful Basis for Processing Personal Data in AI Systems

### 6.1 Identifying the Lawful Basis (GDPR Article 6)

| Processing Activity | Typical Lawful Basis | Notes |
|---|---|---|
| Training an AI model on personal data | Legitimate interests (Art. 6(1)(f)) — requires balancing test | Consider whether training could use anonymised or synthetic data instead |
| Using a deployed AI system to process individual's data to make a decision | Contract (Art. 6(1)(b)) or legal obligation (Art. 6(1)(c)) or legitimate interests | Document basis per deployment context |
| FRIA or DPIA processing of staff / user data | Legitimate interests | Document LIA |
| Logging and record-keeping under AI Act Art. 12 | Legal obligation (Art. 6(1)(c)) — AI Act imposes the obligation | AI Act creates the legal basis for mandatory logging |
| Monitoring for bias using personal data | Legitimate interests — with safeguards | Use aggregated analysis; minimise individual data use |

### 6.2 Special Category Data — Legal Basis (GDPR Article 9)

Where special category personal data is processed in training or operation of an AI system:

| Special Category Data | Possible Article 9(2) Basis | AI Act Requirement |
|---|---|---|
| Biometric data for identification | Art. 9(2)(g): substantial public interest; Art. 9(2)(a): explicit consent | High-risk Annex III Area 1 or prohibited (Art. 5) depending on use |
| Health data (medical AI) | Art. 9(2)(h): healthcare purposes; Art. 9(2)(i): public health | High-risk Annex III Area 5 or medical device (MDR) |
| Race / ethnicity for bias testing | Art. 9(2)(g): substantial public interest with safeguards | AI Act Art. 10(2)(f): bias examination permitted |
| Trade union membership (employment AI) | Art. 9(2)(b): employment law; Art. 9(2)(g): public interest | High-risk Annex III Area 4 |

---

## Part 7 — Rights of Data Subjects and AI Act Obligations

### 7.1 Data Subject Rights Relevant to AI Systems

| Right | GDPR Article | AI Act Interaction | Joint Obligation |
|---|---|---|---|
| Right of access | Art. 15 | Transparency requirements (Art. 13 AI Act) | Provide information about AI role in decisions affecting the individual |
| Right to erasure | Art. 17 | AI Act does not override erasure right | Establish process to remove individual's data from training sets if erasure requested (note: may affect model — document approach) |
| Right to object to profiling | Art. 21 | AI Act human oversight (Art. 14) | Accept objection; route to human decision-maker |
| Right not to be subject to solely automated decisions | Art. 22 | Art. 14 human oversight | Ensure meaningful human review is available and documented |
| Right to explanation of automated decisions | Art. 22(3) | Art. 13 instructions for use; deployer transparency | Provide individual with explanation of AI system's role and ability to contest |
| Right to portability | Art. 20 | No direct equivalent | Standard GDPR obligation |
| Right to rectification | Art. 16 | May affect model performance if rectification changes training data | Document approach to rectification requests for training data |

---

## Part 8 — DPO Role in AI Act Compliance

### 8.1 DPO Involvement Requirements

| Activity | DPO Role |
|---|---|
| DPIA (where required) | Mandatory consultation (GDPR Art. 35(2)) |
| FRIA (where required) | Document 03 Part 7: DPO consultation is a required question |
| AI system register | Review for personal data processing identification |
| Conformity assessment | Review data governance sections (Section B) |
| Technical documentation | Review personal data and special category data sections |
| Incident reporting | Coordinate with AI Oversight Officer — AI serious incidents may also be GDPR personal data breaches (Art. 33 GDPR) |

### 8.2 Dual Incident Reporting — AI Act and GDPR

Where a serious incident under the AI Act also involves a personal data breach:

| Obligation | Deadline | Recipient | Document Reference |
|---|---|---|---|
| AI Act serious incident notification | Within 72 hours of awareness | National MSA | 08-INCIDENT-REPORTING-PROCEDURE.md |
| GDPR personal data breach notification | Within 72 hours of awareness | National DPA (supervisory authority) | Standard GDPR breach procedure |
| Notification to affected individuals (if high risk to their rights) | Without undue delay | Affected individuals | GDPR Art. 34 |

> **Note:** The 72-hour window runs from when the organisation became aware. If the same incident triggers both, notifications should be coordinated but filed separately with the MSA and DPA.

---

## Part 9 — Common Conflict Points and Resolution

### 9.1 Tension: Data Minimisation vs. Representativeness

| Tension | GDPR Principle | AI Act Requirement | Resolution |
|---|---|---|---|
| Need representative data vs. data minimisation | Art. 5(1)(c): collect only what is necessary | Art. 10(3): data must be sufficiently representative | Use the minimum volume of personal data that achieves representativeness; consider synthetic data; anonymise where possible; document the necessity assessment |

### 9.2 Tension: Retention of Logs vs. Storage Limitation

| Tension | GDPR Principle | AI Act Requirement | Resolution |
|---|---|---|---|
| 10-year retention of technical documentation | Art. 5(1)(e): kept no longer than necessary | Art. 18: technical docs kept 10 years | AI Act creates a legal obligation (Art. 6(1)(c) GDPR lawful basis) for retention; anonymise or pseudonymise personal data in logs where possible; retain only what is required |

### 9.3 Tension: Model Explainability vs. Trade Secrets

| Tension | GDPR Right | AI Act Requirement | Resolution |
|---|---|---|---|
| Individuals' right to explanation of automated decisions | Art. 22(3): meaningful information about logic | Art. 13: instructions for use to deployers | Provide meaningful, accessible explanation at the individual level without disclosing proprietary model architecture; this is a documented governance decision |

---

## Part 10 — Joint Compliance Checklist

Use this checklist to identify whether joint GDPR / AI Act compliance actions have been completed:

| Action | GDPR Reference | AI Act Reference | Status |
|---|---|---|---|
| Personal data inventory completed for AI system | Art. 30 records of processing | Art. 10 / Art. 11 | Done / Pending |
| Lawful basis for all processing identified and documented | Art. 6 / Art. 9 | Supports Art. 10 | Done / Pending |
| Privacy notice updated to include AI processing | Art. 13/14 | Art. 13 / Art. 26 | Done / Pending |
| Automated decision-making assessment completed | Art. 22 | Art. 14 | Done / Pending |
| DPIA completed (where required) | Art. 35 | Complements FRIA | Done / Pending / N/A |
| FRIA completed (where required) | Complementary | Art. 27 | Done / Pending / N/A |
| DPO consulted on AI system deployment | Art. 35(2) | Doc 03 Part 7 | Done / Pending |
| Data subject rights procedures updated for AI context | Arts. 15-22 | Arts. 13-14, 26 | Done / Pending |
| Special category data legal basis identified | Art. 9 | Art. 10(5) | Done / Pending / N/A |
| Retention schedules cover AI Act 10-year requirement | Art. 5(1)(e) | Art. 18 | Done / Pending |
| Dual incident reporting procedure in place (MSA + DPA) | Art. 33 | Art. 73 | Done / Pending |
| Bias audit results reviewed by DPO | Arts. 5(1)(d), 9; Recital 71 | Art. 10(2)(f) | Done / Pending |

---

## Related Documents

| Document | Reference |
|---|---|
| FRIA Template | 03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md |
| Technical Documentation | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md |
| Transparency Obligations | 06-TRANSPARENCY-OBLIGATIONS.md |
| Human Oversight Framework | 07-HUMAN-OVERSIGHT-FRAMEWORK.md |
| Incident Reporting Procedure | 08-INCIDENT-REPORTING-PROCEDURE.md |
| Provider / Deployer Responsibilities | 10-PROVIDER-DEPLOYER-RESPONSIBILITIES.md |
| Quality Management System | 16-QUALITY-MANAGEMENT-SYSTEM.md |

---

*Part of the EU AI Act Compliance Toolkit*

*This document does not constitute legal advice. Seek qualified legal counsel for binding compliance determinations. GDPR guidance from your national Data Protection Authority should also be consulted.*
