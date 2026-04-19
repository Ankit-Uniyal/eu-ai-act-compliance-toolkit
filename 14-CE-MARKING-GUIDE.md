# 14 -- CE Marking Guide for AI Systems

**EU AI Act Reference:** Article 16(h) | Article 48 | Article 49 | Annex I
**Applies to:** Providers of High-Risk AI Systems embedded in or constituting Annex I products
**Last Updated:** April 2026

---

## Purpose

CE marking is the visible declaration that a product meets all applicable EU legislation requirements. For AI systems, CE marking requirements are closely tied to the product categories listed in **Annex I** of the EU AI Act.

This guide clarifies when CE marking is required, how it interacts with existing product legislation, and what steps are needed to affix it correctly.

---

## Part 1 -- Does Your AI System Require CE Marking?

**Step 1:** Is the AI system a safety component of, or itself, a product covered by Annex I EU harmonisation legislation?

- If NO: The AI system is classified under Article 6(2) / Annex III (standalone high-risk). CE marking typically follows the product legislation path if embedded in a CE-marked product. Standalone software AI systems deployed via API may not require a physical CE mark. Document your rationale.
- If YES: Proceed to Step 2.

**Step 2:** Does the Annex I legislation covering the product require CE marking?

| Annex I Product Legislation | CE Marking Required? |
|---|---|
| Machinery Regulation (EU) 2023/1230 | Yes |
| Medical Devices Regulation (EU) 2017/745 (MDR) | Yes |
| In Vitro Diagnostic Devices Regulation (EU) 2017/746 (IVDR) | Yes |
| Radio Equipment Directive 2014/53/EU (RED) | Yes |
| Automotive (EU) 2018/858 type approval | Type approval mark (not standard CE) |
| Civil aviation (EASA regulations) | EASA airworthiness mark (not CE) |
| Marine equipment Directive 2014/90/EU | Wheel mark (not CE) |
| General Product Safety Regulation (EU) 2023/988 | No CE mark but safety obligations apply |

**Step 3:** Has the AI system undergone conformity assessment for CE marking under the product legislation, in addition to the EU AI Act conformity assessment?

Both assessments are required where both the product legislation and the EU AI Act apply. Article 11(3) allows a single combined technical documentation where feasible.

---

## Part 2 -- CE Marking Requirements Under the EU AI Act

### 2.1 When Does the EU AI Act Itself Require CE Marking?

| Scenario | CE Marking Under EU AI Act? |
|---|---|
| AI system sold as standalone hardware device | Yes (if high-risk and Annex I product) |
| AI system embedded in a CE-marked product (e.g. medical device, machinery) | Yes -- CE marking covers the combined product |
| AI system provided purely as software (SaaS / API) | Generally no physical CE mark; check product legislation |
| AI system embedded in a product NOT requiring CE marking | Generally not required; document rationale |

### 2.2 CE Marking Rules (Article 48)

| Rule | Detail |
|---|---|
| Minimum height | 5mm (unless product dimensions require smaller) |
| Proportionality | Must be proportional -- no distortion of CE symbol |
| Visibility | Must be visible, legible, and indelible |
| Placement | On the AI system, its packaging, or accompanying document |
| No false CE marking | Affixing CE marking on non-conformant systems is a regulatory offence |
| No misleading marks | Other marks must not reduce visibility or legibility of CE mark |

### 2.3 Notified Body Number Requirement

When a Notified Body has been involved in the conformity assessment, the Notified Body's four-digit identification number must be affixed next to or below the CE marking.

Format: CE [XXXX] where XXXX is the Notified Body number.

---

## Part 3 -- CE Marking Procedure

### 3.1 Pre-Marking Checklist

| Step | Requirement | Status | Reference |
|---|---|---|---|
| 1 | Confirm product is covered by EU harmonisation legislation requiring CE marking | [ ] Done | Annex I EU AI Act |
| 2 | Complete conformity assessment under all applicable legislation | [ ] Done | 02-CONFORMITY-ASSESSMENT-CHECKLIST.md |
| 3 | Compile technical documentation (Annex IV) | [ ] Done | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md |
| 4 | Draw up EU Declaration of Conformity (Article 47) | [ ] Done | 12-EU-DECLARATION-OF-CONFORMITY.md |
| 5 | Register system in EU AI Act database (Article 71) | [ ] Done | 05-AI-SYSTEM-REGISTER.md |
| 6 | Obtain Notified Body certificate (where required) | [ ] Done / N/A | 02-CONFORMITY-ASSESSMENT-CHECKLIST.md |
| 7 | Confirm CE mark format meets Article 48 requirements | [ ] Done | This document |
| 8 | Identify location(s) for CE mark affixation | [ ] Done | See Section 3.2 |

### 3.2 CE Marking Affixation Decision

| Product Type | Recommended Affixation Location |
|---|---|
| Physical hardware with AI embedded | Directly on product housing |
| Product with packaging | Product + packaging |
| Standalone software product (digital delivery) | User interface, documentation, and download confirmation |
| Software embedded in physical product | On the host product + documentation |
| Small product with insufficient space | On packaging and/or accompanying document |

### 3.3 Combined CE Marking (Multiple Legislation)

Where an AI system is subject to multiple pieces of EU legislation each requiring CE marking:

- A single CE mark is affixed -- it covers conformity with all applicable legislation
- The EU Declaration of Conformity must reference all applicable legislation
- Technical documentation should address all legislative requirements
- Example: A medical imaging AI system may need CE marking under both MDR and the EU AI Act

---

## Part 4 -- Interaction with Sector-Specific Product Legislation

### 4.1 Medical Devices and IVDs (MDR / IVDR)

AI systems qualifying as medical devices (e.g. AI diagnostic software) must comply with MDR in addition to the EU AI Act. Both apply simultaneously.

| Issue | Guidance |
|---|---|
| Which regulation takes precedence? | Both apply -- MDR defines device class and conformity route; EU AI Act adds AI-specific requirements |
| Can conformity assessments be combined? | Article 11(3) allows combined technical documentation |
| Notified Body involvement | MDR requires Notified Body for Class IIa and above; EU AI Act may also require NB for certain biometric AI |
| CE marking | Single CE mark covers both; DoC references both MDR and EU AI Act |

### 4.2 Machinery (Machinery Regulation 2023/1230)

AI systems embedded in machinery or constituting machine safety components must comply with both the Machinery Regulation and the EU AI Act.

| Issue | Guidance |
|---|---|
| Which systems are affected? | AI controlling safety functions (e.g. emergency stop, speed limiting, guarding) |
| Self-certification vs. Notified Body | Annex IV machinery requires Notified Body; others may self-certify |
| CE marking | Machinery CE marking covers the complete machine including AI components |

### 4.3 Automotive and Transport

AI systems in vehicles are subject to type approval frameworks rather than standard CE marking. EU AI Act obligations still apply to AI safety components in vehicles. Contact relevant type approval authorities for specific guidance.

### 4.4 General Product Safety

For consumer AI products not covered by specific sector legislation, the General Product Safety Regulation (GPSR, EU 2023/988) may apply. GPSR does not require CE marking but imposes safety obligations.

---

## Part 5 -- CE Marking Compliance Tracker

| System / Product | Annex I Legislation | CE Marking Required? | Notified Body? | NB Number | CE Mark Location | Date Affixed | DoC Reference |
|---|---|---|---|---|---|---|---|
| | | Yes / No | Yes / No | | | | |

---

## Part 6 -- Market Surveillance and Enforcement

Market surveillance authorities (MSAs) can:
- Request to see technical documentation and Declaration of Conformity
- Require CE marking to be corrected or removed if affixed incorrectly
- Order withdrawal or recall of non-conformant products
- Impose fines for false or missing CE marking

**False CE marking** is a regulatory offence in all EU Member States and can result in product withdrawal, significant fines, criminal liability in some jurisdictions, and reputational damage.

**Non-EU providers** placing CE-marked products on the EU market must designate an EU Authorised Representative (see 13-AUTHORISED-REPRESENTATIVE.md) and ensure the Importer verifies CE marking and DoC (see 15-IMPORTER-DISTRIBUTOR-CHECKLISTS.md).

---

## Related Documents

| Document | Reference |
|---|---|
| Conformity Assessment Checklist | 02-CONFORMITY-ASSESSMENT-CHECKLIST.md |
| Technical Documentation | 04-TECHNICAL-DOCUMENTATION-TEMPLATE.md |
| EU Declaration of Conformity | 12-EU-DECLARATION-OF-CONFORMITY.md |
| Authorised Representative | 13-AUTHORISED-REPRESENTATIVE.md |
| Importer / Distributor Checklists | 15-IMPORTER-DISTRIBUTOR-CHECKLISTS.md |
| NANDO database (Notified Bodies) | https://ec.europa.eu/growth/tools-databases/nando/ |

---

*Part of the EU AI Act Compliance Toolkit*
