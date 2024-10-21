# Module 2

## Factors in Assay Design

### Learning objectives

- List design factors for robust assays
- Define Z'-factor for assay performance

### Z'-factor

#### Controls

- Max/active → tool compounds
- Min/neutral

Z' = 1 - \[\frac{3(σ_a - σ_n)}{(μ_a - μ_n)}\]

The ideal Z'-factor for a high-throughput assay is between 0.5 and 1. A Z'-factor in this range indicates a robust assay with a good separation between the signal and noise, allowing for reliable detection of active compounds.

### Effect of S:B and S:N

**S:B** – signal-to-background  

- maximum quantifiable signal / average background signal  

**S:N** – signal-to-noise  

- mean quantifiable signal / signal standard deviation  

**Fluorescence**: provides strong assay signal  
**Luminescence**: provides low background noise  

## IC50 and Ki

### Overview

- **IC50** and **Ki** are measures of the potency of small molecules that inhibit enzymes or receptors through reversible binding.
- **IC50**: Concentration of an inhibitor needed to reduce enzyme activity by 50%.
- **Ki**: Dissociation equilibrium constant of the enzyme-inhibitor complex.

### IC50

- Determined via functional assays measuring enzyme activity reduction.
- Affected by substrate concentration; IC50 values are not directly comparable unless assays are conducted under identical conditions.

### Ki

- Determined via binding assays without substrate.
- Represents a constant for a specific enzyme-inhibitor pair, allowing direct comparison of inhibitor potency.

### Cheng-Prusoff Equation

- Describes the relationship between IC50 and Ki.
- Considers substrate concentration ([S]) and Michaelis constant (Km) for conversion between IC50 and Ki.
- Useful for comparing competitive inhibitors' potency.

\[
K_i = \frac{IC_{50}}{1 + \frac{[S]}{K_m}}
\]

Cheng, Y.C.; Prusoff, W.H. Relationship between the inhibition constant (\(K_i\)) and the concentration of inhibitor which causes 50 percent inhibition (\(IC_{50}\)) of an enzyme reaction. *Biochem Pharmacol* **1973**, *22*, 3099-3108.

### Notes

- Ki is preferred for comparing inhibitory potency due to its substrate-independent nature.
- IC50 remains widely used but requires careful consideration of assay conditions for accurate comparisons.

## Molecular Space

### Learning objectives

- Explain the concept of a molecular space  
- Connect the ideas of hits, leads, and drugs

### Molecules in oral drug space

Guida, W. *Med. Res. Rev.* **1996**, *16*, 3-50.

## Compound Libraries

### Learning objectives

- List common types of molecular libraries used in drug discovery  
- Contrast advantages and disadvantages of each type  

### Compound libraries

- Can number several million molecules for a major pharmaceutical company  
- Reflects previous area of research of the company  
- Unlikely to uniformly sample drug-like molecular space  

### Focused screening collections

- Is a subset of the full compound collection  
- Facilitates rapid screening of desired compounds  
- Selection criteria may be based on:  
  → chemical diversity representation  
  → physicochemical properties  
  → known target activity  

### Fragment library

- Collection of a few thousand molecules (~1000's)  
- Smaller molecules (~15 atoms – C, N, O, X, P, S) vs. larger "drug-like" molecules of (~30 atoms)  
- **Advantage** – sample drug space with a small library (FBDD)  
- **Disadvantage** – hits have lower potency  

Schubart, A. et al. *Proc. Natl. Acad. Sci. USA* **2019**, *116*, 7926-7931.

### DNA-encoded library (DELs)

- Massive libraries of over a billion molecules  
- DNA "barcode" attached for identification  
- Relatively easy to prepare a large library  
- More challenging to identify and validate hits from a screen

## High-Throughput Screening and the Primary Assay

### Learning objectives

- List factors considered at the start of a screening campaign  
- Describe aspects of high-throughput screens

### High-throughput screening (HTS)

- Efficient screening of large libraries requires a high-throughput screen.  
- HTS can handle 10,000 to 100,000 compounds/day.  
- Automation through robotics is essential and allows miniaturization to reduce reagent requirements.  

### The primary assay

- Normally a biochemical assay or a cell-based assay  
- Thoroughly developed to ensure precision and accuracy  
- Should tolerate low concentrations (<1%) of DMSO for solubility of library molecules

### Single concentration screening

- Often test at 1 μM or 10 μM  
- Best molecules are “actives”  
- Follow-up testing of actives determines the hit pool  
  - Hits typically have activity greater than 3 standard deviations (>3 s.d.)  
  - Represents about ~0.1% of tested compounds  

## Molecular Properties Summary

### Molecular Weight (MW)

- The molecular weight of oral small molecule drugs is frequently 500 g/mol or less.
- Hits and early leads for an oral drug campaign tend to have lower molecular weights to allow for molecular growth during lead optimization.

### logP – Measure of Lipophilicity

- logP is the logarithm of P, the octanol: water partition constant for a molecule.
- A higher logP value indicates a compound is more lipophilic.
- High lipophilicity can negatively impact drug properties, including aqueous solubility.
- Hits and leads often have a logP of 3 or lower.

### Fsp3 – Fraction of sp3 Hybridized Atoms

- Fsp3 measures the three-dimensional character of a molecule.
- Many molecules in chemical libraries are relatively flat with Fsp3 values closer to 0.
- Molecules with increased three-dimensional character are believed to be better suited to bind to three-dimensional macromolecules like proteins.

## Orthogonal Assays, Counterscreens, and PAINS

### Learning objectives

- Identify potential problems in the primary assay  
- List assays that help confirm primary assay results  

### Potential issues in the primary assay

- Library molecule interacts with the target
- Target activates a reporter enzyme (e.g., luciferases)
- Reporter enzyme generates a signal

Potential issues can arise at any step in this process, such as non-specific interactions, reporter interference, or signal misinterpretation.

### Orthogonal assays

- Detect on-target activity with a different signal method  
- Possible changes: use a different reporter enzyme or directly detect products from target binding  
- True actives should show activity across the primary and orthogonal assays

### Counterscreen assays

- Do NOT test for on-target activity  
- Detect unwanted interaction between the library molecule and other parts of the primary assay (e.g., reporter enzyme)  
- Actives in counterscreens *may* still be hits  

### Pan-assay interference compounds

- Test positively in the primary and orthogonal assays  
- Also called frequent hitters, non-specific binders, or nuisance compounds  
- Often covalently bind proteins non-selectively  
- Can be identified with counterscreens  
