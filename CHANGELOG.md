# Changelog

All notable changes to the EU AI Act Compliance Toolkit are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Toolkit versioning: MAJOR.MINOR.PATCH
Regulatory baseline: Regulation (EU) 2024/1689 as entered into force 1 August 2024. This toolkit will be updated as delegated acts, implementing acts, and EU AI Office guidance documents are published.

---

## [3.2.0] - 2026-04-29

### Added

**25-PROHIBITED-PRACTICES-ASSESSMENT.md** — New standalone Article 5 Prohibited Practices Assessment Checklist. Closes a critical coverage gap: the eight prohibited practices have been enforceable since 2 February 2025 and carry the highest fines in the Regulation (up to €35 million / 7% of global turnover). Covers: preliminary scoping questions; individual assessments for all eight prohibitions (subliminal techniques, vulnerable group exploitation, social scoring by public authorities, real-time remote biometric identification, biometric categorisation by protected characteristics, emotion recognition in workplace/education, untargeted facial image scraping, and predictive individual criminal profiling); exemption tests for Prohibitions 4 and 6; scope boundary notes distinguishing prohibited from high-risk; clearance certificate with four-party sign-off; and post-clearance obligations table linking to Doc 01.

**26-RISK-MANAGEMENT-SYSTEM.md** — New standalone Article 9 Risk Management System template. Article 9 is one of the most frequently audited requirements for high-risk AI systems but was previously covered only partially within Doc 02 (Conformity Assessment) and Doc 04 (Technical Documentation). This document provides a complete, standalone RMS framework distinct from the QMS (Article 17, Doc 16). Covers: RMS governance structure and scope; Step 1 — risk identification across six categories (technical performance, data and bias, human oversight, security/adversarial, fundamental rights, operational) plus reasonably foreseeable misuse; Step 2 — risk estimation with likelihood/severity/breadth scales and risk register; Step 3 — risk evaluation against acceptable thresholds (four-level policy with approval requirements); Step 4 — risk treatment plans by category with standard treatment measures library; Step 5 — residual risk assessment and acceptance with aggregate sign-off; Step 6 — testing and validation including pre-market testing, bias testing by protected characteristic, and performance threshold table; Step 7 — post-market monitoring integration with update triggers and RMS update log; and Article 9 completeness checklist with Annex IV cross-reference map.

**27-GPAI-SYSTEMIC-RISK-COMPLIANCE.md** — New GPAI Systemic Risk Compliance Guide for Articles 55-56. Supplements Doc 11 (GPAI baseline obligations) with the additional obligations triggered when a GPAI model meets the systemic risk threshold (≥ 10²⁵ FLOPs or EU AI Office designation). Covers: systemic risk classification determination; rebuttable presumption process; Obligation 1 — adversarial testing/red-teaming with eight risk domain coverage checklist (CBRN uplift, cyberoffensive capabilities, critical infrastructure attack, disinformation at scale, autonomous harmful action, safety bypass, bias at scale, privacy violation at scale) and findings register; Obligation 2 — enhanced incident reporting with systemic risk incident categories and timelines (including parallel GDPR/AI Act reporting for personal data breach); Obligation 3 — cybersecurity measures including risk assessment table and 10-control minimum standard; Obligation 4 — EU AI Office cooperation including five-step internal response process; Article 56 powers awareness checklist; post-training risk mitigation measures register (six measure types); downstream provider management controls; annual review governance; and voluntary codes of practice participation tracker.

**28-MARKET-SURVEILLANCE-RESPONSE.md** — New Market Surveillance and Regulatory Response Procedure. Addresses the practical "what happens when the regulator comes knocking" gap that existing toolkit documents did not cover. Covers: regulatory landscape (national MSAs, EU AI Office, DPAs, sectoral regulators) with competent authority contact register; comprehensive document retention schedule (12 document types with Article-specific retention periods, including the critical 10-year obligation for technical documentation and QMS records); deployer-specific retention obligations; annual document retention audit; regulatory readiness assessment with 16-item self-assessment across three categories; five-step first response protocol (Day 0 authentication through sign-off); on-site inspection protocol with guidance on cooperation, note-taking, and rights; regulatory interaction log template; corrective action response procedure; Article 99 administrative fines reference table (€35m/7%; €15m/3%; €7.5m/1.5%); appeals and judicial remedies overview; and 15-item enforcement readiness checklist with scoring.

### Changed

**README.md** — Updated to v3.2.0. Added Docs 25-28 to document table. Updated routing table to include new "Preparing for market surveillance inspection" row and updated all relevant rows to include Doc 25 (prohibited practices) as Step 1 for all providers and deployers. Updated "How to Use" section: added Step 1 (prohibited practices screen) before risk classification, added RMS step for high-risk providers, added market surveillance preparation to ongoing processes. Added RMS and MSA to Key Definitions.

### Regulatory Coverage Added in v3.2.0

| Coverage Added | Reference | Document |
|---|---|---|
| All 8 Article 5 prohibited practices with exemption tests | Art. 5(1)(a)-(h), Art. 5(2)-(7), Recitals 40-49 | Document 25 |
| Article 9 Risk Management System — complete standalone template | Art. 9 | Document 26 |
| GPAI systemic risk obligations — adversarial testing, incident reporting, cybersecurity, EU AI Office cooperation | Arts. 51, 55-56, Annex XIII | Document 27 |
| Market surveillance authorities, enforcement powers, document retention, regulatory response | Arts. 74-99, Art. 18 | Document 28 |

---

## [3.1.0] - 2026-04-29

### Fixed

**04-TECHNICAL-DOCUMENTATION-TEMPLATE.md** — Annex IV Section 8 (Post-Market Monitoring) was a one-line cross-reference placeholder. Replaced with full embedded PMM template including: performance monitoring approach (activities, method, frequency, thresholds), data collection from deployers (Article 72(3)), trigger criteria for reactive review (6 named triggers), corrective action 6-step process, and PMM record-keeping table with 10-year retention requirements per Article 18.

**16-QUALITY-MANAGEMENT-SYSTEM.md** — Added Part 3A: Article 17(1) Sub-Paragraph Compliance Map — explicit table mapping each Article 17(1)(a)-(g) sub-paragraph to QMS sections and evidence documents for conformity assessment reviewers. Added Part 3B: ISO/IEC 42001:2023 Gap Mapping — 11-row table mapping each AI Act Article 17(1) requirement to the corresponding ISO/IEC 42001:2023 clause, identifying gaps and adoption approach options (Full / Partial / Reference only).

**18-GDPR-AI-ACT-INTERSECTION.md** — Corrected a material error in Section 2.1 (Data Governance Joint Compliance Map): GDPR Art. 5(1)(f) (integrity and confidentiality / security) was incorrectly mapped to the "bias examined" row. Corrected to Art. 5(1)(d) (accuracy) + Recital 71 GDPR (non-discrimination in profiling) for the bias row. Added a separate row for data integrity/security correctly mapped to Art. 5(1)(f). Updated bias audit reference in the joint compliance checklist to "Arts. 5(1)(d), 9; Recital 71".

**19-MASTER-COMPLIANCE-SCORECARD.md** — Corrected item count arithmetic: the scorecard contained 118 checkable requirements across 11 sections (not 100 as previously stated in Part 14). Updated summary table totals to show accurate section counts (Part 3: 10; Part 4: 35; Part 5: 12; Part 6: 8; Part 7: 6; Part 8: 4; Part 9: 8; Part 10: 7; Part 11: 5; Part 12: 5; Part 13: 8; Total: 118). Added per-section totals throughout the scorecard. Added explanatory note in Part 14.1. Improved table structure with explicit column headers throughout.

**20-NOTIFIED-BODY-ENGAGEMENT-GUIDE.md** — Corrected imprecise Article reference in Section 1.2, Circumstance 2: "Article 5(1)(h)" was cited for real-time remote biometric identification systems. Per the enacted Regulation (EU) 2024/1689, the conditions and derogations for real-time remote biometric identification in publicly accessible spaces for law enforcement are in Article 5(2)-(7). Updated to cite "Article 5(2)-(7)" with contextual explanation.

### Added

**21-LEGITIMATE-INTEREST-ASSESSMENT.md** — New GDPR Art. 6(1)(f) Legitimate Interest Assessment template for AI data processing contexts. Covers: three-part LIA test (purpose, necessity, balancing), AI-specific risk factors, safeguards assessment, AI processing context table for common activities (training, deployment, bias monitoring, logging), special category data legal basis, ongoing review requirements, and relationship to AI Act Art. 10 data governance. Includes LIA tracker and required actions checklist.

**22-WORKER-INFORMATION-NOTICE.md** — New Article 26(7) worker information notice template. Covers: scope trigger assessment, pre-deployment information procedure with timeline, model notice text (plain-language description, safeguards, worker rights, contact details), national law assessment table (Germany BetrVG, France Labour Code, Netherlands WOR, Sweden MBL, EU EWC Directive), information and consultation tracker, and post-deployment review checklist.

**23-ANNEX-VII-ASSESSMENT-CHECKLIST.md** — New Annex VII provider readiness checklist mapping what a Notified Body actually reviews against required evidence. Covers: Phase 1 QMS assessment (15 items covering all Art. 17(1)(a)-(g) requirements), Phase 2 technical documentation assessment (32 items across all 8 Annex IV sections), Phase 3 substantive requirements assessment (Articles 9, 10, 14, 15, 13). Includes traffic light readiness tracker and estimated NB finding risk assessment.

**24-WORKED-EXAMPLE-CREDIT-SCORING-AI.md** — Second end-to-end worked example covering a fictional credit scoring AI (CreditScore-AI v2.3, RetailBank NV as deployer, FinTech Solutions BV as provider). Covers Annex III Area 5(b) classification, Article 6(3) exclusion assessment, provider/deployer role split, risk management (6 risks identified), data governance (training data summary, bias audit by protected characteristic), GDPR joint compliance (DPIA, Art. 22, LIA), human oversight design, transparency (Art. 13(3) instructions mapped), conformity assessment (internal; CONFORMANT), EU database registration, PMM plan summary, AI literacy requirements, and lessons learned table.

### Changed

**README.md** — Updated to v3.1.0. Added "Which Documents Apply to Me?" routing table (12 role-based rows). Added Doc 24 to Worked Examples table. Updated scorecard item count to 118. Updated v3.1.0 document table (Docs 21-24). Added LIA to Key Definitions.

### Regulatory Coverage Added in v3.1.0

| Coverage Added | Reference | Document |
|---|---|---|
| GDPR Art. 6(1)(f) legitimate interests three-part test for AI processing | GDPR Art. 6(1)(f); Recital 47; AI Act Art. 10 | Document 21 |
| Worker information obligation before workplace AI deployment | AI Act Art. 26(7) | Document 22 |
| Notified Body assessment criteria evidence mapping | Annex VII; Arts. 43-44 | Document 23 |
| Credit scoring AI system worked example (Annex III Area 5) | All Articles | Document 24 |

---

## [3.0.0] - 2026-04-29

### Added

**16-QUALITY-MANAGEMENT-SYSTEM.md** — New standalone QMS template for Article 17 compliance. Fills a critical gap: Article 17 was referenced in Document 02 (conformity assessment) but had no standalone template. Covers: QMS scope and quality policy statement, organisation and responsibilities (Article 17(1)(e)), compliance strategy mapped to all Articles 9-17/72/73, design and development lifecycle with 11-stage quality gates, change management and substantial modification assessment, data governance procedures (Article 17(1)(c)), technical documentation lifecycle, post-market monitoring integration (Article 17(1)(f)), incident reporting integration (Article 17(1)(g)), internal audit schedule, annual management review, CAPA log, and complete document index linking all 20 toolkit documents.

**17-AI-LITERACY-COMPETENCY-FRAMEWORK.md** — New framework for Article 4 AI literacy obligations and Article 14(3) human oversight competency. Covers: regulatory basis (Articles 4, 14(3), 26(2)), role categories (Executive/Board, AI Governance, Technical, Product, Oversight Persons, End Users, Procurement/Legal), four-level competency model (Awareness L1 to Expert L4), 10-module training programme with role-based requirements, self-assessment tool with scored statements at each level (L1-L4), gap analysis and closure planning, training delivery and individual records log, Article 14(3) oversight person certification record, programme governance and AI literacy metrics dashboard.

**18-GDPR-AI-ACT-INTERSECTION.md** — New systematic mapping of GDPR and EU AI Act overlapping obligations. Addresses one of the most commonly missed compliance areas for real deployments. Covers: regulatory relationship and scope overlap, data governance joint compliance (Article 10 AI Act / Article 5 GDPR), special category data requirements (GDPR Article 9 / AI Act Article 10(5)), automated decision-making (GDPR Article 22 / AI Act Article 14), transparency and disclosure obligations map, DPIA and FRIA comparison with combined assessment approach, lawful basis for all AI-related processing activities, data subject rights in AI context, DPO role in AI Act compliance, dual incident reporting (MSA and DPA), common conflict points and resolution guidance (data minimisation vs. representativeness; retention vs. storage limitation; explainability vs. trade secrets), joint compliance checklist.

**19-MASTER-COMPLIANCE-SCORECARD.md** — New consolidated 100-item gap analysis covering all 20 toolkit documents and the full EU AI Act obligation set. Designed as the entry point for organisations beginning their compliance programme, as a progress tracker, and as a board-level reporting tool. Covers: AI system portfolio summary with risk tier breakdown, scoring methodology (DONE/IN PROGRESS/GAP/N/A/PENDING) with P1-P4 priority codes, 11 compliance sections (risk classification, pre-market high-risk requirements, conformity and placement, deployer obligations, FRIA, limited-risk transparency, GPAI, post-market and incidents, supply chain, AI literacy, GDPR intersection), consolidated gap summary with P1/P2/P3 action tables, executive dashboard with traffic light summary.

**20-NOTIFIED-BODY-ENGAGEMENT-GUIDE.md** — New practical guide for the third-party conformity assessment process. Covers: when a Notified Body is mandatory vs. optional (decision table covering Annex I products, biometric systems, Annex III standalone systems), what a Notified Body does and does not do, NB independence requirements (Article 44), how to find NBs via NANDO database, selection criteria and shortlisting register, pre-assessment readiness checklist, documentation package requirements, five-phase assessment process with typical timelines (3-6 months for straightforward systems), finding types (observation/minor/major/critical) and provider responses, certificate maintenance and surveillance obligations, ongoing notification triggers, cost drivers and indicative timeline planning (working backwards from market placement date), interaction with sector-specific NBs (MDR, Machinery), engagement tracker.

### Changed

**README.md** — Updated to v3.0.0. Added new v3.0 documents table (Documents 16-20). Revised "How to Use" section with 8-step structured onboarding path starting from Master Compliance Scorecard as the entry point. Updated toolkit description to reflect new additions.

### Regulatory Coverage Added

| Coverage Added | Article | Document |
|---|---|---|
| Quality Management System | Article 17 | Document 16 |
| AI literacy obligations | Article 4 | Document 17 |
| Oversight person competency | Article 14(3) | Document 17 |
| GDPR / AI Act intersection | Articles 9, 10, 13, 26, 27 + GDPR Arts. 5, 6, 9, 22, 35 | Document 18 |
| Consolidated compliance gap analysis | All Articles | Document 19 |
| Notified Body third-party assessment | Articles 43-46, Annex VII | Document 20 |

---

## [2.0.0] - 2026-04-19

### Added

**11-GPAI-TECHNICAL-DOCUMENTATION.md** -- New template for GPAI model providers. Covers Annex XI (standard GPAI) and Annex XII (systemic risk GPAI, >10^25 FLOPs). Fills critical gap: GPAI providers have entirely different obligations from Annex IV. Covers: model identity, training data, copyright compliance (Art. 53(1)(c)), training data summary for publication (Art. 53(1)(d)), adversarial testing / red-teaming (Art. 55(1)(a)), incident reporting to EU AI Office (Art. 55(1)(b)), cybersecurity (Art. 55(1)(c)), energy efficiency (Art. 55(1)(d)), and Codes of Practice (Art. 56).

**12-EU-DECLARATION-OF-CONFORMITY.md** -- New Article 47 / Annex V template. Full DoC template with provider information, system description, conformity statement mapping all Articles 9-17 and 72, conformity assessment procedure (Annex VI or VII), harmonised standards table, CE marking section, and signature blocks for provider and EU Authorised Representative. Includes revision log and update triggers.

**13-AUTHORISED-REPRESENTATIVE.md** -- New Article 22 designation agreement template. Covers: when an Authorised Representative is required, provider and AR details, scope of mandate (systems and geography), mandatory obligations per Article 22(3), day-to-day activities with SLAs, provider obligations to AR, liability framework, termination procedures, and mandate register.

**14-CE-MARKING-GUIDE.md** -- New guide for CE marking requirements. Covers: decision tree for when CE marking is required, interaction with Annex I product legislation (MDR, Machinery Regulation, IVDR, RED), CE marking format rules (Article 48), Notified Body number requirement, combined CE marking for multiple legislation, sector-specific guidance (medical devices, machinery, automotive), and market surveillance enforcement.

**15-IMPORTER-DISTRIBUTOR-CHECKLISTS.md** -- New dedicated checklists for Importers (Article 23) and Distributors (Article 24). Covers: pre-market verification, CE marking verification, DoC verification, AR verification, instruction language requirements, risk assessment, storage/transport conditions, identity marking requirements, record-keeping for 10 years, ongoing monitoring obligations, and non-conformance log. Includes Article 25 provider-becoming trigger table and supply chain due diligence register.

**WORKED-EXAMPLE-HR-SCREENING-SYSTEM.md** -- Completed worked example for a fictional CV screening AI system (TalentFilter Pro, HireRight GmbH).

**CHANGELOG.md** -- This file. Toolkit-level versioning and regulatory update tracking.

### Changed

**scripts/risk_classifier.py** upgraded to v2.0: Article 6(3) exclusion logic via structured CSV fields; dedicated 'prohibited_practice' CSV field; warning system for keyword-matched prohibited practices; GPAI model flag references Document 11; disclaimer: tool output is a triage aid.

### Regulatory Coverage Added

| Coverage Added | Article | Document |
|---|---|---|
| Authorised Representative designation | Article 22 | Document 13 |
| Importer obligations | Article 23 | Document 15 |
| Distributor obligations | Article 24 | Document 15 |
| EU Declaration of Conformity | Article 47 / Annex V | Document 12 |
| CE Marking requirements | Article 48 | Document 14 |
| GPAI and systemic risk documentation | Articles 51, 53-56, Annexes XI, XII | Document 11 |

---

## [1.0.0] - 2026-04-11

### Added (Initial Release)

**01-RISK-CLASSIFICATION-GUIDE.md** -- Four-tier risk classification framework. Articles 5, 6, 50. Annexes I, III. Decision tree. Risk register entry template.

**02-CONFORMITY-ASSESSMENT-CHECKLIST.md** -- Pre-market conformity assessment. Articles 9-15, 17, 43-48, Annex IV. Eight sections with PASS/FAIL/PARTIAL status.

**03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md** -- FRIA template. Article 27. Full EU Charter of Fundamental Rights assessment matrix (Arts. 1-48). Bias assessment, human oversight and redress, consultation, four-outcome decision.

**04-TECHNICAL-DOCUMENTATION-TEMPLATE.md** -- Annex IV documentation. Article 11. Eight-section structure matching Annex IV exactly.

**05-AI-SYSTEM-REGISTER.md** -- Organisational AI inventory. Articles 49, 71, 16(d), 26(6). Compliance status dashboard. Decommissioned systems log.

**06-TRANSPARENCY-OBLIGATIONS.md** -- Article 50 / Article 53 checklist. Chatbots, emotion recognition, deepfakes, GPAI. C2PA and IPTC labelling guidance.

**07-HUMAN-OVERSIGHT-FRAMEWORK.md** -- Article 14 framework. Oversight roles, competency requirements, operational controls, automation bias mitigation, decision workflow classification, metrics.

**08-INCIDENT-REPORTING-PROCEDURE.md** -- Article 73 / Article 26(5) procedure. P1-P4 severity classification. Four-phase response (0-2h, 2-48h, 72h notification, full). Regulatory notification template.

**09-POST-MARKET-MONITORING-PLAN.md** -- Article 72 plan template. Data sources, logging requirements, performance metrics, monitoring schedule, substantial modification assessment (Article 25), corrective actions.

**10-PROVIDER-DEPLOYER-RESPONSIBILITIES.md** -- Articles 16-27 obligations matrix. Full provider, deployer, importer, and distributor obligation tables. Article 25 provider-becoming trigger table. Obligation tracker.

**scripts/risk_classifier.py v1.0** -- CLI risk classifier. CSV-driven, Python stdlib only. Article 5 keyword detection, Annex I and Annex III classification.

**scripts/sample_ai_inventory.csv** -- 15-system sample inventory covering all risk tiers.

**scripts/README.md** -- Documentation for GRC engineering automation scripts.

---

## Planned Updates

The following updates are planned as EU AI Act implementation guidance develops:

| Update | Trigger | Expected |
|---|---|---|
| EU AI Office GPAI Code of Practice adoption | Code of Practice finalised 2025-2026 | TBC |
| Delegated acts for Article 6(2) Annex III update | EU Commission adoption | TBC |
| Common specifications for high-risk AI | CEN/CENELEC standards published | TBC |
| EU AI Act database operational details | EU AI Office announcement 2026 | 2026 |
| Article 6(3) exclusion guidance | EU AI Office guidance | TBC |
| FRIA scope clarification | EU AI Office guidance | TBC |
| National MSA contact directory | Maintained separately | Ongoing |
| Worked examples for additional system types | Community contributions / v4.0 | TBC |

## How to Check for Updates

- Watch this repository for releases and commits
- Monitor the EU AI Office website: https://digital-strategy.ec.europa.eu/en/policies/ai-office
- Monitor EUR-Lex for delegated and implementing acts: https://eur-lex.europa.eu
- Review NANDO database for Notified Body updates: https://ec.europa.eu/growth/tools-databases/nando/

---

## Disclaimer

This toolkit is provided for informational and educational purposes. It does not constitute legal advice. Always consult qualified legal counsel for compliance decisions. The toolkit maintainer is not liable for compliance outcomes based on use of this toolkit.

*Part of the EU AI Act Compliance Toolkit*
