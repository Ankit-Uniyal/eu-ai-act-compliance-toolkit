# 20 — Notified Body Engagement Guide

**EU AI Act Reference:** Article 43 | Article 44 | Article 45 | Article 46 | Annex VII
**Applies to:** Providers of High-Risk AI Systems requiring third-party conformity assessment
**Last Updated:** April 2026

## Purpose

Most high-risk AI systems under the EU AI Act allow providers to self-certify via an internal conformity assessment (Annex VI). However, certain categories require involvement of a Notified Body — an independent third-party assessment organisation accredited by a national accreditation body. This guide explains when a Notified Body is required, how to find and select one, how to prepare for the assessment, and how to manage the ongoing relationship.

## Document Control

| Field | Entry |
|---|---|
| Document Title | Notified Body Engagement Guide |
| Version | |
| Owner | |
| Last Updated | |

---

## Part 1 — When Is a Notified Body Required?

### 1.1 The Default Rule: Internal Conformity Assessment

For most Annex III high-risk AI systems, Article 43(2) permits providers to conduct an internal conformity assessment (Annex VI procedure) without involving a Notified Body. This requires the provider to:
- Verify the system complies with all Chapter III Section 2 requirements (Articles 9-15, 17)
- Maintain technical documentation
- Draw up the EU Declaration of Conformity

### 1.2 When a Notified Body Is Mandatory

A Notified Body is required in two specific circumstances:

**Circumstance 1 — Annex I Product Safety Components (Article 43(1))**

Where a high-risk AI system is a safety component of, or is itself, a product covered by Annex I EU harmonisation legislation, AND that legislation requires third-party conformity assessment, the AI Act conformity assessment must also be carried out by a Notified Body.

Relevant Annex I legislation typically requiring NB involvement:
- Medical Devices Regulation (MDR) (EU) 2017/745 — Class IIa and above
- In Vitro Diagnostic Devices Regulation (IVDR) (EU) 2017/746 — Class B and above
- Machinery Regulation (EU) 2023/1230 — Annex IV machinery
- Radio Equipment Directive 2014/53/EU — certain categories

**Circumstance 2 — Real-Time Remote Biometric Identification Systems (Article 43(1)(b))**

Where a high-risk AI system is intended for use as a real-time remote biometric identification system in publicly accessible spaces, Notified Body involvement is required under Article 43(1)(b).

Under the enacted EU AI Act (Regulation (EU) 2024/1689), the use of real-time remote biometric identification systems in publicly accessible spaces for law enforcement purposes is addressed in **Article 5(2)-(7)**, which sets out the conditions, safeguards, and derogations under which such use may exceptionally be permitted. Systems falling within Article 5(2) derogations that are deployed as high-risk systems under Annex III Area 1 still require Notified Body assessment where Article 43(1)(b) applies.

> **Note:** The biometric categorisation systems listed in Annex III Area 1 that are NOT real-time remote biometric identification systems may still be assessed via internal conformity assessment (Annex VI).

### 1.3 Summary Decision Table

| AI System Type | Notified Body Required? | Assessment Procedure |
|---|---|---|
| Annex III high-risk — standalone software (e.g. HR AI, credit scoring) | No | Internal — Annex VI |
| Annex III high-risk — safety component of Annex I product with mandatory NB | Yes | Annex VII (NB) |
| Medical device AI — Class I | No (unless AI Act Art. 43(1)(b) applies) | Internal — Annex VI |
| Medical device AI — Class IIa and above (MDR) | Yes (MDR NB required) | MDR NB + Annex VII AI Act |
| Real-time remote biometric identification in publicly accessible spaces (Art. 43(1)(b)) | Yes | Annex VII (NB) |
| GPAI model only (no high-risk AI system) | No | N/A — Articles 53-56 apply |

---

## Part 2 — Understanding the Notified Body Role

### 2.1 What a Notified Body Does

Under Article 44 and Annex VII, a Notified Body assesses whether the high-risk AI system meets all applicable requirements. The NB:
- Reviews technical documentation
- Assesses the risk management system
- Evaluates data governance and bias assessment methodology
- Reviews logging, transparency, human oversight, and accuracy provisions
- Issues a certificate of conformity if requirements are met
- Monitors ongoing compliance through surveillance activities

### 2.2 What a Notified Body Does NOT Do

- Does not provide compliance consultancy or tell the provider how to fix non-conformances before assessment (conflict of interest restriction)
- Does not guarantee commercial success or fitness for purpose beyond regulatory requirements
- Does not replace internal QMS or ongoing post-market monitoring obligations
- Does not assess GDPR compliance (separate DPA jurisdiction)

### 2.3 Notified Body Independence Requirements (Article 44)

Notified Bodies must be:
- Independent of the providers and systems they assess
- Free from any commercial, financial, or other pressure that could compromise their objectivity
- Accredited by a National Accreditation Body (NAB) designated by an EU Member State
- Listed in the NANDO database (European Commission database of Notified Bodies)

---

## Part 3 — Finding a Notified Body

### 3.1 NANDO Database

The primary source for finding accredited Notified Bodies is the NANDO (New Approach Notified and Designated Organisations) database maintained by the European Commission:

**NANDO Database:** https://ec.europa.eu/growth/tools-databases/nando/

Search filters to use:
- **Directive / Regulation:** Select the relevant legislation (EU AI Act once operational; or MDR / Machinery for Annex I products)
- **Country:** Select EU Member State where NB is established
- **Product code:** Use relevant product classification codes

### 3.2 EU AI Act Specific Notified Bodies

> **Note:** As of April 2026, the Notified Body designation process under the EU AI Act is still maturing. Many existing NBs designated under Annex I product legislation (MDR, Machinery) are expected to seek designation under the AI Act.

Monitor:
- NANDO database for newly designated AI Act NBs
- EU AI Office announcements: https://digital-strategy.ec.europa.eu/en/policies/ai-office
- National Accreditation Body announcements in your jurisdiction

### 3.3 Criteria for Selecting a Notified Body

Evaluate potential NBs against these criteria:

| Criterion | What to Assess |
|---|---|
| Designation scope | Confirmed designation covers your system type and Annex III category |
| Technical expertise | NB has assessors with relevant AI / ML expertise in your application domain (healthcare, employment, etc.) |
| Sector experience | Prior experience with similar systems in your industry vertical |
| Capacity and timeline | Can accommodate your target assessment timeline; no excessive queue times |
| Geographic presence | Accessible for on-site activities; familiar with relevant national regulations |
| Language | Can conduct assessment in your working language |
| Fee structure | Transparent, proportionate to system complexity |
| References | Can provide client references for comparable assessments |

### 3.4 Notified Body Selection Register

| NB Name | Designation Scope | Member State | Contact | Shortlisted? | Notes |
|---|---|---|---|---|---|
| | | | | Yes / No | |

---

## Part 4 — Preparing for a Notified Body Assessment

### 4.1 Pre-Assessment Readiness Checklist

Complete your internal conformity assessment (Document 02) first. All items should be PASS or PARTIAL with remediation plan before engaging a Notified Body.

| Preparation Item | Status | Reference |
|---|---|---|
| Internal conformity assessment completed | Done / In Progress | 02-CONFORMITY-ASSESSMENT-CHECKLIST.md |
| Technical documentation (Annex IV) complete and reviewed | Done / In Progress | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md |
| Risk management system documented and tested | Done / In Progress | Document 02, Section A |
| Data governance documentation complete (bias audit included) | Done / In Progress | Document 02, Section B |
| Logging capabilities implemented and tested | Done / In Progress | Document 02, Section D |
| Instructions for use prepared | Done / In Progress | Document 02, Section E |
| Human oversight controls designed and tested | Done / In Progress | 07-HUMAN-OVERSIGHT-FRAMEWORK.md |
| Accuracy and robustness metrics declared and achieved | Done / In Progress | Document 02, Section G |
| Quality Management System documented | Done / In Progress | 16-QUALITY-MANAGEMENT-SYSTEM.md |
| EU Declaration of Conformity draft prepared | Done / In Progress | 12-EU-DECLARATION-OF-CONFORMITY.md |
| All known non-conformances have remediation plans | Done / In Progress | |

### 4.2 Documentation Package for Notified Body

Prepare the following documentation package for submission to the NB:

| Document | Content | Status |
|---|---|---|
| System overview and intended purpose | One-page summary; Annex III classification | |
| Technical documentation (Annex IV) | Full document per Document 04 | |
| Risk management system and risk register | Per Article 9 | |
| Training data documentation | Data governance, bias audit results, representativeness assessment | |
| Validation and test reports | Performance metrics, fairness metrics, benchmark results | |
| Architecture and system diagrams | System architecture, data flows, component interactions | |
| Instructions for use | Per Article 13 | |
| Human oversight design documentation | Oversight measures, override mechanisms, automation bias mitigations | |
| Cybersecurity assessment | Article 15 cybersecurity measures | |
| Quality management system | Document 16 | |
| Change management procedure | Substantial modification assessment process | |
| Post-market monitoring plan | Document 09 | |
| Draft EU Declaration of Conformity | Document 12 | |

---

## Part 5 — The Assessment Process (Annex VII)

### 5.1 Assessment Phases

| Phase | Description | Typical Duration | Your Responsibilities |
|---|---|---|---|
| Phase 1: Contract and scoping | Sign engagement agreement; agree scope, timeline, fees | 1-2 weeks | Provide system overview; confirm scope; agree access |
| Phase 2: Document review | NB reviews technical documentation package | 4-8 weeks | Respond to information requests promptly |
| Phase 3: Product assessment | NB technical experts assess the AI system itself; may include testing | 4-8 weeks | Provide system access; support testing activities |
| Phase 4: Findings and non-conformances | NB issues preliminary findings; provider addresses non-conformances | 2-6 weeks | Remediate findings; provide evidence of corrections |
| Phase 5: Certificate decision | NB issues certificate of conformity or declines | 1-2 weeks | — |
| Phase 6: Certificate issuance | Certificate issued; valid for defined period (typically 3-5 years) | — | Update DoC, register, technical docs to reference certificate |

**Total typical timeline:** 3-6 months for a straightforward system. Complex systems, significant non-conformances, or NB capacity constraints can extend this materially. Plan your compliance timeline accordingly.

### 5.2 Types of NB Findings

| Finding Type | Description | Provider Action Required |
|---|---|---|
| Observation | Minor gap; improvement recommended but does not block certificate | Document response; address in next review |
| Minor non-conformance | Gap that can be remediated before certificate issuance | Remediate within agreed timeframe; submit evidence |
| Major non-conformance | Significant gap; certificate cannot be issued until resolved | Full remediation required; may trigger re-assessment |
| Critical finding | System does not meet fundamental requirements | Significant rework; new assessment cycle |

### 5.3 If the NB Declines to Issue a Certificate

If a Notified Body concludes the system does not meet requirements:
- Request a detailed written explanation of all non-conformances
- Assess whether findings are correct or whether you wish to appeal
- If correct: implement remediation and request re-assessment
- If disputing: engage the appeals process (each NB must have a defined appeals mechanism per Article 44(10))

> **Note:** A declined certificate does not automatically require notification to authorities, but the system cannot be placed on the market until conformity is achieved.

---

## Part 6 — Certificate Maintenance and Surveillance

### 6.1 Certificate Validity and Renewal

| Item | Typical Requirement |
|---|---|
| Certificate validity period | 3-5 years (varies by NB and regulation) |
| Renewal process | Re-application and assessment before expiry |
| Surveillance visits | Periodic unannounced or scheduled surveillance (often annual) |
| Change notification | Provider must notify NB of any substantial modifications |

### 6.2 Ongoing NB Notification Obligations

Once a certificate is in place, providers must notify the Notified Body of:

| Event | Notification Required? | Timeline |
|---|---|---|
| Substantial modification to the AI system (Article 25) | Yes | Before implementing change |
| Change to intended purpose | Yes | Before implementing change |
| Serious incident involving the system | Yes (if NB was involved in assessment) | Without undue delay |
| Change of provider name or address | Yes | Within reasonable time |
| Provider becomes aware of non-conformance | Yes | Without undue delay |

### 6.3 Certificate Register

Maintain a register of all active NB certificates:

| Certificate Number | NB Name | AI System | Issue Date | Expiry Date | Surveillance Due | Status |
|---|---|---|---|---|---|---|
| | | | | | | Active / Expired |

---

## Part 7 — Costs and Timeline Planning

### 7.1 Cost Drivers for NB Assessment

NB assessment costs vary significantly based on:

| Factor | Lower Cost | Higher Cost |
|---|---|---|
| System complexity | Simple single-purpose system | Complex multi-component system with multiple use cases |
| Documentation readiness | Well-prepared documentation package | Incomplete docs requiring extensive NB review |
| Non-conformances | No or minor findings | Major findings requiring rework and re-assessment |
| System type | Standard AI software | Medical device AI or safety-critical system |
| NB experience | NB with prior AI Act assessment experience | First-time AI Act NB (learning curve) |
| Surveillance requirements | Annual desk-based surveillance | Frequent on-site surveillance |

**Indicative ranges** (highly variable; confirm with NB): Initial assessments for straightforward Annex III systems may range from EUR 15,000 to EUR 100,000+. Medical device AI NB assessments are typically higher. Request detailed fee proposals from at least two NBs.

### 7.2 Timeline Planning

Working backwards from your target market placement date:

| Milestone | Lead Time Before Market Placement |
|---|---|
| NB certificate received | At least 4 weeks before placement (DoC update, registration) |
| NB assessment complete (no major findings) | 3-6 months before target placement date |
| Documentation package submitted to NB | 4-8 months before target placement |
| NB selected and engaged | 5-9 months before target placement |
| Internal conformity assessment complete | 6-10 months before target placement |
| Technical documentation complete | 7-11 months before target placement |
| System development complete and tested | 8-12 months before target placement |

**Recommended approach:** Engage a Notified Body early — even before internal assessment is complete — to understand their requirements, queue times, and documentation expectations. Many NBs offer pre-assessment consultations or scoping meetings.

---

## Part 8 — Interaction with Other EU Legislation NBs

Where an AI system is a component of a product regulated under Annex I legislation, the NB assessment may be combined or coordinated:

| Scenario | Approach |
|---|---|
| AI system is a medical device (MDR) — Class IIa+ | Single NB preferred; NB must be designated under both MDR and EU AI Act. Article 11(3) permits combined technical documentation. |
| AI system in machinery (Machinery Regulation Annex IV) | Coordinate with MDR NB or separate Machinery NB; confirm dual designation |
| AI system in radio equipment (RED) | RED NB + AI Act NB; combined assessment if NB holds dual designation |
| Single combined certificate possible? | Only if NB holds designation under all applicable legislation; confirm with specific NB |

---

## Part 9 — Notified Body Engagement Tracker

| Activity | Date | Status | Notes | Owner |
|---|---|---|---|---|
| Notified Body requirement confirmed | | | | Compliance |
| NANDO database research completed | | | | Compliance |
| NB candidates shortlisted | | | | Compliance |
| NB selected and engagement letter signed | | | | Compliance |
| Documentation package prepared | | | | Technical Lead |
| Documentation submitted to NB | | | | Compliance |
| Phase 2 document review complete | | | | NB |
| Phase 3 product assessment complete | | | | NB |
| Non-conformances remediated | | | | Technical Lead |
| Certificate received | | | | NB |
| EU Declaration of Conformity updated with certificate reference | | | | Legal |
| EU database registration updated | | | | Compliance |
| First surveillance activity due | | | | Compliance |

---

## Related Documents

| Document | Reference |
|---|---|
| Conformity Assessment Checklist | 02-CONFORMITY-ASSESSMENT-CHECKLIST.md |
| Technical Documentation | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md |
| EU Declaration of Conformity | 12-EU-DECLARATION-OF-CONFORMITY.md |
| CE Marking Guide | 14-CE-MARKING-GUIDE.md |
| Quality Management System | 16-QUALITY-MANAGEMENT-SYSTEM.md |
| Master Compliance Scorecard | 19-MASTER-COMPLIANCE-SCORECARD.md |
| NANDO Database | https://ec.europa.eu/growth/tools-databases/nando/ |
| EU AI Office | https://digital-strategy.ec.europa.eu/en/policies/ai-office |

---

*Part of the EU AI Act Compliance Toolkit*

*This document does not constitute legal advice. Seek qualified legal counsel for binding compliance determinations. Notified Body selection and engagement decisions have significant legal and commercial implications and should be made with expert guidance.*
