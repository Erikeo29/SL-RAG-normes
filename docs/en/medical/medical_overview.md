# Overview of the regulatory landscape — medical devices

This document provides a structured overview of the regulatory framework
applicable to medical devices. It covers the main jurisdictions
(United States, European Union, international), quality management system
standards (ISO 13485), software requirements (IEC 62304),
cybersecurity, and the interconnections between these various frameworks.
The objective is to serve as an entry point for navigating the collection
of documents indexed in the RAG and to enable a rapid understanding
of the regulatory obligations at each stage of the life cycle of a
medical device.

---

## Table of contents

1. [Introduction — why standards matter](#1-introduction--why-standards-matter)
2. [International regulatory landscape — comparative table](#2-international-regulatory-landscape--comparative-table)
3. [FDA 21 CFR 820 (QMSR) — design controls, CAPA, production, validation](#3-fda-21-cfr-820-qmsr--design-controls-capa-production-validation)
4. [ISO 13485 — medical device QMS, clauses 4-8](#4-iso-13485--medical-device-qms-clauses-4-8)
5. [EU MDR 2017/745 and IVDR 2017/746](#5-eu-mdr-2017745-and-ivdr-2017746)
6. [IEC 62304 — medical software, classes A/B/C, life cycle](#6-iec-62304--medical-software-classes-abc-life-cycle)
7. [Cybersecurity — FDA premarket, SBOM, threat modeling](#7-cybersecurity--fda-premarket-sbom-threat-modeling)
8. [Interconnections between standards — cross-reference table](#8-interconnections-between-standards--cross-reference-table)
9. [Documents indexed in the RAG](#9-documents-indexed-in-the-rag)

---

## 1. Introduction — why standards matter

### 1.1 Role of standards in the life cycle of a medical device

The standards and regulations governing medical devices exist
to ensure patient safety, product effectiveness, and
traceability throughout their life cycle. They cover each stage,
from initial design through to post-market surveillance,
including manufacturing, sterilization, packaging,
and distribution.

A medical device, whether it is a simple adhesive bandage, an
orthopedic implant, or a diagnostic support software, is subject to
a set of requirements proportionate to the risk it poses to the
patient or user. This proportionality is the foundation of
the modern regulatory approach.

Standards fulfill several essential functions:

- **Harmonization**: they provide a common language between manufacturers,
  notified bodies, regulatory authorities, and healthcare professionals.
- **Presumption of conformity**: compliance with a harmonized standard
  allows the presumption of conformity with the essential requirements
  of a regulation.
- **State of the art**: they codify good practices recognized by
  the scientific and industrial community.
- **Market access**: they constitute a prerequisite for obtaining the
  CE marking in Europe or FDA clearance/approval in the United States.

### 1.2 Main regulatory and standardization bodies

| Body | Jurisdiction | Primary role |
|------|-------------|--------------|
| FDA (Food and Drug Administration) | United States | Regulatory authority. Evaluates and authorizes the marketing of medical devices through the 510(k), PMA, and De Novo pathways. |
| European Commission | European Union | Issues regulations (EU MDR 2017/745, EU IVDR 2017/746) directly applicable in the law of Member States. |
| ISO (International Organization for Standardization) | International | Develops consensus standards (ISO 13485, ISO 14971) used worldwide as compliance frameworks. |
| IEC (International Electrotechnical Commission) | International | Standards for electrical, electronic, and software aspects (IEC 62304, IEC 60601, IEC 62443). |
| IMDRF (International Medical Device Regulators Forum) | International | Forum for regulatory convergence among the major worldwide authorities. |
| Health Canada | Canada | Canadian regulatory authority. Enforces the Medical Devices Regulations (SOR/98-282). |
| TGA (Therapeutic Goods Administration) | Australia | Australian regulatory authority. Manages the ARTG register. |
| PMDA (Pharmaceuticals and Medical Devices Agency) | Japan | Japanese regulatory authority. Enforces the Pharmaceutical Affairs Law (PAL). |

### 1.3 Risk-based approach

The guiding principle of medical device regulation is
the risk-based approach. The higher the risk associated with a device,
the stricter the regulatory requirements. This principle is
concretely reflected in classification systems:

- **FDA**: class I (low risk, general controls), class II (moderate
  risk, special controls + 510(k)), class III (high risk, PMA).
- **EU MDR**: class I, IIa, IIb, III according to the rules in Annex VIII.
- **EU IVDR**: class A, B, C, D.
- **ISO 14971**: risk management standard applicable to all
  medical devices, regardless of class.

Risk management according to ISO 14971 is the common thread connecting
all other standards together. It is involved in design
(design controls), software validation (IEC 62304),
cybersecurity (IEC 81001-5-1), and post-market surveillance (EU MDR
Chapter VII).

---

## 2. International regulatory landscape — comparative table

### 2.1 Comparative overview

The table below compares the main regulatory frameworks
applicable to medical devices across six jurisdictions and the
international ISO framework.

| Aspect | FDA (United States) | EU MDR (Europe) | ISO (international) | Health Canada | TGA (Australia) | PMDA (Japan) |
|--------|---------------------|-----------------|---------------------|---------------|-----------------|--------------|
| **Legal framework** | Federal Food, Drug, and Cosmetic Act (FD&C Act) | Regulation (EU) 2017/745 (MDR) and 2017/746 (IVDR) | Voluntary standards (ISO 13485, ISO 14971) | Food and Drugs Act + SOR/98-282 | Therapeutic Goods Act 1989 | Pharmaceutical and Medical Device Act (PMD Act) |
| **Classification** | Class I, II, III | Class I, IIa, IIb, III | Not applicable (cross-cutting framework) | Class I, II, III, IV | Class I, IIa, IIb, III | Class I, II, III, IV |
| **Primary approval pathway** | 510(k), PMA, De Novo | Conformity assessment by notified body (Annexes IX, X, XI) | ISO 13485 certification by accredited body | Licence application (class II-IV) | Inclusion in the ARTG register | Shonin (approval) application |
| **QMS requirement** | 21 CFR 820 (QMSR, aligned with ISO 13485 since 2024) | ISO 13485 required via Annex IX | ISO 13485:2016 | ISO 13485 required (CMDR) | ISO 13485 required | ISO 13485 required (QMS ordinance) |
| **Risk management** | ISO 14971 referenced in QMSR | ISO 14971 harmonized standard | ISO 14971:2019 | ISO 14971 required | ISO 14971 required | ISO 14971 required |
| **Post-market surveillance** | MDR (Medical Device Reporting), 21 CFR 803 | PMS plan, PSUR, vigilance reports (Chapters VII and VIII) | Not directly applicable | Mandatory incident reporting | TGA vigilance system | Adverse event reports |
| **Unique device identification (UDI)** | UDI Rule (21 CFR 801.20), GUDID database | UDI system, EUDAMED database (Article 27) | Not applicable | UDI mandatory (IMDRF harmonized) | UDI being deployed | UDI being implemented |
| **Clinical evaluation** | Clinical trials (IDE), clinical data for PMA | Clinical evaluation (Article 61), clinical investigations (Chapter VI) | ISO 14155 (clinical investigations) | Clinical evidence required | Clinical evidence required | Clinical data for shonin |
| **Software (SaMD)** | FDA guidance SaMD, IEC 62304 referenced | IEC 62304 harmonized standard, MDCG guidances | IEC 62304:2006+A1:2015 | SaMD framework (IMDRF) | Specific SaMD regulations | Specific SaMD regulations |

### 2.2 International convergence via IMDRF

The IMDRF (International Medical Device Regulators Forum) plays a
central role in the harmonization of regulatory approaches. Its main
convergence documents include:

- **IMDRF/SaMD N12**: classification framework for Software as a
  Medical Device (SaMD), based on the significance of the information
  provided and the targeted health condition.
- **IMDRF/UDI**: unique device identification system, progressively
  adopted by all member jurisdictions.
- **IMDRF/MDSAP**: single audit program (Medical Device Single Audit
  Program) recognized by five authorities (FDA, Health Canada, TGA, ANVISA,
  PMDA).

The IMDRF N47 document on SaMD, indexed in the RAG, details the
qualification and classification framework for medical software.

---

## 3. FDA 21 CFR 820 (QMSR) — design controls, CAPA, production, validation

### 3.1 Context and transition to the QMSR

21 CFR Part 820, historically known as the Quality System
Regulation (QSR), constitutes the regulatory foundation of the quality
management system for medical devices marketed in the
United States. In February 2024, the FDA published the final rule establishing
the Quality Management System Regulation (QMSR), which aligns 21 CFR 820
with the ISO 13485:2016 standard.

The key points of this transition are as follows:

- **Incorporation by reference**: the QMSR incorporates ISO 13485:2016
  as a regulatory requirement, rather than maintaining a separate
  and divergent regulatory text.
- **Transition period**: manufacturers have a deadline to comply
  with the new framework (effective date: February 2, 2026).
- **FDA-specific requirements**: certain requirements specific to the FDA
  remain and supplement ISO 13485 (notably complaint reports,
  MDRs, and traceability requirements).
- **Risk management**: ISO 14971 is explicitly referenced as the
  risk management method in the QMSR.

### 3.2 Design controls (historically 21 CFR 820.30)

Design controls represent one of the pillars of the FDA quality system.
They apply to all class II and III devices, as well as
certain specifically listed class I devices. The waterfall diagram
of design controls follows a logical sequence.

#### Elements of design controls

| Step | Historical reference | ISO 13485 correspondence | Description |
|------|---------------------|--------------------------|-------------|
| Design and development planning | 820.30(b) | 7.3.2 | Planning of design activities, including planned reviews, verifications, and validations. |
| Design input | 820.30(c) | 7.3.3 | Device requirements: performance, safety, compatibility, applicable standards. |
| Design output | 820.30(d) | 7.3.4 | Design results: specifications, drawings, manufacturing procedures, acceptance criteria. |
| Design review | 820.30(e) | 7.3.5 | Formal and documented reviews at defined stages of the design process. |
| Design verification | 820.30(f) | 7.3.6 | Confirmation that design outputs meet design inputs (does the product conform to specifications?). |
| Design validation | 820.30(g) | 7.3.7 | Confirmation that the final device meets user needs and intended use (was the right product designed?). |
| Design transfer | 820.30(h) | 7.3.8 | Transfer of design specifications to production, ensuring reproducibility. |
| Design changes | 820.30(i) | 7.3.9 | Control of design changes, including evaluation, verification, and validation as applicable. |

#### Distinction between verification and validation

The distinction between verification and validation is fundamental:

- **Verification**: "Did we design the product correctly?" —
  tests, inspections, analyses demonstrating that each design output
  conforms to the corresponding design input.
- **Validation**: "Did we design the right product?" — demonstration
  that the final device meets user needs under actual
  or simulated conditions of use.

The FDA Design Controls Guidance, indexed in the RAG, provides detailed
examples and recommendations for each step.

### 3.3 CAPA (historically 21 CFR 820.90)

The CAPA (Corrective and Preventive Action) system is historically
the subsystem most frequently cited during FDA inspections. With
the QMSR, CAPA requirements are now aligned with clauses
8.5.2 (corrective action) and 8.5.3 (preventive action) of ISO 13485.

The steps of a complete CAPA process are as follows:

1. **Identification**: detection of the problem through complaints, audits,
   production data, post-market surveillance, or internal nonconformities.
2. **Evaluation**: determination of the scope and severity of the problem.
3. **Investigation**: root cause analysis using tools such as the
   Ishikawa diagram, the 5 Whys, or fault tree analysis.
4. **Action plan**: definition of corrective actions (eliminate the
   cause of the existing problem) and/or preventive actions (prevent the
   occurrence of a potential problem).
5. **Implementation**: execution of planned actions with defined
   responsibilities and deadlines.
6. **Effectiveness verification**: confirmation that the implemented
   actions resolved the problem and did not introduce new risks.
7. **Closure and documentation**: complete recording of the CAPA process
   in the quality system.

### 3.4 Production and process controls

The requirements related to production cover:

- **Production controls**: documented procedures, controlled
  environments, qualified equipment, and trained personnel.
- **Process validation**: mandatory for any process whose
  outcome cannot be fully verified by subsequent inspection or
  testing (for example: sterilization, welding, injection
  molding, screen printing).
- **Environmental controls**: clean rooms, temperature and
  humidity control, according to product requirements.
- **Equipment control**: preventive maintenance, calibration, and
  qualification of production and measurement equipment.

### 3.5 Device master record and device history record

| Record | Content | Objective |
|--------|---------|-----------|
| Device master record (DMR) | Device specifications, manufacturing procedures, quality system requirements, packaging and labeling specifications. | Define "how to manufacture" the device. |
| Device history record (DHR) | Production records for each lot/unit: manufacturing dates, quantities, acceptance criteria, test results, personnel involved. | Demonstrate that each device was manufactured in accordance with the DMR. |
| Quality system record (QSR) | Procedures, quality policy, quality objectives, audit reports, CAPA, management reviews. | Document the overall functioning of the quality system. |
| Complaint files | Records of all complaints received, evaluations, investigations, and actions taken. | Ensure traceability and systematic handling of field feedback. |

### 3.6 Summary table of key subparts of 21 CFR 820

| Subpart | Subject | Corresponding ISO 13485 clauses |
|---------|---------|----------------------------------|
| Subpart A | General provisions, scope | 1, 4.1 |
| Subpart B | Quality system requirements | 4.1, 4.2, 5.1, 5.4, 5.5, 5.6 |
| Subpart C | Design controls | 7.3 |
| Subpart D | Document controls | 4.2.3, 4.2.4 |
| Subpart E | Purchasing controls | 7.4 |
| Subpart F | Identification and traceability | 7.5.3, 7.5.9 |
| Subpart G | Production and process controls | 7.5.1, 7.5.2, 7.5.6 |
| Subpart H | Acceptance activities | 7.5.7, 8.2.4 |
| Subpart I | Nonconforming product | 8.3 |
| Subpart J | Corrective and preventive action | 8.5.2, 8.5.3 |
| Subpart K | Labeling and packaging control | 7.5.1 |
| Subpart L | Handling, storage, distribution | 7.5.5, 7.5.11 |
| Subpart M | Records | 4.2.4, 4.2.5 |
| Subpart N | Servicing | 7.5.4 |
| Subpart O | Statistical techniques | 8.2.3, 8.2.4 |

---

## 4. ISO 13485 — medical device QMS, clauses 4-8

### 4.1 Scope and field of application

ISO 13485:2016 specifies the requirements for a quality management
system (QMS) for organizations that need to demonstrate their ability
to provide medical devices and related services that conform to
customer requirements and applicable regulatory requirements.

Key points:

- The standard is applicable to any organization involved in the life cycle
  of a medical device: design, manufacturing, storage, distribution,
  installation, maintenance, and decommissioning.
- It is independent of the size of the organization and the type of
  medical device produced.
- Unlike ISO 9001, ISO 13485 emphasizes regulatory compliance
  and product safety rather than continual improvement
  and customer satisfaction.
- Since the QMSR, ISO 13485 has direct regulatory force in the
  United States in addition to its use as a harmonized standard in Europe.

### 4.2 Clause 4 — quality management system

#### 4.2.1 General requirements (clause 4.1)

The organization shall establish, document, implement, and maintain a
quality management system and maintain its effectiveness. This
includes:

- Determining the processes needed for the QMS and their application
  throughout the organization.
- Determining the sequence and interaction of these processes.
- Determining the criteria and methods needed to ensure the
  effectiveness of the operation and control of these processes.
- Applying a risk-based approach to the control of QMS processes.

#### 4.2.2 Documentation requirements (clause 4.2)

| Document type | Requirement | Examples |
|---------------|-------------|----------|
| Quality policy | Mandatory, approved by management. | Commitment to regulatory compliance and QMS effectiveness. |
| Quality objectives | Measurable, consistent with the quality policy. | Rate of CAPA closed on time, rate of recurring nonconformities. |
| Quality manual | Scope of the QMS, documented procedures or references, description of process interactions. | Master document of the quality system. |
| Documented procedures | Required by the standard for specific processes. | Document control, records control, internal audit, CAPA. |
| Records | Evidence of conformity and effective functioning of the QMS. | Design review reports, validation results, training records. |
| Medical device file | For each type or family of medical device. | Specifications, manufacturing procedures, risk management file. |

### 4.3 Clause 5 — management responsibility

Management shall demonstrate its commitment to the QMS through the
following actions:

- **Management commitment** (5.1): communicating the importance of
  meeting regulatory and customer requirements, establishing the
  quality policy and quality objectives.
- **Customer focus** (5.2): customer requirements and regulatory
  requirements are determined and met.
- **Quality policy** (5.3): appropriate to the purpose of the organization,
  communicated and understood at all relevant levels.
- **Planning** (5.4): quality objectives are established at relevant
  functions and levels; QMS planning is carried out to meet the
  requirements of clause 4.1 and quality objectives.
- **Management representative** (5.5.2): a member of management is
  appointed to ensure that QMS processes are established, implemented,
  and maintained.
- **Management review** (5.6): planned review of the QMS at defined
  intervals, including input elements (audits, customer feedback,
  process performance, CAPA) and output elements (improvement,
  resource needs).

### 4.4 Clause 6 — resource management

| Subclause | Subject | Key requirements |
|-----------|---------|------------------|
| 6.1 | Provision of resources | The organization determines and provides the resources needed for the QMS. |
| 6.2 | Human resources | Competence based on initial education, professional training, skills, and experience. Mandatory training records. |
| 6.3 | Infrastructure | Buildings, equipment, support services (transportation, communication, information systems). Documentation of maintenance requirements. |
| 6.4 | Work environment and contamination control | Working conditions needed for product conformity. Specific requirements for clean rooms and contamination prevention. |

### 4.5 Clause 7 — product realization

This clause is the most extensive in the standard and covers the entire
process of medical device realization.

#### 7.1 — Planning of product realization

The organization plans and develops the processes needed for
product realization, consistent with QMS requirements. Planning
shall include, as appropriate: quality objectives and product
requirements, specific processes and resources, verification and
validation activities, acceptance criteria, and necessary records.

Risk management according to ISO 14971 shall be integrated into the
planning of product realization.

#### 7.2 — Customer-related processes

Determination of product requirements (specified by the customer,
not stated but necessary, regulatory) and review of these requirements
before the organization commits.

#### 7.3 — Design and development

Clause 7.3 details the requirements for the design and development
process, mirroring the FDA design controls:

- 7.3.1: General provisions.
- 7.3.2: Design and development planning.
- 7.3.3: Design and development inputs.
- 7.3.4: Design and development outputs.
- 7.3.5: Design and development review.
- 7.3.6: Design and development verification.
- 7.3.7: Design and development validation.
- 7.3.8: Design and development transfer.
- 7.3.9: Control of design and development changes.
- 7.3.10: Design and development files.

#### 7.4 — Purchasing

Control of suppliers and purchased products: supplier evaluation and
selection, purchasing specifications, verification of purchased product.

#### 7.5 — Production and service provision

- 7.5.1: Control of production and service provision.
- 7.5.2: Cleanliness of product.
- 7.5.3: Installation activities.
- 7.5.4: Servicing activities.
- 7.5.5: Particular requirements for sterile medical devices.
- 7.5.6: Validation of processes for production and service provision.
- 7.5.7: Particular requirements for validation of processes for
  sterilization and sterile barrier systems.
- 7.5.8: Identification.
- 7.5.9: Traceability.
- 7.5.10: Customer property.
- 7.5.11: Preservation of product.

#### 7.6 — Control of monitoring and measuring equipment

Calibration, verification at defined intervals, recording of
calibration results, and metrological traceability.

### 4.6 Clause 8 — measurement, analysis, and improvement

| Subclause | Subject | Key requirements |
|-----------|---------|------------------|
| 8.1 | General | Planning of monitoring, measurement, analysis, and improvement processes. |
| 8.2.1 | Feedback | System for collecting and analyzing feedback, including complaints, as an input element for post-market surveillance. |
| 8.2.2 | Complaint handling | Documented procedure for the timely receipt, evaluation, and investigation of complaints. |
| 8.2.3 | Reporting to regulatory authorities | Documented procedure for reporting events meeting notification criteria. |
| 8.2.4 | Internal audit | Audit program at planned intervals, independent and competent auditors, follow-up of corrective actions. |
| 8.2.5 | Monitoring and measurement of processes | Appropriate methods for monitoring QMS processes. |
| 8.2.6 | Monitoring and measurement of product | Verification of product conformity to requirements at appropriate stages. |
| 8.3 | Control of nonconforming product | Identification, documentation, segregation, and disposition of nonconforming product. Evaluation of the need for investigation and notification to responsible parties. |
| 8.4 | Analysis of data | Collection and analysis of data to demonstrate the suitability and effectiveness of the QMS and to identify improvement opportunities. |
| 8.5.1 | General (improvement) | Identification and implementation of changes necessary for the continued suitability and effectiveness of the QMS. |
| 8.5.2 | Corrective action | Documented procedure: determination of nonconformities, causes, actions, effectiveness verification. |
| 8.5.3 | Preventive action | Documented procedure: determination of potential nonconformities, causes, actions, effectiveness verification. |

---

## 5. EU MDR 2017/745 and IVDR 2017/746

### 5.1 Transition from the MDD to the MDR — timeline

Regulation (EU) 2017/745 on medical devices (MDR) replaces
the former directives 93/42/EEC (MDD) and 90/385/EEC (AIMDD). The
transition followed the schedule below:

| Date | Event |
|------|-------|
| April 5, 2017 | Publication of EU MDR 2017/745 in the Official Journal of the EU. |
| May 25, 2017 | Entry into force of the MDR (beginning of the transition period). |
| May 26, 2020 | Originally planned date of application (postponed due to COVID-19). |
| May 26, 2021 | Effective date of application of the MDR. |
| May 26, 2024 | End of the transition period for devices certified under the MDD (valid MDD certificates). |
| December 31, 2027 | Extended deadline for placing on the market devices covered by MDD certificates (subject to conditions). |
| December 31, 2028 | Extended deadline for class III and implantable devices covered by MDD certificates. |

**Note**: the transition dates were amended by Regulation
(EU) 2023/607 to avoid supply disruptions of medical devices
on the European market.

### 5.2 Classification rules (Annex VIII)

The MDR defines 22 classification rules divided into four categories
of devices.

| Class | Risk level | Examples | Main rules |
|-------|-----------|----------|------------|
| I | Low | Non-sterile dressings, manual wheelchairs, stethoscopes. | Rules 1-4 (non-invasive devices). |
| I sterile / I with measuring function / I reusable surgical | Low (with additional requirements) | Sterile examination gloves, syringes, reusable surgical instruments. | Rules 1-4 with special conditions. |
| IIa | Moderate | Hearing aids, contact lenses, short-term urinary catheters. | Rules 5-8 (short-term invasive), rules 9-13 (active devices). |
| IIb | Moderate-high | Pulmonary ventilators, hemodialyzers, ureteral stents. | Rules 5-8 (long-term invasive), rule 11 (diagnostic software). |
| III | High | Heart valves, hip prostheses, coronary stents, breast implants. | Rule 6 (CNS/heart contact), rule 8 (long-term implantable). |

#### Rule 11 — software classification

Rule 11 of the MDR is particularly important for software:

- Software intended to provide information used to make decisions
  for diagnostic or therapeutic purposes is classified as
  class IIa, unless these decisions may result in:
  - Death or irreversible deterioration of health condition — class III.
  - Serious deterioration of health condition or surgical
    intervention — class IIb.
- Software intended to monitor physiological processes is
  classified as class IIa, unless it monitors vital parameters and
  variations may present an immediate danger — class IIb.
- All other software is classified as class I.

### 5.3 Conformity assessment pathways

| Annex | Application | Bodies involved |
|-------|-------------|-----------------|
| Annex IX | Conformity assessment based on a quality management system and assessment of technical documentation. Applicable to all classes (Chapter I for QMS, Chapter II for technical documentation assessment, Chapter III for type examination). | Notified body (for classes Is, Im, Ir, IIa, IIb, III). |
| Annex X | Conformity assessment based on type examination. Combined with Annex XI. | Notified body. |
| Annex XI | Conformity assessment based on product conformity verification (Part A: production quality assurance; Part B: product verification). | Notified body. |

For class I devices (non-sterile, without measuring function,
non-reusable surgical), the manufacturer performs a self-assessment
of conformity without the involvement of a notified body.

### 5.4 General safety and performance requirements (GSPR)

Annex I of the MDR replaces the "essential requirements" of the MDD with
the "general safety and performance requirements"
(GSPR — General Safety and Performance Requirements). They are organized
into three chapters:

1. **Chapter I — general requirements** (GSPR 1-9): general safety,
   risk management (acceptability of residual risk), clinical
   performance, shelf life, transport, and storage.
2. **Chapter II — requirements regarding design and manufacture**
   (GSPR 10-22): chemical, physical, and biological properties;
   infection and microbial contamination; compatibility with
   the use environment; requirements for active devices,
   software, and connected devices.
3. **Chapter III — requirements regarding the information supplied with the
   device** (GSPR 23): labeling, instructions for use, languages.

### 5.5 Clinical evaluation (Article 61)

Clinical evaluation is a continuous process throughout the life cycle
of the device. It shall be based on:

- Clinical data from clinical investigations on the
  device concerned.
- Clinical data from clinical investigations or other
  studies reported in the scientific literature on a demonstrated
  equivalent device.
- Clinical data from post-market surveillance (in
  particular, post-market clinical follow-up — PMCF).

The document MDCG 2020-6 (Sufficient Clinical Evidence), indexed in the RAG,
provides guidance on the sufficient level of clinical evidence for
each device class.

### 5.6 Post-market surveillance and vigilance

The MDR significantly strengthens post-market surveillance requirements
compared to the MDD:

| Requirement | Description | MDR articles |
|-------------|-------------|--------------|
| Post-market surveillance plan | Structured document describing the methods for collecting and analyzing post-market data. | Article 84 |
| Post-market surveillance report | Summary of surveillance results, regularly updated. Required for class I. | Article 85 |
| Periodic safety update report (PSUR) | Detailed report including the conclusions of the benefit-risk assessment and sales volume. Required for classes IIa, IIb, and III. | Article 86 |
| Post-market clinical follow-up (PMCF) | Continuous process of collecting clinical data to confirm safety and performance over the entire lifetime of the device. | Annex XIV, Part B |
| Vigilance | Reporting of serious incidents and field safety corrective actions (FSCA) to competent authorities. | Articles 87-92 |
| Trend analysis | Statistically significant increase in the frequency or severity of incidents and adverse effects. | Article 88 |

### 5.7 Unique device identification (UDI) and EUDAMED

The UDI (Unique Device Identification) system is defined in Articles 27
and 28 and in Annex VI of the MDR. It comprises:

- **UDI-DI** (Device Identifier): code identifying the manufacturer and the
  specific version or model of the device.
- **UDI-PI** (Production Identifier): code identifying the unit of
  production (serial number, lot number, manufacturing date,
  expiration date).

EUDAMED (European Database on Medical Devices) is the centralized
European database that is intended to consolidate six modules: registration
of economic operators, UDI/device registration, notified bodies
and certificates, clinical investigations, vigilance and post-market
surveillance, market surveillance.

### 5.8 IVDR 2017/746 — specificities for in vitro diagnostic devices

Regulation (EU) 2017/746 (IVDR) applies to in vitro diagnostic
medical devices. It introduces a major change compared to
Directive 98/79/EC (IVDD): the shift from a list-based classification
system to a rule-based classification system.

#### IVDR classification

| Class | Risk level | Examples |
|-------|-----------|----------|
| A | Low | General culture media, laboratory reagents without specific diagnostic purpose. |
| B | Moderate-low | Pregnancy self-tests, cholesterol tests, quality control devices. |
| C | Moderate-high | HIV screening tests (for diagnosis), ABO blood group tests, human genetics tests. |
| D | High | HIV screening tests (for transfusion safety), tests for detecting transmissible agents (blood, organs). |

#### Performance evaluation (IVDR)

The IVDR replaces the concept of "clinical evaluation" (used for
medical devices under the MDR) with "performance evaluation,"
which comprises:

- Analytical performance studies (analytical sensitivity,
  analytical specificity, accuracy, repeatability, reproducibility).
- Clinical performance studies (clinical sensitivity, clinical
  specificity, positive and negative predictive value).
- Scientific validity evaluation (literature review
  and review of available data).

### 5.9 Comparative table MDR vs MDD

| Aspect | MDD 93/42/EEC | MDR 2017/745 |
|--------|---------------|--------------|
| Type of text | Directive (national transposition). | Regulation (directly applicable). |
| Classification | 18 rules, 4 classes. | 22 rules, 4 classes (reclassification of certain devices). |
| Clinical evaluation | General requirement, little detail. | Strengthened requirements (Article 61), mandatory PMCF. |
| Post-market surveillance | Minimal requirements. | PMS plan, PSUR, PMCF, trend analysis. |
| UDI | Not required. | Mandatory (Articles 27-28). |
| Person responsible for regulatory compliance | Not explicitly required. | Explicit requirement (Article 15). |
| Transparency | Limited. | EUDAMED, summary of safety and clinical performance (SSCP). |
| Software | Few specific provisions. | Specific rule 11, GSPR 17 (software). |
| Notified bodies | Limited oversight. | Strengthened oversight, unannounced audits, technical documentation reviews. |
| Custom-made devices | Lighter requirements. | Strengthened requirements (Annex XIII). |

---

## 6. IEC 62304 — medical software, classes A/B/C, life cycle

### 6.1 Scope

IEC 62304:2006+A1:2015 (Software life cycle processes) defines the
life cycle requirements for the development and maintenance of
medical software. It applies to two categories:

- **Software as a Medical Device (SaMD)**: software that is itself a
  medical device (for example, a radiological diagnostic support
  software).
- **Software in a Medical Device (SiMD)**: software embedded in a
  medical device (for example, the firmware of a patient monitor).

The standard is harmonized under EU MDR 2017/745 and is
referenced in the FDA QMSR. It is applicable in conjunction with
ISO 14971 for risk management and ISO 13485 for the quality
management system.

### 6.2 Software safety classification

IEC 62304 introduces a safety classification system specific to
software, distinct from the regulatory classification of the medical
device as a whole.

| Software class | Definition | Consequence on the life cycle |
|----------------|------------|-------------------------------|
| Class A | No injury or damage to health is possible. | Minimum requirements: development planning, configuration management, problem resolution. |
| Class B | Non-serious injury is possible. | Intermediate requirements: addition of requirements analysis, architectural design, integration testing, and verification. |
| Class C | Death or serious injury is possible. | Full requirements: addition of detailed design, unit testing, and complete requirements traceability. |

**Important**: the software safety classification is determined by
the risk management process (ISO 14971). A software system can
be decomposed into subsystems (software items), each of which may have a
different safety classification, provided that the separation is
sufficiently robust to prevent a lower-class element from
affecting a higher-class element.

### 6.3 Software development life cycle processes

#### 6.3.1 Software development planning (clause 5.1)

The software development plan shall document:

- The applicable life cycle processes, activities, and tasks.
- The deliverables of each activity and task.
- The traceability between system requirements, software requirements,
  tests, and risk management.
- The life cycle model used (V-model, agile, iterative, etc.).
- The development standards and methods, tools, and programming
  language.
- The software safety classification and the subsystem
  decomposition strategy.

#### 6.3.2 Software requirements analysis (clause 5.2)

This step consists of defining software requirements from
system requirements and risk management requirements:

- Functional and performance requirements.
- Input and output requirements (interfaces).
- Safety requirements (resulting from risk analysis).
- Usability requirements (ergonomics, fitness for use).
- Data requirements and data integrity requirements.
- Installation and maintenance requirements.

#### 6.3.3 Architectural design (clause 5.3)

The software is decomposed into elements (software items) at a level of
detail sufficient to allow:

- Identification of all software items and their interfaces.
- Description of how the software is structured to
  meet the requirements.
- Identification of SOUP (Software of Unknown
  Provenance) software items — third-party libraries, open source
  components, operating systems.
- Safety classification of each software item.

#### 6.3.4 Detailed design (clause 5.4)

Required only for class C software items. It shall
detail:

- The algorithms, data structures, and interfaces of each software
  unit.
- The level of detail allowing correct implementation and
  verification through unit testing.

#### 6.3.5 Software unit implementation and verification (clause 5.5)

- Implementation of source code in accordance with the detailed design.
- Verification that each software unit meets its specifications
  (unit testing for class C, verification strategy for class B).
- Acceptance criteria defined in advance for each unit.

#### 6.3.6 Integration and integration testing (clause 5.6)

- Progressive integration of software items in accordance with the
  integration plan.
- Integration testing verifying that interfaces between elements
  function correctly.
- Verification that SOUP items are correctly integrated.
- Documentation of test results and identified anomalies.

#### 6.3.7 Software system testing (clause 5.7)

- Testing at the complete software system level.
- Verification that the software system meets the software requirements.
- Testing performed in an environment representative of the intended
  use environment.
- Requirements coverage by tests documented via a traceability
  matrix.

#### 6.3.8 Software release (clause 5.8)

- Verification that all planned activities and tasks have been
  completed.
- Documentation of the released version and build procedures.
- Complete traceability between requirements, design, implementation,
  and tests.
- Evaluation of known residual anomalies (known bugs and their
  impact on safety).

#### 6.3.9 Software maintenance (clause 6)

The maintenance process covers:

- Monitoring of post-market feedback related to
  the software.
- Analysis and resolution of reported problems.
- Management of software modifications (impact assessment,
  safety reclassification if necessary).
- Implementation of updates and patches.

### 6.4 Table of activities required by safety class

| Activity / Process | Class A | Class B | Class C |
|--------------------|---------|---------|---------|
| Development planning (5.1) | Required | Required | Required |
| Requirements analysis (5.2) | Not required | Required | Required |
| Architectural design (5.3) | Not required | Required | Required |
| Detailed design (5.4) | Not required | Not required | Required |
| Implementation (5.5.1) | Required | Required | Required |
| Unit verification (5.5.2-5.5.5) | Not required | Not required | Required |
| Integration and integration testing (5.6) | Not required | Required | Required |
| Software system testing (5.7) | Not required | Required | Required |
| Software release (5.8) | Required | Required | Required |
| Configuration management (clause 8) | Required | Required | Required |
| Problem resolution (clause 9) | Required | Required | Required |
| Maintenance (clause 6) | Required | Required | Required |
| Software risk management (clause 7) | Required | Required | Required |
| Requirements traceability | Not required | Required | Required (complete) |

### 6.5 SOUP (Software of Unknown Provenance) management

SOUP represents a particular challenge in medical software
development. IEC 62304 requires:

- Identification of all SOUP items used (name, version,
  manufacturer).
- Definition of functional and performance requirements for
  each SOUP.
- Verification that each SOUP meets the defined requirements.
- Monitoring of anomalies published by SOUP suppliers.
- Assessment of the impact of SOUP anomalies on the safety of the
  medical software.

### 6.6 Relationships with other standards

| Related standard | Relationship with IEC 62304 |
|------------------|----------------------------|
| ISO 14971 | Provides the risk management framework used for software safety classification and identification of safety requirements. |
| ISO 13485 | Provides the quality management system framework in which IEC 62304 processes are integrated (design controls, CAPA). |
| IEC 62366-1 | Usability engineering. Provides the ergonomic requirements integrated into software requirements. |
| IEC 82304-1 | Standard for standalone health software. Uses IEC 62304 for life cycle requirements. |
| IEC 81001-5-1 | Safety, effectiveness, and security of health software and health IT systems — product life cycle security. Complements IEC 62304 on cybersecurity aspects. |
| IEC 62443 | Security for industrial automation and control systems. Referenced for cybersecurity aspects of connected medical systems. |

---

## 7. Cybersecurity — FDA premarket, SBOM, threat modeling

### 7.1 Regulatory context

Medical device cybersecurity has become a major issue with
the increasing connectivity of healthcare systems. Cybersecurity
incidents can have direct consequences on patient safety:
dose modification, unauthorized access to health data,
unavailability of critical devices.

Several regulatory and normative texts now govern the
cybersecurity of medical devices:

- **FDA**: Premarket Cybersecurity Guidance (September 2023), Section 524B
  of the FD&C Act (Consolidated Appropriations Act, 2023).
- **EU MDR**: GSPR 17.2 (cybersecurity requirements), MDCG 2019-16 rev. 1.
- **IEC 81001-5-1**: security in the life cycle of health software.
- **IEC 62443**: security for industrial control systems, applicable
  by extension to connected medical systems.
- **AAMI TIR57**: principles of security risk management for
  medical devices.

### 7.2 FDA premarket cybersecurity guidance (2023)

The FDA document "Cybersecurity in Medical Devices: Quality System
Considerations and Content of Premarket Submissions," published in September
2023, constitutes the primary reference for premarket submissions in the
United States. It is indexed in the RAG under the name
`FDA_Cybersecurity_Medical_Devices.pdf`.

The essential points of this document are as follows:

#### Secure Product Development Framework (SPDF)

The FDA recommends the adoption of a Secure Product Development Framework
(SPDF) encompassing the entire product life cycle. The SPDF integrates:

- Security risk management.
- Secure architecture and design (secure by design).
- Cybersecurity verification and validation.
- Post-market cybersecurity management.

#### Content of the premarket submission

For devices containing software elements or connected features, the FDA
expects the following information in the premarket submission:

1. **System description**: architecture, components, data flows,
   network interfaces, and communication protocols.
2. **Threat model**: identification of potential threats, attack
   surfaces, malicious actors, and compromise scenarios.
3. **Cybersecurity risk assessment**: likelihood and impact of
   identified threats, mitigation measures.
4. **Software Bill of Materials (SBOM)**: complete inventory of all
   software components (proprietary, open source, SOUP).
5. **Security controls**: authentication, encryption,
   logging, access control, data integrity.
6. **Cybersecurity management plan**: vulnerability response
   procedures, update policy, end of support.
7. **Cybersecurity testing**: penetration testing results,
   vulnerability analyses, fuzzing, static code review.

### 7.3 Threat modeling

Threat modeling is a structured process for identifying
and assessing cybersecurity risks. The methodologies commonly
used for medical devices are as follows.

| Methodology | Description | Typical application |
|-------------|-------------|---------------------|
| STRIDE | Classification of threats into six categories: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. | Systematic analysis of device components and interfaces. |
| CVSS | Common Vulnerability Scoring System. Quantitative assessment of vulnerability severity. | Prioritization of identified vulnerabilities and patches. |
| Attack trees | Tree representation of possible attack paths to achieve a malicious objective. | In-depth analysis of specific attack scenarios. |
| TARA | Threat Assessment and Remediation Analysis. MITRE methodology for identifying and prioritizing countermeasures. | Systematic evaluation of cybersecurity countermeasures. |

The threat modeling process typically comprises the following steps:

1. **Scope definition**: identification of assets to protect
   (patient data, safety functions, device integrity).
2. **Architecture decomposition**: identification of components,
   interfaces, data flows, and trust boundaries.
3. **Threat identification**: for each component and interface,
   systematic identification of possible threats.
4. **Risk assessment**: estimation of the likelihood of exploitation
   and the potential impact of each threat.
5. **Countermeasure definition**: for each threat deemed
   unacceptable, definition of appropriate security controls.
6. **Verification**: security testing confirming the effectiveness of
   countermeasures.

### 7.4 Software Bill of Materials (SBOM)

The SBOM is a structured, machine-readable inventory of all
software components integrated into a medical device. The FDA requires
an SBOM for any premarket submission of a device containing
software, in accordance with Section 524B of the FD&C Act.

The elements that must appear in an SBOM are as follows:

- **Proprietary components**: name, version, manufacturer.
- **Open source components**: name, version, license, source.
- **Commercial third-party components**: name, version, supplier.
- **Dependencies**: relationships between components.
- **Known vulnerabilities**: CVEs associated with the versions used.

The standard SBOM formats are:

- **SPDX** (Software Package Data Exchange): ISO/IEC 5962:2021 format.
- **CycloneDX**: OWASP format optimized for security analysis.

### 7.5 Vulnerability management and patching

Vulnerability management throughout the device life cycle
comprises:

- **Continuous monitoring**: watching for published vulnerabilities (NVD,
  CVE) affecting device components.
- **Impact assessment**: analysis of exploitability and potential impact
  on patient safety for each vulnerability.
- **Remediation**: development, validation, and deployment of patches
  within timeframes proportionate to criticality.
- **Communication**: notification to users and authorities
  (ICS-CERT/CISA for the FDA, vigilance for the MDR).

### 7.6 IEC 81001-5-1 — security in the life cycle of health software

IEC 81001-5-1:2021 is the reference standard for the cybersecurity of
health software. It is harmonized under the MDR and will be increasingly
referenced by regulatory authorities worldwide.

The key processes defined by IEC 81001-5-1 are as follows:

| Process | Description | Link with IEC 62304 |
|---------|-------------|---------------------|
| Security planning | Integration of cybersecurity into the software development plan. | Extension of clause 5.1. |
| Security requirements | Identification of security requirements from the threat model and risk analysis. | Feeds into clause 5.2. |
| Secure architecture | Design of an architecture integrating the principles of defense in depth, least privilege, and separation. | Extension of clause 5.3. |
| Secure implementation | Secure coding practices, code review, static analysis. | Extension of clause 5.5. |
| Security testing | Penetration testing, fuzzing, vulnerability analysis, verification of security controls. | Extension of clauses 5.6 and 5.7. |
| Security configuration management | Secure management of source code, build artifacts, and cryptographic keys. | Extension of clause 8. |
| Security problem management | Specific process for handling security vulnerabilities. | Extension of clause 9. |
| Security maintenance | Security patch management, secure deactivation, and end of life. | Extension of clause 6. |

### 7.7 Summary table of cybersecurity deliverables

| Deliverable | Description | Reference(s) |
|-------------|-------------|--------------|
| Threat model | Documentation of identified threats, attack surfaces, compromise scenarios. | FDA Cybersecurity Guidance, IEC 81001-5-1 clause 5.3.2 |
| Cybersecurity risk assessment | Security risk analysis with likelihood, impact, and mitigation measures. | FDA Cybersecurity Guidance, ISO 14971, IEC 81001-5-1 |
| SBOM | Complete inventory of software components in SPDX or CycloneDX format. | FDA (Section 524B FD&C Act), IEC 81001-5-1 |
| Cybersecurity management plan | Vulnerability response procedures, update policy, communication. | FDA Cybersecurity Guidance |
| Security testing reports | Penetration testing results, vulnerability analyses, code review. | FDA Cybersecurity Guidance, IEC 81001-5-1 clause 5.7 |
| Update and end-of-support policy | Planned support duration, update strategy, end-of-life procedure. | FDA Cybersecurity Guidance |
| Security architecture documentation | Description of security controls: encryption, authentication, access control, logging. | IEC 81001-5-1 clause 5.4, AAMI TIR57 |
| Incident response plan | Procedure for managing cybersecurity incidents, including notification of authorities. | FDA Postmarket Guidance, IEC 81001-5-1 |

---

## 8. Interconnections between standards — cross-reference table

### 8.1 Overview of interactions

The standards governing medical devices are not isolated from one
another. They form an interconnected ecosystem where each standard
relies on or complements the others. The cross-reference table below
shows the correspondences between the main frameworks.

### 8.2 Cross-reference table — correspondences by domain

| Standard / Regulation | QMS | Design | Risk management | Software | Cybersecurity | Clinical evaluation | Post-market surveillance |
|-----------------------|-----|--------|-----------------|----------|---------------|---------------------|--------------------------|
| **FDA 21 CFR 820 (QMSR)** | Incorporates ISO 13485 (in full). FDA-specific requirements as supplements. | 7.3 (via ISO 13485). Historically 820.30. | References ISO 14971 in the QMSR. | References IEC 62304 in guidances. | FDA Cybersecurity Guidance (2023). Section 524B FD&C Act. | Clinical evidence for PMA. Substantial equivalence for 510(k). | 21 CFR 803 (MDR reporting). 21 CFR 806 (corrections and removals). |
| **ISO 13485:2016** | Clauses 4-8 (standard dedicated to QMS). | Clause 7.3 (design and development). | Clause 7.1 (planning with risk management). References ISO 14971 in a note. | Not software-specific (covered by IEC 62304). | Not specific (covered by IEC 81001-5-1). | Not specific (covered by ISO 14155 and MDR). | Clause 8.2.1 (feedback), 8.2.2 (complaints), 8.2.3 (reporting). |
| **EU MDR 2017/745** | Annex IX Chapter I (QMS required, ISO 13485 as the framework). | GSPR 5 (performance), Annex II (technical documentation), Annex IX Chapter II. | GSPR 1-3 (risk management). ISO 14971 harmonized standard. | GSPR 17 (software and programmable devices). Rule 11 (classification). IEC 62304 harmonized. | GSPR 17.2 (cybersecurity). MDCG 2019-16. | Article 61 (clinical evaluation). Chapter VI (investigations). Annex XIV Part A (evaluation) and B (PMCF). | Chapter VII (vigilance and PMS). Articles 83-92. PSUR (Article 86). |
| **IEC 62304:2006+A1:2015** | Integrates within the QMS (ISO 13485 clause 7.3 for the design part). | Clauses 5.1-5.8 (software development life cycle). | Clause 7 (software risk management). Uses ISO 14971 as the framework. | Standard dedicated to the software life cycle. Classes A, B, C. | Clause 5.2 (security requirements). Complemented by IEC 81001-5-1. | Not directly applicable. | Clause 6 (maintenance). Clause 9 (problem resolution). |
| **IEC 81001-5-1:2021** | Integrates within the QMS (security processes added to quality processes). | Clauses 5.3-5.4 (secure design). Complements IEC 62304. | Clauses 5.2-5.3 (security risk management). Uses ISO 14971 extended to security. | Extends IEC 62304 processes with cybersecurity requirements. | Standard dedicated to cybersecurity of health software. | Not directly applicable. | Clause 5.9 (security maintenance). Post-market vulnerability management. |
| **ISO 14971:2019** | Applies within the QMS framework (ISO 13485 clause 7.1). | Feeds design inputs (safety requirements from risk analysis). | Standard dedicated to risk management. Complete process: analysis, evaluation, control, monitoring. | Provides the safety classification framework for IEC 62304. | Framework extended by AAMI TIR57 for cybersecurity risks. | Feeds the benefit-risk assessment. | Continuous monitoring of residual risks in the post-market phase (clause 10). |

### 8.3 Information flow between standards

The typical information flow between standards follows the scheme below:

1. **ISO 14971** provides the initial risk analysis, which determines:
   - Safety-related design requirements (ISO 13485 clause 7.3.3).
   - Software safety classification (IEC 62304 clause 4.3).
   - Cybersecurity requirements (IEC 81001-5-1 clause 5.2).

2. **ISO 13485** provides the structural framework of the quality system in
   which all other processes are integrated:
   - The design and development process (clause 7.3) encapsulates
     IEC 62304 and IEC 81001-5-1 processes.
   - The CAPA process (clause 8.5) handles problems identified by
     IEC 62304 (clause 9) and IEC 81001-5-1 (clause 5.8).

3. **EU MDR** or **FDA 21 CFR 820** provide the regulatory framework
   that makes these standards mandatory or recommended.

4. **IEC 62304** and **IEC 81001-5-1** detail the software life cycle
   and cybersecurity aspects, respectively, building on the frameworks
   provided by ISO 14971 and ISO 13485.

### 8.4 Points of attention during integrated implementation

| Point of attention | Explanation | Standards concerned |
|--------------------|-------------|---------------------|
| Unified risk management file | A single risk management file covering risks related to patient safety, cybersecurity, and usability. | ISO 14971, IEC 81001-5-1, IEC 62366-1 |
| End-to-end traceability | From system requirement to software requirement, through design, implementation, and testing. | ISO 13485 (7.3), IEC 62304 (5.1-5.8), EU MDR (Annex II) |
| Integrated CAPA/SOUP/vulnerability process | A single problem resolution process covering quality nonconformities, software anomalies, SOUP vulnerabilities, and cybersecurity vulnerabilities. | ISO 13485 (8.5), IEC 62304 (clause 9), IEC 81001-5-1 (5.8) |
| Integrated post-market surveillance | PMS plan covering clinical complaints, software anomalies, and cybersecurity vulnerabilities. | EU MDR (Articles 83-86), IEC 62304 (clause 6), FDA 21 CFR 803 |
| Joint validation | Medical software validation shall cover functional aspects, patient safety aspects, and cybersecurity aspects. | ISO 13485 (7.3.7), IEC 62304 (5.7), IEC 81001-5-1 (5.7) |

---

## 9. Documents indexed in the RAG

### 9.1 Medical collection

The following documents are indexed in the medical collection of the RAG and
can be queried directly through the Streamlit interface.

| File | Description | Source |
|------|-------------|--------|
| `EU_MDR_2017_745_EN.pdf` | Regulation (EU) 2017/745 on medical devices — English version. Full text of the regulation including Annexes I to XVII. | Official Journal of the EU (open access). |
| `EU_MDR_2017_745_FR.pdf` | Regulation (EU) 2017/745 — French version. Identical to the EN document but in the official French language version. | Official Journal of the EU (open access). |
| `Règlement Européen (MDR) 2017_745.pdf` | Supplementary version of the MDR regulation in French. May correspond to an annotated or reformatted version. | Public source. |
| `EU_IVDR_2017_746_EN.pdf` | Regulation (EU) 2017/746 on in vitro diagnostic medical devices — English version. | Official Journal of the EU (open access). |
| `EU_IVDR_2017_746_FR.pdf` | Regulation (EU) 2017/746 — French version. | Official Journal of the EU (open access). |
| `FDA_Cybersecurity_Medical_Devices.pdf` | FDA guidance: "Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions" (2023). | FDA (open access). |
| `FDA_Guide_Inspections_Quality_Systems.pdf` | FDA guide for quality system inspections. Used by FDA inspectors during audits of medical device manufacturing establishments. | FDA (open access). |
| `FDA_MDQS_Manual.pdf` | FDA Medical Device Quality Systems Manual. Reference documentation on FDA QMS requirements. | FDA (open access). |
| `FDA_Quality_System_Regulation_Overview.pdf` | Overview of the FDA quality system regulation (21 CFR 820). Covers the fundamental principles of the QSR/QMSR. | FDA (open access). |
| `FDA_QMSR_Risk_Management.pdf` | FDA document on risk management within the QMSR framework. Articulation between the QMSR and ISO 14971. | FDA (open access). |
| `IMDRF_N47_Software_SaMD.pdf` | IMDRF N47 document: "Software as a Medical Device (SaMD): Clinical Evaluation." International reference framework for the clinical evaluation of software qualified as medical devices. | IMDRF (open access). |
| `ISO_IEC_Guide_99_International_Vocabulary_Metrology.pdf` | ISO/IEC Guide 99: International Vocabulary of Metrology (VIM). Fundamental definitions used in measurement and device qualification standards. | ISO/IEC (open access for vocabulary). |
| `MDCG_2020-6_Sufficient_Clinical_Evidence.pdf` | MDCG 2020-6: "Guidance on Sufficient Clinical Evidence for Legacy Devices." Guidance from the Medical Device Coordination Group on the sufficient level of clinical evidence for existing devices in the context of the transition to the MDR. | European Commission (open access). |

### 9.2 Notes on the collection

- All indexed documents are regulatory texts, guidances, or standards
  whose public version is freely accessible.
- The complete ISO and IEC standards (for example ISO 13485:2016 or
  IEC 62304:2006+A1:2015) are protected by copyright and are not
  included in the collection. References to these standards in this
  document are based on publicly available information.
- The collection may be enriched over time with new documents
  (for example, additional MDCG guidances, updated FDA guidances,
  ASTM standards applicable to medical devices).
- To query these documents, use the RAG interface of the Streamlit
  application by selecting the "medical" collection.

### 9.3 Standards not indexed but referenced in this document

The following standards are frequently mentioned in this document but are
not indexed in the RAG due to their protected publication status:

| Standard | Title | Reason for absence |
|----------|-------|--------------------|
| ISO 13485:2016 | Medical devices — Quality management systems — Requirements for regulatory purposes. | Paid standard (ISO). |
| ISO 14971:2019 | Medical devices — Application of risk management to medical devices. | Paid standard (ISO). |
| IEC 62304:2006+A1:2015 | Medical device software — Software life cycle processes. | Paid standard (IEC). |
| IEC 81001-5-1:2021 | Health software and health IT systems safety, effectiveness and security — Part 5-1: Security — Activities in the product life cycle. | Paid standard (IEC). |
| IEC 62366-1:2015+A1:2020 | Medical devices — Part 1: Application of usability engineering to medical devices. | Paid standard (IEC). |
| ISO 14155:2020 | Clinical investigation of medical devices for human subjects — Good clinical practice. | Paid standard (ISO). |
| IEC 62443 (series) | Security for industrial automation and control systems. | Paid standard series (IEC). |

---

*Document generated for the medical standards RAG module. The information
presented reflects the current state of regulations and standards in force.
For any regulatory application, refer to the official texts
in their most recent version.*
