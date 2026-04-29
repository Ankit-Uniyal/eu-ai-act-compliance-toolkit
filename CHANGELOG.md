# Changelog

All notable changes to the EU AI Act Compliance Toolkit are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Toolkit versioning: MAJOR.MINOR.PATCH
Regulatory baseline: Regulation (EU) 2024/1689 as entered into force 1 August 2024. This toolkit will be updated as delegated acts, implementing acts, and EU AI Office guidance documents are published.

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
