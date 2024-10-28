# Module 1

## Interview

## Routes of Administration

The US FDA recognizes over 100 different routes of administration -
<https://www.fda.gov/drugs/data-standards-manual-monographs/route-administration>
. Route of administration is just one of many types of information that the FDA and other health authorities record on approved drugs.

### Learning objectives

- Describe common routes of administration.
- Connect pharmacokinetic (PK) parameters to route of administration.

### Systemic administration

- Involves exposure of the entire body to the drug dose.
- **Enteral** – via the GI tract, often as an oral pill (PO).
- **Parenteral** – not via the GI tract:
  - **Injection**:
    - Intravenous (IV)
    - Subcutaneous (SC)
    - Intramuscular (IM)
    - These methods **avoid hepatic first-pass effect**.
  - Surgical implant.
  - Transdermal patch.

### SC and IM injection

- Both create a reservoir or "depot" of a drug at the site of injection.
- Absorption involves diffusion of the drug from the site of injection to the circulatory system.
- No first-pass effect, but bioavailability is likely **less than 100%** (due to incomplete absorption).

### Local administration

- Administration directly to a drug’s site of action (i.e., not systemic administration).
- **Examples**: Lotions, creams, nasal sprays, eye drops, and inhaled drugs.
- Requires direct access to the target or site of action.
- Can reduce adverse events encountered with systemic exposure.

### Key PK parameters relevant to most routes of administration

- **Clearance (CL)**
- **Volume of distribution (Vd)**
- **Half-life (T1/2)**
- **Bioavailability (F)**

## IV Bolus Cp Time Curves

### Learning objectives

- Summarize ADME concepts.
- Sketch Cp-time curve of an IV bolus.
- Calculate PK parameters from IV bolus Cp-time data.

### ADME

- **Absorption**: Movement of a drug from the site of administration to systemic circulation.
- **Distribution**: Movement of a drug to and from circulation and various tissues and organs.
- **Metabolism**: Chemical modification of a drug, often associated with the liver (hepatic metabolism).
- **Excretion**: Removal of intact drug, often associated with the kidneys (renal filtration) and liver (biliary secretion).

### IV bolus Cp-time data

- **Cp-time curve**: Shows the plasma concentration (Cp) over time after an IV bolus injection.
- **AUC (Area Under the Curve)**: Represents the total exposure of the drug in the plasma over time, measured in ng·h/mL.
- **Clearance (CL)**: Calculated as CL = Dose (D) / AUC, representing the volume of plasma cleared of the drug per unit time (e.g., vol/t/kg).
- **Elimination**: The rate of drug removal from the plasma (ΔCp/Δt).

### IV bolus log Cp-time data

- **kel (elimination rate constant)**: Calculated as kel = -2.303 × slope (time⁻¹), where the slope is derived from the log Cp-time curve.
- **T1/2 (half-life)**: T1/2 = 0.693 / kel, which represents the time required for the drug concentration to decrease by half.
- **Vd (volume of distribution)**: Vd = 0.693 × T1/2 / CL (clearance), representing the volume in which the drug is distributed in the body.

### Key pharmacokinetic parameters

- Three key parameters:
  - **Half-life (T1/2)**,
  - **Clearance (CL)**,
  - **Apparent volume of distribution (Vd)**.
  
- If any two of these parameters are known, the third can be estimated using the equation:
  - T1/2 = 0.693 × (Vd / CL)
  
- **Units**:
  - T1/2: hours,
  - CL: mL/min/kg,
  - Vd: L/kg.

- Expanded equation with conversion factors:
  - T1/2 (h) = 0.693 × (Vd [L/kg] × 1,000 mL/L) / (CL [mL/min/kg] × 60 min/h).

- Simplified equation:
  - T1/2 (h) = 11.55 × (Vd [mL/kg] / CL [mL/h/kg]).

## Oral Dose Cp Time Curves

### IV bolus vs. oral Cp-time data

- **IV bolus (left graph)**:
  - Immediate peak in plasma concentration (Cp).
  - Gradual elimination phase as drug is cleared from the system.

- **Oral administration (right graph)**:
  - **Tmax**: Time to reach peak concentration (**Cmax**).
  - **Absorption phase**: Drug slowly enters the bloodstream before reaching **Cmax**.
  - **AUC (Area Under the Curve)**: Represents total drug exposure.
  - **Elimination phase**: Follows absorption as the drug is cleared from the system.

### Oral bioavailability

- **IV curve**:
  - Dose = 20 mg
  - AUC = 1429 ng·h/mL

- **Oral curve**:
  - Dose = 20 mg
  - AUC = 1066 ng·h/mL

- **Bioavailability (F)**:
  - \( F = \frac{AUC_{PO}/dose_{PO}}{AUC_{IV}/dose_{IV}} \)
  - \( F = 0.75 \) or **75%**

#### Factors affecting absorption

- Poor solubility
- Low membrane permeability
- Efflux transporters
- Gut lining metabolism (gastric first-pass effect)
- Liver metabolism (hepatic first-pass effect)

### Impact of poor metabolic stability

#### For **oral drugs**

- Low stability → Low absorption → Low bioavailability (**F**) → Low exposure

#### For **all drugs**

- Low stability → High hepatic clearance (**CL_H**) → Short half-life (**T₁/₂**) → Low exposure
