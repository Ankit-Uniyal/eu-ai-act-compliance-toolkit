# 25 — Article 5 Prohibited Practices Assessment Checklist
## EU AI Act Compliance Toolkit | v3.2.0 | April 2026
### Regulatory Reference: Article 5, Recitals 40-49 | Enforcement Date: 2 February 2025

---

## Purpose and Scope

This checklist provides a structured decision framework for determining whether an AI system, technique, or intended use falls within the **prohibited practices** established by Article 5 of Regulation (EU) 2024/1689. All eight prohibited categories have been active since **2 February 2025**.

**Who must use this document:**
- Any organisation developing or deploying an AI system that could plausibly fall within a prohibited category
- Legal and compliance teams conducting pre-launch clearance reviews
- Procurement teams evaluating third-party AI systems
- Risk management functions performing annual compliance reviews

**Critical rule:** If any prohibited practice applies to your system **without a valid exemption**, the system must not be placed on the EU market, put into service, or used in the EU. Continued use is subject to fines of up to **€35 million or 7% of global annual turnover** (Article 99(3)).

---

## Part 1 — Preliminary Scoping Questions

Answer these questions first. If all answers are NO, this checklist does not apply to your system.

| # | Scoping Question | Yes | No |
|---|---|---|---|
| S1 | Does the system use machine-learning techniques, logic- or knowledge-based approaches, or statistical methods to generate outputs such as predictions, recommendations, decisions, or content? | ☐ | ☐ |
| S2 | Is the system intended for use in the EU, placed on the EU market, or used by persons in the EU? | ☐ | ☐ |
| S3 | Does the system interact with, observe, infer about, or make decisions affecting natural persons? | ☐ | ☐ |

**If all S1–S3 = YES, continue to Part 2.**
**If any = NO, this checklist does not apply. Document your reasoning below.**

Scoping notes: _______________________________________________

---

## Part 2 — The Eight Prohibited Practice Assessments

Work through each prohibition in sequence. For each, complete the primary test. If the primary test is positive, complete the exemption test before concluding.

---

### Prohibition 1 — Subliminal, Manipulative, or Deceptive Techniques
**Regulatory Reference:** Article 5(1)(a)

**What is prohibited:** Deploying AI techniques that operate below the threshold of conscious awareness, exploit psychological weaknesses or biases, or use deceptive techniques in a way that materially distorts a person's behaviour — causing or likely to cause harm.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 1.1 | Does the system present stimuli at speeds or intensities outside conscious perception (subliminal audio, visual, or haptic)? | ☐ | ☐ |
| 1.2 | Does the system exploit known cognitive biases (anchoring, scarcity, social proof) to drive behaviour beyond what the person would choose with full information? | ☐ | ☐ |
| 1.3 | Does the system use techniques designed to create false impressions of urgency, scarcity, or social consensus? | ☐ | ☐ |
| 1.4 | Does the system use dark patterns, deceptive framing, or personalised persuasion in a way that bypasses rational agency? | ☐ | ☐ |
| 1.5 | Could the technique cause the person to take an action or hold a belief they would not otherwise have taken or held, resulting in harm (financial, physical, psychological, reputational)? | ☐ | ☐ |

**Prohibition 1 triggered if:** Any 1.1–1.5 = YES **AND** harm (actual or likely) is present.

**Prohibition 1 triggered:** ☐ YES ☐ NO

**No exemptions exist for Prohibition 1.** If triggered, the system is prohibited.

**Conclusion — Prohibition 1:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 2 — Exploitation of Vulnerable Groups
**Regulatory Reference:** Article 5(1)(b)

**What is prohibited:** AI systems that exploit specific vulnerabilities of a group of persons due to their age, disability, or social or economic circumstances, with the objective or effect of materially distorting their behaviour in a harmful way.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 2.1 | Is the system specifically targeted at or primarily used with children under 18? | ☐ | ☐ |
| 2.2 | Is the system used in contexts where persons with cognitive impairments, mental health conditions, or severe social deprivation are a primary user group? | ☐ | ☐ |
| 2.3 | Does the system personalise its behaviour based on detected vulnerability signals (emotional state, economic stress, loneliness, grief)? | ☐ | ☐ |
| 2.4 | Does the system use vulnerability-exploiting techniques to drive purchasing decisions, data sharing, behavioural change, or political views? | ☐ | ☐ |
| 2.5 | Could the technique cause persons to take actions harmful to their physical, financial, psychological, or social wellbeing? | ☐ | ☐ |

**Prohibition 2 triggered if:** Any 2.1–2.5 = YES **AND** harm (actual or likely) is present.

**Prohibition 2 triggered:** ☐ YES ☐ NO

**No exemptions exist for Prohibition 2.** If triggered, the system is prohibited.

**Conclusion — Prohibition 2:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 3 — Social Scoring by Public Authorities
**Regulatory Reference:** Article 5(1)(c)

**What is prohibited:** AI systems used by public authorities (or on their behalf) to evaluate or classify natural persons based on social behaviour or personal characteristics, resulting in detrimental treatment in unrelated social contexts or treatment disproportionate to the conduct.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 3.1 | Is the system operated by or on behalf of a public authority (government, law enforcement, public administration, state-owned entity)? | ☐ | ☐ |
| 3.2 | Does the system assign scores, ratings, or classifications to persons based on their behaviour, social relationships, or personal characteristics? | ☐ | ☐ |
| 3.3 | Are those scores used to determine access to services, opportunities, or resources in contexts unrelated to where the data was collected? | ☐ | ☐ |
| 3.4 | Does the system result in disproportionate or unjustified adverse treatment relative to the conduct being evaluated? | ☐ | ☐ |

**Prohibition 3 triggered if:** 3.1 = YES **AND** any of 3.2–3.4 = YES.

**Prohibition 3 triggered:** ☐ YES ☐ NO

**No exemptions exist for Prohibition 3.** If triggered, the system is prohibited.

**Note:** Private-sector credit scoring that complies with GDPR and applicable financial services law is **not** covered by Prohibition 3 (it falls under High Risk — Annex III, Area 5). See Doc 24 for the credit scoring worked example.

**Conclusion — Prohibition 3:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 4 — Real-Time Remote Biometric Identification in Public Spaces
**Regulatory Reference:** Article 5(1)(d) and Article 5(2)–(7)

**What is prohibited:** The use of real-time remote biometric identification (RBI) systems in publicly accessible spaces for law enforcement purposes.

**Definitions:**
- **Real-time:** biometric data is captured and compared without significant delay
- **Remote:** persons are not physically present at the point of identification
- **Publicly accessible space:** any physical location open to the public (streets, transport hubs, shopping centres, public buildings)
- **Law enforcement purpose:** prevention, investigation, detection, or prosecution of criminal offences, or execution of criminal penalties

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 4.1 | Is the system a biometric identification system (matches individuals against a reference database using physical, physiological, or behavioural characteristics)? | ☐ | ☐ |
| 4.2 | Does the system operate in real-time (live video feed or near-live processing with less than a few seconds delay)? | ☐ | ☐ |
| 4.3 | Is the system deployed in a publicly accessible space? | ☐ | ☐ |
| 4.4 | Is the deployment purpose related to law enforcement (prevention, detection, investigation, or prosecution of criminal offences)? | ☐ | ☐ |

**Prohibition 4 triggered if:** All of 4.1–4.4 = YES.

**Prohibition 4 triggered:** ☐ YES ☐ NO

If triggered, proceed to the **Exemption Test** below before concluding.

#### Exemption Test — Article 5(2) Permitted Exceptions

Real-time RBI for law enforcement is permitted **only** in the following strictly defined cases, subject to authorisation and conditions:

| Exemption | Conditions | Applicable? |
|---|---|---|
| **E4-A: Targeted search for missing persons or victims of trafficking** (Art. 5(2)(a)) | System is used to find specific named missing persons or victims of human trafficking or sexual exploitation | ☐ YES ☐ NO |
| **E4-B: Prevention of specific terrorist threat** (Art. 5(2)(b)) | Specific, substantial, and imminent threat of a terrorist attack; prior judicial or independent administrative authorisation obtained; deployment limited in time and geography | ☐ YES ☐ NO |
| **E4-C: Identification of suspect in serious crime** (Art. 5(2)(c)) | Offence punishable by at least 4 years' custodial sentence; prior judicial or independent administrative authorisation obtained; deployment proportionate and necessary | ☐ YES ☐ NO |

**Additional mandatory conditions for all exemptions (Article 5(3)–(7)):**

| Condition | Met? |
|---|---|
| Prior authorisation obtained from judicial authority or independent administrative body (except duly justified urgent cases, with retroactive authorisation within 24 hours) | ☐ YES ☐ NO |
| Deployment limited to the specific time period and geographic area authorised | ☐ YES ☐ NO |
| System registered in the EU database before deployment | ☐ YES ☐ NO |
| Fundamental rights impact assessment completed | ☐ YES ☐ NO |
| Human oversight mechanism in place | ☐ YES ☐ NO |
| Non-discrimination safeguards implemented | ☐ YES ☐ NO |

**Conclusion — Prohibition 4:**
- ☐ Not triggered (one or more of 4.1–4.4 = NO) → **Not prohibited under Art. 5(1)(d)**
- ☐ Triggered, valid exemption with all conditions met → **Permitted under Art. 5(2)-(7)**
- ☐ Triggered, no valid exemption or conditions not met → **PROHIBITED**

*Assessment notes:* _______________________________________________

---

### Prohibition 5 — Biometric Categorisation by Protected Characteristics
**Regulatory Reference:** Article 5(1)(e) (formerly Art. 5(1)(b) in earlier drafts)

**What is prohibited:** AI systems that categorise natural persons individually based on biometric data to deduce or infer their race, ethnicity, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 5.1 | Does the system process biometric data (facial geometry, iris patterns, fingerprints, voice characteristics, gait, behavioural patterns)? | ☐ | ☐ |
| 5.2 | Does the system assign persons to categories that correspond to or proxy for race, ethnicity, political opinions, trade union membership, religious beliefs, sex life, or sexual orientation? | ☐ | ☐ |
| 5.3 | Are those categorisations derived from or inferred through the biometric data? | ☐ | ☐ |

**Prohibition 5 triggered if:** All of 5.1–5.3 = YES.

**Prohibition 5 triggered:** ☐ YES ☐ NO

**Important scope note:** This prohibition does **not** cover: (i) biometric verification (1:1 matching for access control); (ii) biometric identification that is not purpose-built to categorise by protected characteristics; (iii) law enforcement databases using biometrics for identity verification of known suspects (subject to separate law enforcement rules).

**No exemptions exist for Prohibition 5.** If triggered, the system is prohibited.

**Conclusion — Prohibition 5:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 6 — Emotion Recognition in Workplace and Education
**Regulatory Reference:** Article 5(1)(f)

**What is prohibited:** AI systems used to infer the emotions of natural persons in the contexts of the workplace and educational institutions.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 6.1 | Does the system use facial expressions, body language, voice patterns, physiological signals, or other signals to infer or classify a person's emotional or affective state? | ☐ | ☐ |
| 6.2 | Is the system deployed in: (a) a workplace (including remote work environments), or (b) an educational institution (schools, universities, training centres)? | ☐ | ☐ |

**Prohibition 6 triggered if:** Both 6.1 AND 6.2 = YES.

**Prohibition 6 triggered:** ☐ YES ☐ NO

**Permitted exceptions (narrow):** Emotion recognition systems placed on the market **solely** for medical or safety reasons are not prohibited. Examples: drowsiness detection in commercial vehicle drivers for road safety purposes; emotion recognition in clinical/therapeutic settings.

| Exception | Applicable? |
|---|---|
| Medical purpose (clinical diagnosis, treatment support, patient monitoring) | ☐ YES ☐ NO |
| Safety purpose (e.g., driver drowsiness detection in transport) | ☐ YES ☐ NO |

**Conclusion — Prohibition 6:**
- ☐ Not triggered → **Not prohibited**
- ☐ Triggered, valid safety/medical exception applies → **Not prohibited** (document exception basis)
- ☐ Triggered, no exception → **PROHIBITED**

*Assessment notes:* _______________________________________________

---

### Prohibition 7 — Untargeted Scraping for Facial Recognition Databases
**Regulatory Reference:** Article 5(1)(g)

**What is prohibited:** Creating or expanding facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 7.1 | Does the system, or did any component of it, build a database of facial images or facial embeddings/templates? | ☐ | ☐ |
| 7.2 | Were any facial images or embeddings obtained through bulk collection from internet sources (social media, image hosting sites, public websites) without the specific consent of the individuals depicted? | ☐ | ☐ |
| 7.3 | Were any facial images or embeddings obtained through bulk extraction from CCTV or surveillance footage without targeted collection? | ☐ | ☐ |

**Prohibition 7 triggered if:** 7.1 = YES **AND** either 7.2 OR 7.3 = YES.

**Prohibition 7 triggered:** ☐ YES ☐ NO

**Scope note:** This prohibition applies to the **creation or expansion** of databases. Use of a lawfully constructed facial recognition database (e.g., passport/ID database with consent) for law enforcement purposes is regulated under the law enforcement AI rules and the GPAI regulations, not this prohibition.

**No exemptions exist for Prohibition 7.** If triggered, the system is prohibited.

**Conclusion — Prohibition 7:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 8 — AI-Enabled Predictive Profiling and Inferring Criminal Risk
**Regulatory Reference:** Article 5(1)(h)

**What is prohibited:** AI systems used by law enforcement for making individual risk assessments of natural persons in order to predict or assess the risk of a natural person committing a criminal offence, based solely on profiling or on traits and characteristics — without being based on objective and verifiable facts directly linked to criminal activity.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 8.1 | Is the system operated by or on behalf of a law enforcement authority? | ☐ | ☐ |
| 8.2 | Does the system generate predictions or risk scores about the likelihood of a specific individual committing a criminal offence? | ☐ | ☐ |
| 8.3 | Are those predictions or risk scores based primarily on profiling, demographic characteristics, social network analysis, or behavioural traits rather than objective and verifiable facts directly linked to criminal activity? | ☐ | ☐ |

**Prohibition 8 triggered if:** All of 8.1–8.3 = YES.

**Prohibition 8 triggered:** ☐ YES ☐ NO

**Scope note — what is NOT prohibited:**
- Predictive policing for geographic hotspot analysis (area-based, not individual-based)
- Recidivism risk tools used in sentencing that are based on verified criminal history (these are High Risk — Annex III, Area 6)
- Systems that assess risk based on **objective facts directly linking an individual to criminal activity** (e.g., transaction monitoring that flags specific suspicious transactions)

**No exemptions exist for Prohibition 8 as defined.** If triggered, the system is prohibited.

**Conclusion — Prohibition 8:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

## Part 3 — Overall Assessment Summary

| Prohibition | Article | Triggered? | Exemption Valid? | Final Conclusion |
|---|---|---|---|---|
| 1. Subliminal/manipulative techniques | Art. 5(1)(a) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 2. Exploitation of vulnerable groups | Art. 5(1)(b) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 3. Social scoring by public authorities | Art. 5(1)(c) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 4. Real-time RBI in public spaces (LE) | Art. 5(1)(d) | ☐ YES ☐ NO | ☐ YES ☐ NO | ☐ Prohibited ☐ Permitted |
| 5. Biometric categorisation by protected characteristics | Art. 5(1)(e) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 6. Emotion recognition (workplace/education) | Art. 5(1)(f) | ☐ YES ☐ NO | ☐ YES ☐ NO | ☐ Prohibited ☐ Permitted |
| 7. Untargeted facial image scraping | Art. 5(1)(g) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 8. Predictive individual criminal profiling | Art. 5(1)(h) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |

### Overall Clearance Decision

☐ **CLEARED** — No prohibited practices identified. System may proceed to risk classification under Doc 01.

☐ **PROHIBITED** — One or more prohibited practices identified without valid exemption. System must **not** be placed on the market, put into service, or used in the EU. Legal counsel must be consulted immediately.

☐ **CONDITIONAL** — Prohibition triggered but valid exemption identified. All exemption conditions must be fully documented and maintained. Proceed to exemption compliance documentation.

---

## Part 4 — Clearance Certificate

| Field | Detail |
|---|---|
| System name | |
| System version | |
| Intended use | |
| Deploying/providing organisation | |
| Assessed by (name and role) | |
| Legal counsel reviewed | ☐ YES ☐ NO — Name: |
| Date of assessment | |
| Date of next review | (recommend annually or upon material change) |
| Overall clearance decision | ☐ CLEARED ☐ PROHIBITED ☐ CONDITIONAL |

### Reviewer Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Compliance Lead | | | |
| Legal Counsel | | | |
| System Owner | | | |
| DPO (if biometric data processed) | | | |

---

## Part 5 — Post-Clearance Obligations

Even where a system is cleared of all Article 5 prohibitions, the following obligations apply:

| Obligation | Reference | Action Required |
|---|---|---|
| Continue to risk classification | Doc 01 | Complete risk tier assessment |
| If High Risk: full conformity assessment | Doc 02 | Follow 8-step process |
| If biometric data processed: GDPR Art. 9 assessment | Doc 18 | Special category data compliance |
| Annual re-assessment upon material change to system | This document | Re-run full Part 2 checklist |
| Record retention (minimum 10 years for law enforcement systems) | Article 12 | Maintain in compliance records |

---

## Revision History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | April 2026 | Initial release — all 8 prohibitions, exemption tests | Toolkit Team |

---

*This document does not constitute legal advice. The prohibited practices under Article 5 are subject to ongoing interpretation by the EU AI Office, national competent authorities, and the European Data Protection Board. Always seek qualified legal counsel for binding determinations, particularly for systems involving biometric data, law enforcement, or vulnerable persons.*
