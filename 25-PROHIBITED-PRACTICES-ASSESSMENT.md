# 25 — Article 5 Prohibited Practices Assessment Checklist
## EU AI Act Compliance Toolkit | v3.2.0 | April 2026
### Regulatory Reference: Article 5, Recitals 28–45 | Enforcement Date: 2 February 2025

---

## Purpose and Scope

This checklist provides a structured decision framework for determining whether an AI system, technique, or intended use falls within the **prohibited practices** established by Article 5 of Regulation (EU) 2024/1689. All eight prohibited categories have been active since **2 February 2025**.

> **Article 5(1) lettering (verified against the enacted text):** (a) subliminal/manipulative/deceptive techniques; (b) exploitation of vulnerabilities; (c) social scoring; (d) predictive criminal-offence risk assessment based on profiling; (e) untargeted scraping to build facial-recognition databases; (f) emotion recognition in workplace/education; (g) biometric categorisation by protected characteristics; (h) real-time remote biometric identification in public spaces for law enforcement. The numbered prohibitions below (1–8) are presentation order; the **Article reference shown for each is the correct enacted sub-letter**.

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

**What is prohibited:** Deploying AI techniques that operate below the threshold of conscious awareness, or that are purposefully manipulative or deceptive, in a way that materially distorts a person's behaviour by appreciably impairing their ability to make an informed decision — causing or reasonably likely to cause significant harm.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 1.1 | Does the system present stimuli at speeds or intensities outside conscious perception (subliminal audio, visual, or haptic)? | ☐ | ☐ |
| 1.2 | Does the system exploit known cognitive biases (anchoring, scarcity, social proof) to drive behaviour beyond what the person would choose with full information? | ☐ | ☐ |
| 1.3 | Does the system use techniques designed to create false impressions of urgency, scarcity, or social consensus? | ☐ | ☐ |
| 1.4 | Does the system use dark patterns, deceptive framing, or personalised persuasion in a way that bypasses rational agency? | ☐ | ☐ |
| 1.5 | Could the technique cause the person to take an action or hold a belief they would not otherwise have taken or held, resulting in significant harm (financial, physical, psychological)? | ☐ | ☐ |

**Prohibition 1 triggered if:** Any 1.1–1.5 = YES **AND** significant harm (actual or reasonably likely) is present.

**Prohibition 1 triggered:** ☐ YES ☐ NO

**No exemptions exist for Prohibition 1.** If triggered, the system is prohibited.

**Conclusion — Prohibition 1:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 2 — Exploitation of Vulnerable Groups
**Regulatory Reference:** Article 5(1)(b)

**What is prohibited:** AI systems that exploit any vulnerabilities of a natural person or specific group due to age, disability, or a specific social or economic situation, with the objective or effect of materially distorting their behaviour in a way that causes or is reasonably likely to cause significant harm.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 2.1 | Is the system specifically targeted at or primarily used with children under 18? | ☐ | ☐ |
| 2.2 | Is the system used in contexts where persons with cognitive impairments, mental health conditions, or severe social deprivation are a primary user group? | ☐ | ☐ |
| 2.3 | Does the system personalise its behaviour based on detected vulnerability signals (emotional state, economic stress, loneliness, grief)? | ☐ | ☐ |
| 2.4 | Does the system use vulnerability-exploiting techniques to drive purchasing decisions, data sharing, behavioural change, or political views? | ☐ | ☐ |
| 2.5 | Could the technique cause persons to take actions harmful to their physical, financial, psychological, or social wellbeing? | ☐ | ☐ |

**Prohibition 2 triggered if:** Any 2.1–2.5 = YES **AND** significant harm (actual or reasonably likely) is present.

**Prohibition 2 triggered:** ☐ YES ☐ NO

**No exemptions exist for Prohibition 2.** If triggered, the system is prohibited.

**Conclusion — Prohibition 2:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 3 — Social Scoring
**Regulatory Reference:** Article 5(1)(c)

**What is prohibited:** AI systems for the evaluation or classification of natural persons or groups over a period of time based on social behaviour or personal/personality characteristics, where the social score leads to detrimental or unfavourable treatment in social contexts unrelated to the original data, or that is unjustified or disproportionate. (Note: unlike earlier drafts, the enacted prohibition is **not** limited to public authorities — it applies regardless of who operates the system.)

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 3.1 | Does the system evaluate or classify natural persons or groups over time based on social behaviour or known/inferred personal or personality characteristics? | ☐ | ☐ |
| 3.2 | Does it produce a social score, rating, or classification? | ☐ | ☐ |
| 3.3 | Is that score used to determine treatment in social contexts unrelated to the contexts in which the data was generated or collected? | ☐ | ☐ |
| 3.4 | Does the system result in detrimental, unjustified, or disproportionate treatment relative to the social behaviour evaluated? | ☐ | ☐ |

**Prohibition 3 triggered if:** 3.1 = YES **AND** 3.2 = YES **AND** (3.3 OR 3.4) = YES.

**Prohibition 3 triggered:** ☐ YES ☐ NO

**No exemptions exist for Prohibition 3.** If triggered, the system is prohibited.

**Note:** Lawful private-sector creditworthiness/credit scoring and insurance pricing that comply with applicable Union law are **not** social scoring — they fall under **High Risk (Annex III, Area 5)**. See Doc 24 for the credit scoring worked example.

**Conclusion — Prohibition 3:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 4 — Predictive Policing Based on Profiling
**Regulatory Reference:** Article 5(1)(d)

**What is prohibited:** AI systems for making risk assessments of natural persons in order to assess or predict the risk of a person committing a criminal offence, based **solely** on profiling or on assessing personality traits and characteristics. (Does not apply to systems that support a human assessment already based on objective and verifiable facts directly linked to a criminal activity.)

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 4.1 | Does the system generate predictions or risk scores about the likelihood of a specific individual committing a criminal offence? | ☐ | ☐ |
| 4.2 | Are those predictions based **solely** on profiling of the person or on assessing their personality traits and characteristics? | ☐ | ☐ |
| 4.3 | Is the assessment **not** merely supporting a human assessment grounded in objective, verifiable facts directly linked to a criminal activity? | ☐ | ☐ |

**Prohibition 4 triggered if:** All of 4.1–4.3 = YES.

**Prohibition 4 triggered:** ☐ YES ☐ NO

**Scope note — what is NOT prohibited:**
- Place-based/geographic predictive analytics (not individual-level)
- Tools supporting a human assessment that is already based on objective, verifiable facts directly linked to criminal activity (these may be High Risk — Annex III, Area 6)

**No exemptions exist for Prohibition 4 as defined.** If triggered, the system is prohibited.

**Conclusion — Prohibition 4:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 5 — Untargeted Scraping for Facial Recognition Databases
**Regulatory Reference:** Article 5(1)(e)

**What is prohibited:** Creating or expanding facial recognition databases through the untargeted scraping of facial images from the internet or CCTV footage.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 5.1 | Does the system, or did any component of it, build or expand a database of facial images or facial embeddings/templates? | ☐ | ☐ |
| 5.2 | Were any facial images or embeddings obtained through **untargeted** bulk collection from internet sources (social media, image hosting sites, public websites)? | ☐ | ☐ |
| 5.3 | Were any facial images or embeddings obtained through **untargeted** bulk extraction from CCTV footage? | ☐ | ☐ |

**Prohibition 5 triggered if:** 5.1 = YES **AND** either 5.2 OR 5.3 = YES.

**Prohibition 5 triggered:** ☐ YES ☐ NO

**Scope note:** This prohibition applies to the **creation or expansion** of databases by untargeted scraping. Use of a lawfully constructed database (e.g. a consented ID database) is regulated under other rules, not this prohibition.

**No exemptions exist for Prohibition 5.** If triggered, the system is prohibited.

**Conclusion — Prohibition 5:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 6 — Emotion Recognition in Workplace and Education
**Regulatory Reference:** Article 5(1)(f)

**What is prohibited:** AI systems to infer the emotions of natural persons in the areas of workplace and education institutions.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 6.1 | Does the system use facial expressions, body language, voice patterns, physiological signals, or other signals to infer or classify a person's emotional or affective state? | ☐ | ☐ |
| 6.2 | Is the system deployed in: (a) a workplace (including remote work environments), or (b) an education institution? | ☐ | ☐ |

**Prohibition 6 triggered if:** Both 6.1 AND 6.2 = YES.

**Prohibition 6 triggered:** ☐ YES ☐ NO

**Permitted exceptions (narrow):** Emotion recognition systems intended to be put in place or into the market for **medical or safety reasons** are not prohibited. Examples: drowsiness/fatigue detection for road safety; clinical/therapeutic monitoring.

| Exception | Applicable? |
|---|---|
| Medical reasons (clinical diagnosis, treatment support, patient monitoring) | ☐ YES ☐ NO |
| Safety reasons (e.g., driver drowsiness detection in transport) | ☐ YES ☐ NO |

**Conclusion — Prohibition 6:**
- ☐ Not triggered → **Not prohibited**
- ☐ Triggered, valid medical/safety exception applies → **Not prohibited** (document exception basis)
- ☐ Triggered, no exception → **PROHIBITED**

*Assessment notes:* _______________________________________________

---

### Prohibition 7 — Biometric Categorisation by Protected Characteristics
**Regulatory Reference:** Article 5(1)(g)

**What is prohibited:** Biometric categorisation systems that individually categorise natural persons based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation.

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 7.1 | Does the system process biometric data (facial geometry, iris patterns, fingerprints, voice characteristics, gait)? | ☐ | ☐ |
| 7.2 | Does the system assign persons to categories that correspond to or proxy for race, political opinions, trade union membership, religious/philosophical beliefs, sex life, or sexual orientation? | ☐ | ☐ |
| 7.3 | Are those categorisations derived from or inferred through the biometric data? | ☐ | ☐ |

**Prohibition 7 triggered if:** All of 7.1–7.3 = YES.

**Prohibition 7 triggered:** ☐ YES ☐ NO

**Important scope note (Art. 5(1)(g)):** This prohibition does **not** cover the labelling or filtering of lawfully acquired biometric datasets (e.g. images) according to biometric data, or the categorisation of biometric data in the area of law enforcement. Biometric **verification** (1:1) and non-protected-characteristic categorisation are outside this prohibition (but may be High Risk — Annex III, Area 1).

**No exemptions exist for Prohibition 7 (beyond the scope carve-outs above).** If triggered, the system is prohibited.

**Conclusion — Prohibition 7:** ☐ Prohibited ☐ Not prohibited

*Assessment notes:* _______________________________________________

---

### Prohibition 8 — Real-Time Remote Biometric Identification in Public Spaces (Law Enforcement)
**Regulatory Reference:** Article 5(1)(h) and Article 5(2)–(7)

**What is prohibited:** The use of real-time remote biometric identification (RBI) systems in publicly accessible spaces for the purposes of law enforcement, unless and in so far as a listed exemption applies.

**Definitions:**
- **Real-time:** biometric data is captured, compared and identified without significant delay
- **Remote:** persons are identified without their active involvement, typically at a distance
- **Publicly accessible space:** any physical place accessible to the public (streets, transport hubs, shopping centres, public buildings)
- **Law enforcement purpose:** prevention, investigation, detection, or prosecution of criminal offences, or execution of criminal penalties

#### Primary Test

| # | Question | Yes | No |
|---|---|---|---|
| 8.1 | Is the system a remote biometric identification system (identifies persons by comparing biometric data against a reference database)? | ☐ | ☐ |
| 8.2 | Does the system operate in real-time (live or near-live, without significant delay)? | ☐ | ☐ |
| 8.3 | Is the system deployed in a publicly accessible space? | ☐ | ☐ |
| 8.4 | Is the deployment purpose law enforcement? | ☐ | ☐ |

**Prohibition 8 triggered if:** All of 8.1–8.4 = YES.

**Prohibition 8 triggered:** ☐ YES ☐ NO

If triggered, proceed to the **Exemption Test** below before concluding.

#### Exemption Test — Article 5(1)(h)(i)–(iii) Permitted Objectives

Real-time RBI for law enforcement is permitted **only** where strictly necessary for one of the following objectives, subject to authorisation and the safeguards in Art. 5(2)–(7):

| Exemption | Conditions | Applicable? |
|---|---|---|
| **E8-A: Targeted search for specific victims / missing persons** (Art. 5(1)(h)(i)) | Abduction, trafficking in human beings, sexual exploitation, or search for missing persons | ☐ YES ☐ NO |
| **E8-B: Prevention of a specific, substantial and imminent threat / terrorist attack** (Art. 5(1)(h)(ii)) | Threat to life or physical safety, or a genuine and present/foreseeable terrorist attack | ☐ YES ☐ NO |
| **E8-C: Localisation/identification of a suspect of a serious offence** (Art. 5(1)(h)(iii)) | Offence listed in Annex II punishable by a custodial sentence of at least 4 years | ☐ YES ☐ NO |

**Additional mandatory conditions (Article 5(2)–(7)):**

| Condition | Met? |
|---|---|
| Prior authorisation by a judicial authority or independent administrative authority (or, in duly justified urgency, requested without undue delay and at the latest within 24 hours) | ☐ YES ☐ NO |
| Deployment limited to the specific time period and geographic area authorised | ☐ YES ☐ NO |
| Fundamental rights impact assessment completed (Art. 27) and system registered in the EU database | ☐ YES ☐ NO |
| National law authorises the use, within the limits of Art. 5(5) | ☐ YES ☐ NO |
| Necessity and proportionality safeguards in place | ☐ YES ☐ NO |

**Conclusion — Prohibition 8:**
- ☐ Not triggered (one or more of 8.1–8.4 = NO) → **Not prohibited under Art. 5(1)(h)**
- ☐ Triggered, valid objective with all conditions met → **Permitted under Art. 5(2)-(7)** (note: still High Risk — Annex III, Area 1)
- ☐ Triggered, no valid objective or conditions not met → **PROHIBITED**

*Assessment notes:* _______________________________________________

---

## Part 3 — Overall Assessment Summary

| Prohibition | Article | Triggered? | Exemption Valid? | Final Conclusion |
|---|---|---|---|---|
| 1. Subliminal/manipulative/deceptive techniques | Art. 5(1)(a) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 2. Exploitation of vulnerable groups | Art. 5(1)(b) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 3. Social scoring | Art. 5(1)(c) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 4. Predictive policing based on profiling | Art. 5(1)(d) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 5. Untargeted facial image scraping | Art. 5(1)(e) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 6. Emotion recognition (workplace/education) | Art. 5(1)(f) | ☐ YES ☐ NO | ☐ YES ☐ NO | ☐ Prohibited ☐ Permitted |
| 7. Biometric categorisation by protected characteristics | Art. 5(1)(g) | ☐ YES ☐ NO | N/A | ☐ Prohibited ☐ Permitted |
| 8. Real-time RBI in public spaces (LE) | Art. 5(1)(h) | ☐ YES ☐ NO | ☐ YES ☐ NO | ☐ Prohibited ☐ Permitted |

### Overall Clearance Decision

☐ **CLEARED** — No prohibited practices identified. System may proceed to risk classification under Doc 01.

☐ **PROHIBITED** — One or more prohibited practices identified without valid exemption. System must **not** be placed on the market, put into service, or used in the EU. Legal counsel must be consulted immediately.

☐ **CONDITIONAL** — Prohibition triggered but valid exemption identified (Prohibitions 6 or 8 only). All exemption conditions must be fully documented and maintained. Note that a permitted real-time RBI deployment remains High Risk.

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
| If High Risk: full conformity assessment | Doc 02 | Follow the conformity assessment process |
| If biometric data processed: GDPR Art. 9 assessment | Doc 18 | Special category data compliance |
| Annual re-assessment upon material change to system | This document | Re-run full Part 2 checklist |
| Record retention | Doc 28 / Art. 18 | Maintain in compliance records |

---

## Revision History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.1 | April 2026 | Corrected Article 5(1) sub-letters to match the enacted text: predictive policing = (d); untargeted scraping = (e); biometric categorisation = (g); real-time RBI = (h). Removed the "public authorities only" limitation from social scoring (c). Aligned exemption references to Art. 5(1)(h)(i)–(iii) and the Annex II 4-year threshold. | Toolkit Team |
| 1.0 | April 2026 | Initial release — all 8 prohibitions, exemption tests | Toolkit Team |

---

*This document does not constitute legal advice. The prohibited practices under Article 5 are subject to ongoing interpretation by the European Commission, the AI Office, national competent authorities, and the European Data Protection Board. Always seek qualified legal counsel for binding determinations, particularly for systems involving biometric data, law enforcement, or vulnerable persons. See the Commission's Article 5 prohibited-practices guidelines for further detail.*
