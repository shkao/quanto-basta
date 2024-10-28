# Module 2

## Pharmacophores and Lead Optimization

### Learning Objectives

- Describe a common approach for defining a lead’s pharmacophore
- Outline some general ideas behind lead optimization

### Pharmacophore

- **Hit**: Represents an initial chemical structure with key features like a hydroxyl (OH) and nitrogen (N) atom.
- **Minimum pharmacophore**:
  - Comprises a **hydrogen bond donor (HBD)** and a **hydrogen bond acceptor (HBA)**.
  - Contains a **space-filling non-polar group** and a **substituent**.
- **Lead**: Optimized version of the hit, containing an amine (NH) and a trifluoromethyl (CF₃) group for enhanced biological properties.
  
- **Structure-Activity Relationship (SAR)**: Describes the connection between the chemical structure and its biological activity.

### Lead Analogues

- **Less optimized** → **More optimized** (optimization progression from left to right).
- **Original lead**: The initial compound identified.
- **Second generation lead**: Developed from analogues of the original lead, further refined.
- **Third generation lead**: A more optimized lead based on improvements from the second generation.
- **Final lead to clinic**: The most optimized version, suitable for clinical trials after multiple iterations and improvements.

## Assays for Guiding Lead Optimization

### Learning Objectives

- Differentiate target-based and phenotypic-based approaches to drug hunting.
- Describe cell proliferation assays used to understand SAR and guide optimization.

### Target-based vs Phenotypic Discovery

- **Target-based program**:
  - Focuses on a **known target** (e.g., enzyme or receptor).
  - Guided by **biochemical or cellular assays**.

- **Phenotypic program**:
  - **Knowledge of the target** is not required.
  - Guided by **phenotypic assays**.
  - Tests for **cellular, tissue, or organism-level outcomes**.

### Antimalarial Program Assays

- Antimalarial programs often use **phenotypic assays** to test compounds for malarial parasite survival.
  - **3D7**: A *Plasmodium falciparum* (Pf) strain of malaria.
  - **W2**: A pyrimethamine-resistant *Plasmodium falciparum* strain.
  - **Huh7**: A human hepatoma cell line (used for testing cytotoxicity).

- These assays help identify active compounds and allow for compound comparisons to understand **structure-activity relationship (SAR)** and guide the optimization of various characteristics.

## Hit Criteria and Characterization

### Learning Objectives

- List selected criteria for defining an acceptable hit molecule.
- Describe potential hit molecule liabilities that guide an optimization strategy.

### Screening Campaign

- **Phenotypic screen**: A screening method used to identify active compounds.
- **>2 million compounds tested**: A large-scale screening effort.
- **Seeking molecules distinct from existing antimalarials**: The goal is to find new compounds that are chemically different from current treatments.

- Structures shown:
  - **Chloroquine**: An aminoquinoline used as an antimalarial.
  - **Artemisinin**: An endo-peroxide used in malaria treatment.

### Key Hit Selection Criteria

1. **< 1 μM activity** against wild-type *Plasmodium falciparum* (3D7) and drug-resistant (W2) strains.
   - Mechanism differs from that of existing drugs.

2. **> 20-fold safety index** against Huh7 cells.
   - Hit has low toxicity to human cells.

3. **Easy synthesis** with activity across a hit series.
   - Potential for further optimization, known as a "tractable hit".

### Identification of Promising Hit

1. **< 1 μM 3D7 & W2 activity**:
   - 3D7: 63 nM
   - W2: 97 nM

2. **> 20-fold Huh7 cytotoxicity**:
   - >10 μM

3. **Activity across a hit series**.

- The identified hit compound is based on an **imidazolopiperazine scaffold** (highlighted in bold).

#### Reference  

Chatterjee, A. K. et al. *J. Med. Chem.*, 2011, 54, 5116-5130.

### Looking Toward Optimization

- **Solubility**:
  - > 175 μM at pH 6.8.

- **hERG inhibition** (toxicity risk):
  - IC₅₀ = 19 μM.

- **CYP450 inhibition**:
  - Not observed.

- **In vivo exposure**:
  - Low in mice.

#### Reference

Chatterjee, A. K. et al. *J. Med. Chem.*, 2011, 54, 5116-5130.

## Composite Parameters in Discovery

### Learning Objectives

- Describe the role of composite parameters in drug discovery.
- List selected examples of composite parameters.
- Demonstrate the use of lipophilic efficiency (LiPE) in a drug hunting program.

### Composite Parameters: Examples

- **In silico metrics**:
  - **MPO score**: Includes parameters like clogP, clogD, molecular weight (MW), topological polar surface area (TPSA), hydrogen bond donors (HBD), and the most basic pKa.

- **In vitro metrics**:
  - **LiPE (Lipophilic Efficiency)** = pIC₅₀ - logP: Measures biochemical or cell potency with clogP, clogD, or measured logD.

- **In vivo metrics**:
  - **Predicted human dose**: Based on in vivo pharmacokinetics (PK) and pharmacodynamics (PD) parameters or in vitro potency and ADME (Absorption, Distribution, Metabolism, and Excretion).

### Lipophilic Efficiency (LiPE)

- **LiPE** = pIC₅₀ - logP
  - Biochemical or cell potency measured with clogP, clogD, or logD.

- **pIC₅₀** = -log IC₅₀ (measures potency).
- **logP or logD** (measures lipophilicity).

- **Higher LiPE is favored**:
  - Desired: High pIC₅₀ (high potency).
  - Desired: Low logP (low lipophilicity).

- **High logP** is associated with:
  - Poor solubility.
  - Higher potency.
  - Potential toxicity risks.

## SAR of a Compound Series

### Learning Objectives

- Examine the structure-activity relationship (SAR) of a series of compounds.
- Summarize representative SAR techniques.

### Original Antimalarial Hit

- The original hit compound is based on an **imidazolopiperazine core**.

| Compound          | 3D7 IC₅₀ (nM) | W2 IC₅₀ (nM) |
|-------------------|---------------|--------------|
| **Hit**           | 460           | 473          |
| **Mefloquine**    | 12            | 8            |
| **Pyrimethamine** | 29            | >10,000      |
| **Artemisinin**   | 12            | 14           |

#### Reference  

Chatterjee, A. K. et al. *J. Med. Chem.*, 2012, 55, 4244-4273.

### SAR of the 7-position

- Structure-activity relationship (SAR) analysis for modifications at the 7-position of the original hit compound, leading to new analogues.

| R¹ Group          | 3D7 IC₅₀ (nM) | W2 IC₅₀ (nM) |
|-------------------|---------------|--------------|
| **gly (glycine)**  | 20            | 23           |
| **ala (alanine)**  | 90            | 64           |
| **α-Me ala**       | 20            | 25           |
| **val (valine)**   | 30            | 24           |
| **phe (phenylalanine)** | 110       | 121          |

#### Reference

Chatterjee, A. K. et al. *J. Med. Chem.*, 2012, 55, 4244-4273.

### SAR of the 2-position

- Structure-activity relationship (SAR) analysis for modifications at the 2-position of the original hit compound, leading to new analogues.

| R¹ Group      | R² Group        | 3D7 IC₅₀ (nM) | W2 IC₅₀ (nM) |
|---------------|-----------------|---------------|--------------|
| **gly**       | 4Me-Ph          | 10            | 13           |
| **α-Me ala**  | 4Me-Ph          | 20            | 24           |
| **gly**       | 4Cl-Ph          | 10            | 9            |
| **α-Me ala**  | 4Cl-Ph          | 30            | 24           |
| **gly**       | 3,4-diF-Ph      | 30            | 23           |
| **α-Me ala**  | 3,4-diF-Ph      | 44            | 36           |
| **gly**       | 3F,4Cl-Ph       | 3             | 4            |
| **α-Me ala**  | 3F,4Cl-Ph       | 40            | 52           |

- **Me** = Methyl
- **Ph** = Phenyl

#### Reference

Chatterjee, A. K. et al. *J. Med. Chem.*, 2012, 55, 4244-4273.

### SAR Around the Imidazolopiperazine (IP) Core

- Structure-activity relationship (SAR) analysis around the IP core, focusing on variations at positions R³, R⁴, R⁵, and R⁶.

| R³ Group     | R⁴ Group   | R⁵ Group | R⁶ Group | 3D7 IC₅₀ (nM) | W2 IC₅₀ (nM) |
|--------------|------------|----------|----------|---------------|--------------|
| 3Cl,4F-Ph    | (S)-Me, H  | H        | H        | 29            | 24           |
| 3Cl,4F-Ph    | (S)-i-Pr, H| H        | H        | 343           | 470          |
| 3Cl,4F-Ph    | Me, Me     | H        | H        | 27            | 24           |
| 3,4-diF-Ph   | Me, Me     | H        | H        | 4             | 5            |
| 4F-Ph        | H, H       | Me       | H        | 80            | 76           |
| 4F-Ph        | H, H       | H        | H        | 82            | 111          |

- **i-Pr** = isopropyl
- **Me** = methyl
- **Ph** = phenyl

#### Reference

Chatterjee, A. K. et al. *J. Med. Chem.*, 2012, 55, 4244-4273.

## Optimization of ADME Properties

### Learning Objectives

- List common in vitro ADME property assays.
- Demonstrate how in vitro ADME properties guide the design of drug candidates.

### Solubility & Permeability

- **Solubility**:
  - Vital for oral absorption.
  - Affects formulation.
  - May be pH-dependent.
  - Higher solubility is generally more favorable.

- **Permeability**:
  - Relevant to absorption and distribution.
  - May be passive or active.
  - Measured using the **Parallel Artificial Membrane Permeability Assay (PAMPA)**.
  - Tested with human colorectal carcinoma cell lines (**Caco-2**).

### In Vitro Metabolism Assays

- Important because metabolism affects bioavailability and half-life (**T₁/₂**).
- Often use **liver microsomes**.
- Estimate **intrinsic clearance (CLint)** or **extraction ratio (ER)**.
- Lower **CLint** and **ER** imply higher metabolic stability.

### Permeability of Anti-malarials

The table below presents the permeability data for different anti-malarial compounds (27, 28, 29, 31) using **PAMPA** and **Caco-2** assays.

| Entry | PAMPA (% absorbed) | Caco-2 (A→B) (cm/s × 10⁶) | Caco-2 (B→A) (cm/s × 10⁶) |
|-------|--------------------|---------------------------|---------------------------|
| **27**| 81                 | 3.1                       | 8.4                       |
| **28**| 99                 | 1.2                       | 1.0                       |
| **29**| 99                 | 3.5                       | 2.4                       |
| **31**| 99                 | 8.2                       | 2.4                       |

#### Reference

Chatterjee, A. K. et al. *J. Med. Chem.*, 2012, 55, 4244-4273.

### Metabolism of Anti-malarials

The table below presents the **microsomal extraction ratio (ER)** for different anti-malarial compounds (27, 28, 29, 31) across mouse, rat, and human microsomes.

| Entry  | Mouse ER | Rat ER | Human ER |
|--------|----------|--------|----------|
| **27** | 0.51     | 0.63   | 0.52     |
| **28** | 0.40     | 0.89   | 0.55     |
| **29** | 0.41     | 0.79   | 0.47     |
| **31** | 0.87     | 0.96   | 0.79     |

#### Reference

Chatterjee, A. K. et al. *J. Med. Chem.*, 2012, 55, 4244-4273.
