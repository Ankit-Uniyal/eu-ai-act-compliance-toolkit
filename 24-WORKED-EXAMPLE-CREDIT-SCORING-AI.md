# 24 — Worked Example: Credit Scoring AI System

**EU AI Act Reference:** Article 6(2) | Annex III Area 5 (Access to and enjoyment of essential private services and public services and benefits) | Articles 9-17 | Article 27 | Article 43-47
**Applies to:** This worked example; providers and deployers of AI systems used in consumer credit assessment
**Last Updated:** April 2026

## Purpose

This worked example demonstrates how to apply the full EU AI Act Compliance Toolkit to a credit scoring AI system — a system that falls squarely within Annex III Area 5 of the EU AI Act (high-risk AI used in access to private services, specifically creditworthiness assessment).

It complements the existing HR Screening System worked example (WORKED-EXAMPLE-HR-SCREENING-SYSTEM.md), providing a second end-to-end illustration covering a different high-risk category and a deployer-provider split scenario.

**Note:** This is a fictional worked example for training and illustration purposes. Names, data, and specifics are fictional.

---

## Part 1 — System Description

### 1.1 Scenario

**Organisation:** RetailBank NV — a mid-sized retail bank operating in the Netherlands, Belgium, and Germany.

**System Name:** CreditScore-AI v2.3

**System Provider:** FinTech Solutions BV (a Netherlands-based AI company)

**Deployer:** RetailBank NV

**Purpose:** CreditScore-AI v2.3 is a machine learning model that assesses the creditworthiness of individual applicants for personal loans between €1,000 and €50,000. It generates a credit risk score (0-1,000) and a decision recommendation (Approve / Refer for human review / Decline). Human loan officers make all final lending decisions; the system does not autonomously approve or decline applications.

**Technology:** Gradient boosted decision tree model (LightGBM); trained on 5 years of RetailBank NV historical loan data; 47 input features.

**Deployment context:** Web and mobile loan application portal; also accessible to branch advisors.

---

## Part 2 — Step 1: Risk Classification

**Reference: 01-RISK-CLASSIFICATION-GUIDE.md**

### 2.1 Is CreditScore-AI an AI System Under Article 3(1)?

| Test | Assessment |
|---|---|
| Machine-based system? | Yes — LightGBM model |
| Infers from input to produce outputs (predictions, decisions, recommendations)? | Yes — outputs credit score and decision recommendation |
| Can influence real-world environments? | Yes — loan decisions affect individuals' access to credit |

**Conclusion: CreditScore-AI is an AI system under Article 3(1).** ✓

### 2.2 Check Against Article 5 — Prohibited Practices

| Prohibited Practice | Applicable? |
|---|---|
| Subliminal manipulation (Art. 5(1)(a)) | No |
| Exploitation of vulnerability (Art. 5(1)(b)) | No — but DPA guidance on vulnerable customers should be consulted |
| Social scoring by public authorities (Art. 5(1)(c)) | No — private lender |
| Real-time remote biometric identification (Art. 5(2)) | No |
| Biometric categorisation for inferences (Art. 5(1)(d)) | No |

**Conclusion: No prohibited practices. Proceed to Annex III assessment.** ✓

### 2.3 Annex III High-Risk Assessment

| Annex III Area | Description | Applicable? |
|---|---|---|
| Area 1 — Biometrics | | No |
| Area 2 — Critical infrastructure | | No |
| Area 3 — Education | | No |
| Area 4 — Employment | | No |
| **Area 5 — Access to private services** | AI used in creditworthiness assessment and credit scoring of natural persons | **YES** |
| Area 6 — Law enforcement | | No |
| Area 7 — Migration | | No |
| Area 8 — Administration of justice | | No |

**Annex III, Area 5, Item (b):** "AI systems intended to be used for the purpose of making decisions, or materially influencing decisions, on the creditworthiness of natural persons or on their access to or enjoyment of essential private services."

**Conclusion: CreditScore-AI is HIGH-RISK under Annex III Area 5(b).** ✓

### 2.4 Article 6(3) Exclusion Assessment

Article 6(3) permits exclusion from high-risk treatment if the AI system does not pose a significant risk. The deployer (RetailBank NV) has assessed:

- The system materially influences credit decisions affecting individuals' access to essential services
- Loan decisions have significant financial and social consequences for individuals
- No Article 6(3) exclusion applies

**Conclusion: Article 6(3) exclusion NOT applicable. Full Chapter III obligations apply.** ✓

---

## Part 3 — Step 2: Roles — Provider vs. Deployer

**Reference: 10-PROVIDER-DEPLOYER-RESPONSIBILITIES.md**

### 3.1 Role Allocation

| Party | Role | Key Obligations |
|---|---|---|
| FinTech Solutions BV | Provider (places AI system on market) | Articles 9-17: risk management, data governance, technical documentation, logging, transparency, human oversight design, accuracy, QMS; conformity assessment; EU Declaration of Conformity; EU database registration |
| RetailBank NV | Deployer (puts into service) | Art. 26: use in accordance with instructions; human oversight; input data quality; monitoring; incident reporting; worker information; FRIA (if applicable — public service? — No, private bank, not mandatory, but good practice); GDPR compliance |

### 3.2 Key Provider-Deployer Interface Points

| Obligation | Provider Action | Deployer Action |
|---|---|---|
| Instructions for use | FinTech Solutions provides instructions per Art. 13(3) | RetailBank implements — human oversight, data input quality |
| Human oversight | FinTech Solutions designs override capability; defines oversight role requirements | RetailBank assigns trained loan officers; ensures meaningful review |
| Logging | FinTech Solutions builds logging capability per Art. 12 | RetailBank retains logs where within deployer control (Art. 26(6)) |
| Post-market monitoring | FinTech Solutions operates PMM plan; receives deployer data | RetailBank reports performance data and incidents to FinTech Solutions |
| Serious incidents | FinTech Solutions reports to MSA within 72 hours | RetailBank reports to FinTech Solutions immediately; may also notify MSA as deployer |

---

## Part 4 — Step 3: Risk Management System

**Reference: 02-CONFORMITY-ASSESSMENT-CHECKLIST.md (Section A) | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md (Section 4)**

### 4.1 Key Risks Identified (Article 9)

| Risk ID | Risk Description | Likelihood | Severity | Residual Risk | Mitigation |
|---|---|---|---|---|---|
| R-001 | Model underperforms for underrepresented demographic groups → disparate impact in lending | Medium | High | Medium | Bias audit; fairness thresholds; human review escalation for borderline cases |
| R-002 | Input data quality from applicant is poor or fraudulent → incorrect credit score | Medium | High | Low | Input validation; fraud detection layer; human oversight required for all Decline recommendations |
| R-003 | Model drift as economic conditions change → predictions become less accurate | Medium | Medium | Low | Monthly accuracy monitoring; quarterly recalibration review |
| R-004 | Automation bias — loan officers over-rely on score, rubber-stamping decisions | Medium | High | Medium | Training programme; decision record requires officer to document independent assessment |
| R-005 | Adversarial gaming by applicants who manipulate inputs | Low | Medium | Low | Feature engineering to reduce gameable features; anomaly detection |
| R-006 | Data breach — applicant personal data including financial data | Low | High | Low | ISO 27001 controls; encryption at rest and in transit; access controls |

### 4.2 Risk Management Process

The risk management system is iterative (Art. 9(1)):
- **Pre-deployment:** Full risk assessment before each major release
- **Quarterly:** PMM data review triggering risk register update if performance thresholds crossed
- **Annually:** Full risk management system review by AI Governance Committee
- **Event-triggered:** Immediate review upon serious incident or MSA inquiry

---

## Part 5 — Step 4: Data Governance

**Reference: 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md (Section 2.5)**

### 5.1 Training Data Summary

| Attribute | Detail |
|---|---|
| Data source | RetailBank NV historical loan data (2019-2024) |
| Data volume | 2.3 million loan applications; 1.8 million with outcome data |
| Data features (47) | Age, income, employment type, loan amount requested, loan term, existing debt, payment history, residence tenure, region, and 37 further financial/behavioural features |
| Personal data | Yes — financial and demographic data of RetailBank NV customers |
| Special category data | No direct special category data used; age and region are proxy variables — bias assessment conducted |
| GDPR lawful basis for training | Art. 6(1)(f) GDPR — legitimate interests of RetailBank NV (internal product development); LIA completed per Doc 21 |

### 5.2 Bias Audit Summary

| Protected Characteristic | Proxy Variables Used? | Demographic Parity Assessed? | Outcome |
|---|---|---|---|
| Age | Age (direct feature) | Yes | Approval rate gap < 3% across age brackets 25-65; 18-24 cohort reviewed separately |
| Gender | Not a direct feature | Yes | No statistically significant disparity identified |
| Ethnicity / Race | Not a feature; region used as proxy | Yes | Regional disparity identified; mitigated by removing high-correlation regional codes; residual disparity < 5% |
| Income level | Direct feature (by design) | Yes — within-income-band performance | Disparity by design (credit risk); documented as intentional and reviewed for proportionality |

**Bias audit result:** PASSED with conditions — regional proxy variable monitoring ongoing; fairness dashboard deployed.

---

## Part 6 — Step 5: Technical Documentation

**Reference: 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md**

### 6.1 Annex IV Section Completion Status

| Annex IV Section | Status | Notes |
|---|---|---|
| §1 General Description | Complete | Intended purpose: creditworthiness assessment for personal loans |
| §2 Detailed System Description | Complete | LightGBM architecture; training data per Part 5 above |
| §3 Monitoring, Functioning, Control | Complete | Capabilities/limitations; human oversight; logging; performance by group |
| §4 Risk Management | Complete | Per Part 4 above |
| §5 Lifecycle Changes | Complete | Version history; v1.0-v2.3 documented |
| §6 Standards Applied | Complete | ISO/IEC 42001:2023; ISO 27001; EBA Guidelines on internal governance |
| §7 EU Declaration of Conformity | Draft — pending conformity assessment completion | |
| §8 Post-Market Monitoring | Complete | Monthly accuracy monitoring; quarterly review |

---

## Part 7 — Step 6: Human Oversight

**Reference: 07-HUMAN-OVERSIGHT-FRAMEWORK.md**

### 7.1 Oversight Design

| Requirement | How Addressed |
|---|---|
| Art. 14(1) — Effective oversight by natural persons | All final credit decisions made by trained loan officers; system outputs score and recommendation only |
| Art. 14(3)(a) — Override capability | Loan officers can override any system recommendation in the loan management system; override requires documentation of reasoning |
| Art. 14(3)(b) — Awareness of automation bias | AI literacy training includes module on automation bias; officers trained to form independent assessment before viewing AI score |
| Art. 14(3)(c) — Interpret outputs correctly | Training programme; system UI includes explanation of score components; confidence intervals displayed |
| Art. 14(3)(d) — Ability to refuse to use | Officers may escalate to Senior Credit Manager if concerned about system outputs |
| Art. 14(4) — Special attention to vulnerable persons | Flagging system for applicants triggering vulnerable customer indicators; enhanced human review required |

### 7.2 Human Oversight Roles

| Role | Training Required | Certification Level | Assigned To |
|---|---|---|---|
| Loan Officer (AI Oversight Person) | EU AI Act AI literacy (Art. 4) + CreditScore-AI specific training | AI Oversight Level 1 | All retail lending staff |
| Senior Credit Manager | Advanced AI oversight training | AI Oversight Level 2 | Credit management team |
| AI Oversight Officer | Full AI Act compliance training | AI Oversight Level 3 | Designated per Art. 26(2) |

**Reference: 17-AI-LITERACY-COMPETENCY-FRAMEWORK.md** for training requirements.

---

## Part 8 — Step 7: Transparency and Instructions for Use

**Reference: 06-TRANSPARENCY-OBLIGATIONS.md**

### 8.1 Instructions for Use (Article 13(3)) — Key Elements

| Art. 13(3) Element | Content |
|---|---|
| (a) Intended purpose | Personal loan creditworthiness assessment for adults aged 18+; personal loans €1,000-€50,000; Netherlands, Belgium, Germany |
| (b) Level of accuracy declared | Gini coefficient 0.72 (overall); AUC 0.87; see performance tables in technical documentation |
| (c) Known / foreseeable circumstances affecting accuracy | Applications from applicants with less than 12 months credit history; self-employed applicants with irregular income patterns; recent major life events not reflected in historical data |
| (d) Input data specifications | 47 specified input fields; data quality requirements; validation rules |
| (e) Changes requiring new conformity assessment | Changes to training data; changes to input features; changes to decision threshold; change of intended purpose |
| (f) Post-market monitoring obligations | RetailBank NV to provide quarterly performance data; incident reporting per Art. 26(5) |

### 8.2 Consumer Transparency (Article 13(1) and GDPR Art. 22)

RetailBank NV (as Deployer) must inform applicants:

| Disclosure | Method | When |
|---|---|---|
| AI is used in credit assessment | Privacy notice; loan application form | Before application |
| Nature and logic of AI-assisted assessment | On request and if adverse decision (GDPR Art. 22(3)) | On request; automatically on Decline |
| Right to human review | Applicant letter/email on adverse decision | At decision |
| Right to contest | Complaints process | At decision |

---

## Part 9 — Step 8: GDPR Joint Compliance

**Reference: 18-GDPR-AI-ACT-INTERSECTION.md | 21-LEGITIMATE-INTEREST-ASSESSMENT.md**

### 9.1 Key GDPR Obligations

| Obligation | How Addressed |
|---|---|
| Lawful basis for credit assessment processing | Art. 6(1)(b) GDPR — necessary for performance of contract (processing loan application) |
| Lawful basis for AI model training | Art. 6(1)(f) — legitimate interests; LIA completed (Doc 21 template) |
| GDPR Art. 22 automated decision-making | System generates recommendation not final decision; genuine human review by loan officer; Art. 22 exception applies (Art. 22(2)(a) — contract necessity) where human reviews and makes final decision |
| DPIA required? | Yes — Art. 35(3)(a) (systematic profiling of natural persons with legal/significant effects); DPIA completed |
| Privacy notice updated? | Yes — includes AI processing description; Art. 13(2)(f) logic of automated processing included |
| Data subject rights procedure | Updated — includes right to request human review; right to obtain explanation; right to object to profiling |

---

## Part 10 — Step 9: Conformity Assessment and Market Placement

### 10.1 Conformity Assessment Method

| Assessment | Detail |
|---|---|
| Annex III Area 5 — Notified Body required? | No — Annex III Area 5 is not Annex I product safety. Internal conformity assessment (Annex VI) permitted. |
| Internal conformity assessment completed? | Yes — per Doc 02; result: CONFORMANT |
| EU Declaration of Conformity prepared? | Yes — per Doc 12 |
| CE marking required? | No — not Annex I product |
| EU AI database registration required? | Yes — Article 49; registration to be completed before placement |
| Registration status | PENDING — timeline: before deployment in Netherlands market |

### 10.2 Conformity Assessment Result

**Overall result: CONFORMANT** — subject to:
1. Ongoing bias monitoring maintaining regional disparity below 5%
2. Human oversight training programme completion for all RetailBank NV loan officers
3. EU AI database registration before market placement

---

## Part 11 — Step 10: Post-Market Monitoring Plan (Summary)

**Reference: 09-POST-MARKET-MONITORING-PLAN.md | Doc 04 Section 8**

| PMM Activity | Frequency | Method | Threshold / Alert |
|---|---|---|---|
| Accuracy monitoring (Gini coefficient, AUC) | Monthly | Automated; holdout test set | Drop > 0.03 from declared value |
| Bias and fairness monitoring | Quarterly | Demographic parity re-assessment | Any group disparity > 5% |
| Model drift monitoring | Monthly | Population Stability Index (PSI) | PSI > 0.2 triggers recalibration review |
| Deployer feedback and complaints | Monthly | RetailBank NV incident reports; complaint register | Any complaint involving discrimination or systematic error |
| Economic environment review | Quarterly | Macroeconomic indicator review | Significant change in credit market conditions |

---

## Part 12 — AI Literacy Requirements

**Reference: 17-AI-LITERACY-COMPETENCY-FRAMEWORK.md**

| Role | Required Training | By When |
|---|---|---|
| Loan officers (AI oversight persons) | Module A: AI fundamentals; Module C: CreditScore-AI specific; Module D: Automation bias | Before first use of system |
| Senior Credit Managers | All above + Module E: Regulatory obligations (Art. 14, 26) | Before system goes live |
| RetailBank NV AI Oversight Officer | Full competency framework including Art. 4 AI literacy obligations | Before deployment |
| RetailBank NV DPO | GDPR/AI Act intersection module | Before deployment |

---

## Part 13 — Summary Compliance Status

| Compliance Area | Status | Key Actions Remaining |
|---|---|---|
| Risk Classification | ✅ Complete | — |
| Provider/Deployer roles | ✅ Complete | — |
| Risk Management System | ✅ Complete | Quarterly review cycle established |
| Data Governance | ✅ Complete | Regional bias monitoring ongoing |
| Technical Documentation | ✅ Complete | DoC pending |
| Human Oversight Framework | ✅ Complete | Training programme in progress |
| Transparency / Instructions for Use | ✅ Complete | Consumer disclosure in privacy notice |
| GDPR Joint Compliance | ✅ Complete | DPIA completed |
| Conformity Assessment | ✅ CONFORMANT | — |
| EU Database Registration | ⚠️ Pending | Register before Netherlands launch |
| Post-Market Monitoring | ✅ Complete | Monitoring systems operational |
| AI Literacy | ⚠️ In Progress | Training completion required before go-live |
| Article 26(7) Worker Notice | ✅ Complete | Loan officer notice issued per Doc 22 |

**Overall Deployment Readiness:** **READY TO DEPLOY** — subject to EU database registration and training completion.

---

## Lessons Learned (For Training Purposes)

| Issue | Lesson |
|---|---|
| Regional proxy variable bias initially overlooked | Always test proxies for protected characteristics, not just direct features |
| Art. 22 GDPR / Art. 14 AI Act interface | Human review must be genuinely meaningful — rubber stamping fails both regimes |
| DPIA and FRIA overlap | For credit scoring by a private lender, DPIA required; FRIA is voluntary (not a public body) — but many elements overlap |
| Deployer's Art. 26(7) obligation | Often overlooked — RetailBank NV must inform loan officer staff before system deployment |
| EU database registration timing | Registration must occur before market placement — not after go-live |

---

## Related Toolkit Documents Used in This Example

| Step | Document Used |
|---|---|
| Risk classification | 01-RISK-CLASSIFICATION-GUIDE.md |
| Conformity assessment | 02-CONFORMITY-ASSESSMENT-CHECKLIST.md |
| Technical documentation | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md |
| Provider/deployer responsibilities | 10-PROVIDER-DEPLOYER-RESPONSIBILITIES.md |
| Transparency | 06-TRANSPARENCY-OBLIGATIONS.md |
| Human oversight | 07-HUMAN-OVERSIGHT-FRAMEWORK.md |
| Post-market monitoring | 09-POST-MARKET-MONITORING-PLAN.md |
| AI Literacy | 17-AI-LITERACY-COMPETENCY-FRAMEWORK.md |
| GDPR/AI Act intersection | 18-GDPR-AI-ACT-INTERSECTION.md |
| Scorecard | 19-MASTER-COMPLIANCE-SCORECARD.md |
| LIA template | 21-LEGITIMATE-INTEREST-ASSESSMENT.md |
| Worker information notice | 22-WORKER-INFORMATION-NOTICE.md |

---

*Part of the EU AI Act Compliance Toolkit*

*This worked example is fictional and for illustration purposes only. It does not constitute legal advice. Seek qualified legal counsel for actual credit AI compliance decisions.*
