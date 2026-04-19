# Changelog

All notable changes to the EU AI Act Compliance Toolkit are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Toolkit versioning: MAJOR.MINOR.PATCH

**Regulatory baseline:** Regulation (EU) 2024/1689 as entered into force 1 August 2024.
This toolkit will be updated as delegated acts, implementing acts, and EU AI Office
guidance documents are published.

---

## [2.0.0] - 2026-04-19

### Added

- **11-GPAI-TECHNICAL-DOCUMENTATION.md** -- New template for GPAI model providers.
  Covers Annex XI (standard GPAI) and Annex XII (systemic risk GPAI, >10^25 FLOPs).
  Fills critical gap: GPAI providers have entirely different obligations from Annex IV.
  Covers: model identity, training data, copyright compliance (Art. 53(1)(c)),
  training data summary for publication (Art. 53(1)(d)), adversarial testing / red-teaming
  (Art. 55(1)(a)), incident reporting to EU AI Office (Art. 55(1)(b)), cybersecurity
  (Art. 55(1)(c)), energy efficiency (Art. 55(1)(d)), and Codes of Practice (Art. 56).

- **12-EU-DECLARATION-OF-CONFORMITY.md** -- New Article 47 / Annex V template.
  Full DoC template with provider information, system description, conformity statement
  mapping all Articles 9-17 and 72, conformity assessment procedure (Annex VI or VII),
  harmonised standards table, CE marking section, and signature blocks for provider
  and EU Authorised Representative. Includes revision log and update triggers.

- **13-AUTHORISED-REPRESENTATIVE.md** -- New Article 22 designation agreement template.
  Covers: when an Authorised Representative is required, provider and AR details,
  scope of mandate (systems and geography), mandatory obligations per Article 22(3),
  day-to-day activities with SLAs, provider obligations to AR, liability framework,
  termination procedures, and mandate register.

- **14-CE-MARKING-GUIDE.md** -- New guide for CE marking requirements.
  Covers: decision tree for when CE marking is required, interaction with Annex I
  product legislation (MDR, Machinery Regulation, IVDR, RED), CE marking format
  rules (Article 48), Notified Body number requirement, combined CE marking for
  multiple legislation, sector-specific guidance (medical devices, machinery, automotive),
  and market surveillance enforcement.

- **15-IMPORTER-DISTRIBUTOR-CHECKLISTS.md** -- New dedicated checklists for Importers
  (Article 23) and Distributors (Article 24). Covers: pre-market verification, CE marking
  verification, DoC verification, AR verification, instruction language requirements,
  risk assessment, storage/transport conditions, identity marking requirements,
  record-keeping for 10 years, ongoing monitoring obligations, and non-conformance log.
  Includes Article 25 provider-becoming trigger table and supply chain due diligence register.

- **WORKED-EXAMPLE-HR-SCREENING-SYSTEM.md** -- Completed worked example for a fictional
  CV screening AI system (TalentFilter Pro, HireRight GmbH). Shows how to apply all 10
  toolkit documents in sequence: risk classification, conformity assessment (including
  partial/conditional result), FRIA, technical documentation, AI system register, human
  oversight framework, and post-market monitoring. Includes key practitioner lessons.

- **CHANGELOG.md** -- This file. Toolkit-level versioning and regulatory update tracking.

### Changed

- **scripts/risk_classifier.py** upgraded to v2.0:
  - Added Article 6(3) exclusion logic via structured CSV fields
    (exclusion_narrow_task, exclusion_human_result, exclusion_no_individual, exclusion_preparatory)
  - Added dedicated 'prohibited_practice' CSV field for Article 5 detection
    (reduces reliance on brittle keyword matching)
  - Added warning system: keyword-matched prohibited practices flagged for human review
  - GPAI model flag now references new document 11-GPAI-TECHNICAL-DOCUMENTATION.md
  - Added disclaimer: tool output is a triage aid, not a legal determination
  - Added validation for missing Art. 6(3)/prohibited columns with informative warnings

### Regulatory Coverage Added

| Article | Coverage Added in v2.0 |
|---|---|
| Article 22 | Authorised Representative designation (Document 13) |
| Article 23-24 | Importer and Distributor obligations (Document 15) |
| Article 47 / Annex V | EU Declaration of Conformity (Document 12) |
| Article 48 | CE Marking requirements (Document 14) |
| Articles 51, 53-56 | GPAI and systemic risk model documentation (Document 11) |
| Annexes XI, XII | GPAI technical documentation templates (Document 11) |

---

## [1.0.0] - 2026-04-11

### Added (Initial Release)

- **01-RISK-CLASSIFICATION-GUIDE.md** -- Four-tier risk classification framework.
  Articles 5, 6, 50. Annexes I, III. Decision tree. Risk register entry template.

- **02-CONFORMITY-ASSESSMENT-CHECKLIST.md** -- Pre-market conformity assessment.
  Articles 9-15, 17, 43-48, Annex IV. Eight sections with PASS/FAIL/PARTIAL status.

- **03-FUNDAMENTAL-RIGHTS-IMPACT-ASSESSMENT.md** -- FRIA template.
  Article 27. Full EU Charter of Fundamental Rights assessment matrix (Arts. 1-48).
  Bias assessment, human oversight and redress, consultation, four-outcome decision.

- **04-TECHNICAL-DOCUMENTATION-TEMPLATE.md** -- Annex IV documentation.
  Article 11. Eight-section structure matching Annex IV exactly.

- **05-AI-SYSTEM-REGISTER.md** -- Organisational AI inventory.
  Articles 49, 71, 16(d), 26(6). Compliance status dashboard. Decommissioned systems log.

- **06-TRANSPARENCY-OBLIGATIONS.md** -- Article 50 / Article 53 checklist.
  Chatbots, emotion recognition, deepfakes, GPAI. C2PA and IPTC labelling guidance.

- **07-HUMAN-OVERSIGHT-FRAMEWORK.md** -- Article 14 framework.
  Oversight roles, competency requirements, operational controls, automation bias mitigation,
  decision workflow classification, metrics.

- **08-INCIDENT-REPORTING-PROCEDURE.md** -- Article 73 / Article 26(5) procedure.
  P1-P4 severity classification. Four-phase response (0-2h, 2-48h, 72h notification, full).
  Regulatory notification template.

- **09-POST-MARKET-MONITORING-PLAN.md** -- Article 72 plan template.
  Data sources, logging requirements, performance metrics, monitoring schedule,
  substantial modification assessment (Article 25), corrective actions.

- **10-PROVIDER-DEPLOYER-RESPONSIBILITIES.md** -- Articles 16-27 obligations matrix.
  Full provider, deployer, importer, and distributor obligation tables.
  Article 25 provider-becoming trigger table. Obligation tracker.

- **scripts/risk_classifier.py** v1.0 -- CLI risk classifier.
  CSV-driven, Python stdlib only. CI/CD integration with GitHub Actions workflow.
  Article 5 keyword detection, Annex I and Annex III classification.

- **scripts/sample_ai_inventory.csv** -- 15-system sample inventory covering all risk tiers.

- **scripts/README.md** -- Documentation for GRC engineering automation scripts.

---

## Planned Updates

The following updates are planned as EU AI Act implementation guidance develops:

| Update | Trigger | Expected |
|---|---|---|
| EU AI Office GPAI Code of Practice adoption | Code of Practice finalised | 2025-2026 |
| Delegated acts for Article 6(2) Annex III update | EU Commission adoption | TBC |
| Common specifications for high-risk AI | CEN/CENELEC standards published | TBC |
| EU AI Act database operational details | EU AI Office announcement | 2026 |
| Article 6(3) exclusion guidance | EU AI Office guidance | TBC |
| FRIA scope clarification | EU AI Office guidance | TBC |
| National MSA contact directory | Maintained separately | Ongoing |

---

## How to Check for Updates

1. Watch this repository for releases and commits
2. Monitor the EU AI Office website: https://digital-strategy.ec.europa.eu/en/policies/ai-office
3. Monitor EUR-Lex for delegated and implementing acts: https://eur-lex.europa.eu
4. Review NANDO database for Notified Body updates: https://ec.europa.eu/growth/tools-databases/nando/

---

## Disclaimer

This toolkit is provided for informational and educational purposes. It does not constitute legal advice. Always consult qualified legal counsel for compliance decisions. The toolkit maintainer is not liable for compliance outcomes based on use of this toolkit.

---

*Part of the EU AI Act Compliance Toolkit*
