# Module 3

## Fragment-Based Drug Discovery

### Learning objectives

- Contrast fragment libraries against traditional libraries
- List characteristics of fragment library screening

### Traditional vs. fragment libraries

| library type    | traditional     | fragment      |
|-----------------|-----------------|---------------|
| typical size    | ≥ 1,000,000      | 1,000 – 3,000 |
| MW of members (g/mol) | ≥ 300         | ≤ 300         |
| HTS?            | Y               | N             |
| potency of hits (Kd) | 1-10 μM      | 0.1-1.0 mM    |

### Screening for low potency hits

- Detecting low potency hits requires screening library members at high concentrations (~1 mM).
- Library members must have good aqueous solubility.
- Common assay formats: NMR, SPR, and x-ray crystallography.
- Only affords binding data.

### Fragment hits

- Fragment hits are normally not discovered in other libraries.
- Fragment hits are less biased for a specific target.
- Fragment hits often support computational searches of active molecules from traditional libraries.
- Fragment hits may be "linked" to increase potency.

## In Silico Screening

### Learning objectives

- Describe the use of molecular docking to estimate binding energies.
- List new technologies that improve computational methods.

### In silico screening workflow

1. 3-D structure of target (x-ray structure)
2. Computer model ("homology modeling")
3. Predict target binding sites
4. Fit molecules into binding sites ("docking")
5. Estimate binding energies
6. Experimentally validate predicted hits

### Docking without a target structure

- Traditional docking requires a target structure.
- Phenotypic drug programs do not have a known target.
- Artificial intelligence algorithms may be able to infer a target structure based on known active molecules.
- New AI methods are an area of potential growth.

## Hit Validation

### Learning objectives

- Define the concept of validating target engagement.
- Describe x-ray crystallography as a validation method.

### Filtering hits

- **Primary HTS**: 10⁵ - 10⁹ compounds
- **Confirmation & counterscreens**: 10³ - 10⁴ compounds
- **Validation, SAR, biophysics, & structural biology**: 10¹ - 10³ compounds
- **Start med chem**

### Questions to address

- Confirm binding?
- Binding stoichiometry?
- Rate of binding/release?
- Binding site?

### Validation via x-ray crystallography

- **Co-crystal**: complement factor B & the ligand shown in the structure
- Citation: Mainolfi, N., et al. *J. Med. Chem.* 2020, 63(11), 5697-5722. [RCSB link](https://www.rcsb.org/3d-view/ngl/6t8v)

### Identification of intermolecular forces

- Co-crystals can reveal intermolecular forces, including:
  - Hydrogen bonds
  - Hydrophobic effects
  - Steric clashes
- [RCSB link](https://www.rcsb.org/3d-view/ngl/6t8v)

### Hit Validation Methods Overview

- **Purpose of Hit Validation**: Confirm that a hit physically binds to its target, essential for drug discovery.
- **X-ray Crystallography**:
  - Visualizes interactions between protein and ligand.
  - Predicts structural changes to improve binding/potency.
  - Limitation: Not all proteins form x-ray-quality crystals.
- **Other Methods**:
  - **Surface Plasmon Resonance (SPR)** and **Differential Scanning Fluorimetry (DSF)**:
    - Fast screening techniques, requiring minimal protein.
    - Used to validate hits from HTS.
  - **Heteronuclear Single Quantum Coherence NMR (HSQC NMR)**:
    - Maps hit binding to specific protein residues.
    - Limitation: Requires 15N-enriched protein samples.
  - **Isothermal Titration Calorimetry (ITC)**:
    - Measures binding thermodynamics (ΔH, Ka, Kd).
    - Does not provide structural data but offers binding energetics.

### HSQC NMR and ITC for Hit Validation

- **HSQC NMR**:
  - Detects interactions between 15N and 1H atoms in protein.
  - **Overlay spectra** of bound vs. unbound protein show amino acids near binding site.
  - **Advantage**: Provides evidence of hit engagement and binding site location.
  - **Limitation**: Requires preparation of 15N-enriched proteins.

- **Isothermal Titration Calorimetry (ITC)**:
  - Measures energy released during hit-protein binding.
  - **Key Output**: Binding enthalpy (ΔH), stoichiometry, association constant (Ka), and dissociation constant (Kd).
  - **Benefit**: Provides detailed thermodynamic data, confirming binding strength and interaction dynamics.
  - **Limitation**: Lacks structural insights but complements HSQC and x-ray data.

## Future Direction in Screening

### Learning objectives

- List some features of a DNA-encoded library (DEL).
- Describe the use of DELs in screening.
