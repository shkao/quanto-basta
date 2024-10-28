# Module 3

## In vivo Pharmacokinetics

### Learning Objectives

- Define in vitro in vivo correlation (IVIVC)
- Correlate compound structures to in vivo pharmacokinetic (PK) properties in mouse and rat
- Describe how in vivo PK studies are used to prioritize lead compounds

### In vivo PK studies

- Informed by in vitro ADME assays
- Common early species: mouse and rat
- Allow determination of all key PK parameters, including CL, Vd, T1/2, and bioavailability
- Correlation of in vitro ADME data with in vivo PK studies in a program (IVIVC) boosts confidence in in vitro results.

### Mouse antimalarial PK data

| Entry | Vd (L/kg)  | CL (mL/min/kg) | T1/2 (h) |
|-------|------------|----------------|----------|
| 15    | 12.3       | 188.9          | 2.7      |
| 22    | 10.2       | 49.2           | 2.0      |
| 34    | 2.7        | 12.5           | 2.8      |
| 36    | 1.2        | 25.9           | 0.7      |

- **Vd (L/kg) classification**:
  - Low: 0.1-0.4
  - Moderate: 0.6-5
  - High: >5

- **CL (mL/min/kg) classification**:
  - Low: 0-30
  - Moderate: 30-60
  - High: >60

### Rat antimalarial PK data

| Entry | AUC(0–5h) (h·nM)  | Cmax (nM) | AUC(0–5h)/dose [(min·μg/mL)/(mg/kg)] |
|-------|-------------------|-----------|--------------------------------------|
| 22    | 487               | 126       | 1.2                                  |
| 29    | Not determined    | BLQ       | -                                    |
| 34    | 2,097             | 504       | 5.1                                  |

### Rat oral PK data for compound 22

| Dose (mg/kg) | Cmax (nM) | Tmax (h) | T1/2 (h) | AUC0→∞ (h·nM) | F (%) |
|--------------|-----------|----------|----------|---------------|-------|
| 10           | 91        | 1.5      | 4.7      | 974           | 20    |
| 30           | 580       | 4.3      | 6.3      | 7,337         | 40    |
| 100          | 2,233     | 8.0      | 8.4      | 34,885        | 57    |

**IV parameters**:

- Vd: 13.7 L/kg
- CL: 67.5 mL/min/kg
- T1/2: 4.6 h

## A Target-Based Example - Complement Factor B Inhibitor

### Learning Objectives

- Contrast target-based drug discovery to a phenotypic drug discovery program
- Describe how structural biology tools can assist lead optimization

### Target-based & phenotypic discovery

- **Phenotypic discovery**:
  - Drug target unknown
  - Lead selection/optimization via activity in cells/tissues

- **Target-based discovery**:
  - Drug target known
  - Lead selection/optimization via target-based biochemical, biophysical, & structural biology assays

### Factor B & the complement system

- Factor B, a protein with serine protease activity, is part of the complement system.
- The complement system is a biological pathway associated with the destruction of pathogens, damaged cells, and inflammation.
- A factor B inhibitor may treat chronic inflammatory diseases.

### Hit finding & X-ray confirmation

- **Compound**: 1 (structure shown)
- **CVF-Bb IC50**: 6.6 µM
- **Kd (SPR)**: 10 µM
- **hERG RLB IC50**: 7.1 µM
- **α1a IC50**: 0.3 µM
- **α2c IC50**: 0.18 µM

### Inclusion of an indole core

- **Compound 1**:
  - IC50 (human FB): 6.6 µM
  - Structure shown with binding interactions in the active site.

- **Compound 8**:
  - IC50 (human FB): 11 µM
  - Modified indole core structure with binding interactions highlighted in the active site.

Both compounds are shown interacting with key residues like Gly216, Arg192, and Thr190 in the active site, indicating important structural features for binding efficacy.

### Elaboration to LNP023

- **Compound 19**:
  - IC50 (human FB): 5.9 µM
  - Structure shown with binding interactions in the active site.

- **LNP023**:
  - IC50 (human FB): 0.012 µM
  - CVF-Bb IC50: 0.012 µM
  - Kd (SPR): 0.0079 µM
  - hERG RLB IC50: >30 µM
  - α1a IC50: >30 µM
  - α2c IC50: >30 µM

The figure shows binding interactions for both compounds in the active site, highlighting key residues such as Gly216, Val218, and Arg192. LNP023 demonstrates significant improvement in potency over compound 19.

## Biomarkers

### Learning Objectives

- Define the term biomarker
- List different types of biomarkers
- Outline how biomarkers support drug hunting

### Biomarker definitions & examples

- **Biomarker definition (U.S. FDA)**:
  - "A defined characteristic that is measured as an indicator of normal biological processes, pathogenic processes, or responses to an exposure or intervention, including therapeutic interventions."

- **Antimalarial program example**:
  - Reduction in parasitemia

- **Surrogate (validated surrogate endpoint)**:
  - A biomarker with a clear mechanistic rationale and clinical data providing strong evidence that an effect on the biomarker predicts a clinical benefit.
  - Example: LDL cholesterol predicts a reduction in cardiovascular disease.

### Types of biomarkers

- **Disease biomarkers**:
  - Diagnosis & prognosis
  - Early detection

- **Safety & efficacy biomarkers**:
  - Monitoring clinical response
  - Surrogate endpoints
  - Predicting outcomes/response

- **Pharmacology biomarkers**:
  - Pharmacodynamic & mechanism of action readouts
  - Pharmacokinetics

### Clinical biomarkers are critical for

- Identifying the right patients
- Optimizing dose and dosing paradigm
- Assuring safety of drug therapy
- Allowing ADME predictions
- Understanding population differences in response
- Supporting rapid decision-making in clinical trials

## In vivo Pharmacology and Safety

### Learning objectives

- **Describe considerations for animal disease models**
- **Prioritize compounds based on biomarker data from in vivo models**
- **List some key safety criteria monitored during drug hunting**

### Pre-clinical in vivo studies

- **Animal disease models track in vivo efficacy during optimization**  
  *minimizes risk of clinical failure for an antimalarial*
  
- **Biomarker measurements quantify efficacy**

- **Malaria treatment goal**  
  *clear parasitic infection completely and quickly to minimize development of resistance*

- **Disease models ideally are translatable to the human disease**

- **Malaria translation challenge**  
  *different malaria parasites infect different animal species*

### Results from efficacy study

| Entry | 1 × 30 mg/kg | | 1 × 100 mg/kg | | 3 × 30 mg/kg | |
|-------|--------------|-------------|---------------|-------------|---------------|------------|
|       | Activity drop (%) | Survival (d) | Activity drop (%) | Survival (d) | Activity drop (%) | Survival (d) |
| **22**   | 99.5          | 16.3       | 99.4         | 14.0         | 99.8         | 17.7        |
| **24**   | 99.0          | 15.0       | 99.1         | 16.7         | 99.7         | 17.0        |
| **34**   | 47.0          | 6.3        | 97.0         | 6.7          | 66.0         | 7.0         |
| **36**   | 90.0          | 7.0        | 99.3         | 9.7          | 99.7         | 12.0        |
| **CQ**   | 99.5          | 9.0        | 99.6         | 12.5         | 99.8         | 13.6        |
| **AS**   | 95.6          | 5.8        | 98.0         | 7.0          | 99.0         | 12.2        |

- **Biomarker**: parasitemia reduction (activity drop)
- **Reference**: Nagle, A., et al. *J. Med. Chem.* 2012, 55, 4244-4273.

### In vitro toxicity studies

- **hERG risk was reduced by 2-3-fold through N-substitution**  
  *(as seen with compound 22)*

- **Compound 22 was inactive against key CYP isoforms**, e.g., CYP3A4, CYP2C9, CYP2D6

- **Compound 22 showed very low cytotoxicity** against a variety of mammalian cell lines

## Discovery Story of KAF156

### Learning objectives

- **List some common steps in the lead optimization process**
- **Identify structural changes within the antimalarial series**
- **Describe optimized properties of KAF156 and its early clinical results**

### Progression of the Antimalarial Project

1. **Hit**
   - Initial compound identified with potential activity.

2. **Iterative process** (SAR: Structure-Activity Relationship)
   - Cycle of optimization focusing on SAR and potency.

3. **Early Leads**
   - Compounds showing promising activity and safety profiles.

4. **Mouse PK** (Pharmacokinetics)
   - Testing the pharmacokinetics in mice to assess absorption, distribution, metabolism, and excretion (ADME).

5. **Mouse efficacy**
   - Assessing the compound's efficacy in mouse models.

6. **Rodent & non-rodent PK**
   - Evaluating pharmacokinetics in both rodent and non-rodent species.

7. **In vivo safety**
   - Safety testing in live animal models to identify any potential toxicities.

### Hit → Lead → Clinical candidate

- **Hit**: The initial compound identified with antimalarial potential.
- **Lead**: The compound is optimized, improving its efficacy and safety.
- **Clinical candidate**: The final optimized compound, KAF156, ready for clinical trials.

### Optimization of Imidazolopiperazines

- **Early Leads**:  
  - Potency (IC₅₀): moderate (10-100 nM)
  - Oral exposure: moderate
  - Clearance (ER): poor (>0.6)
  - Solubility: poor (<30 mM)
  - Microsomal stability (ER): poor (>0.6)
  - hERG (IC₅₀): moderate (5-30 μM)
  - In vivo efficacy: moderate
  - Rule of 5 compliance: good

- **KAF156**:  
  - Potency (IC₅₀): good (<10 nM)
  - Oral exposure: good
  - Clearance (ER): good (<0.3)
  - Solubility: good (>100 mM)
  - Microsomal stability (ER): good (<0.3)
  - hERG (IC₅₀): good (>30 μM)
  - In vivo efficacy: good
  - Rule of 5 compliance: good

KAF156 represents a significant optimization across several parameters, improving in areas like potency, clearance, solubility, and in vivo efficacy compared to the early leads.

### Clinical efficacy & PK of KAF156

- **Left graph**:  
  - Depicts the decrease in **parasite count (per mm³)** over time (hours) after treatment with KAF156 in patients infected with *P. falciparum*.
  - Shows rapid parasite clearance, with significant reductions observed within 48 hours.

- **Right graph**:  
  - Represents the **pharmacokinetic (PK) profile** of KAF156.
  - The concentration of KAF156 (ng/mL) decreases over time, with a half-life indicated by a steady decline within the first 48 hours and further slow clearance up to 192 hours.

- **Reference**: White, N. J. et al. *N. Engl. J. Med.* 2016, 375, 1152-1160.
