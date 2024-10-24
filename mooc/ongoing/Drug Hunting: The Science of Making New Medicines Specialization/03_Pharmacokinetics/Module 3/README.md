# Module 3

## Plasma Protein Binding

### Learning objectives

- Define plasma protein binding (PPB)
- List the most relevant proteins for PPB
- Describe the importance of measuring PPB

### Plasma protein binding (PPB)

- **Plasma protein** + **drug** (free, unbound) ↔ **plasma-drug protein** (bound)
  
- **Human plasma protein content**: 60-80 mg/mL
  - 50-60% **albumin**: binds acidic & neutral drugs
  - 3% **α1-acid glycoprotein**: binds basic drugs

### Why measure PPB?

**Free drug hypothesis**:  
\[ C_p (\text{unbound}) = \text{unbound concentration at site of action} \]

- PPB can affect drug disposition (distribution).
- PPB can affect clearance.
- PPB can vary among preclinical species and may be affected by disease states.
- Knowing PPB assists in human dose prediction and evaluating safety margin.

### Measuring PPB

- **Three common methods for PPB measurement**:
  - Equilibrium dialysis
  - Ultrafiltration
  - Ultracentrifugation

- **Relationships of values**:
  - \( f_u \): fraction unbound
  - \( C_p = C_p \) (bound) + \( C_p \) (unbound)
  - \( C_p \) (unbound) = \( C_p \times f_u \)

### PPB considerations

- **Interspecies PPB variability**:
  - \( f_u = 0.016 \) in human
  - \( f_u = 0.60 \) in dog
  - 40-fold difference

- **Concentration effects**:
  - PPB can be saturated at higher \( C_p \)
  - \( f_u = 0.1 \) at lower \( C_p \)
  - \( f_u = 0.5 \) at higher \( C_p \)

## Drug-Drug Interactions

### Learning objectives

- Define drug-drug interactions (DDIs)
- Describe how DDIs are identified
- Visualize how DDIs affect C\_p-time curves of drugs

### Drug-drug interactions (DDI)

**definition**  
an interaction between a drug and another substance that prevents the drug from performing as expected

**consequence**  

- increase in exposure (toxicity)  
- decrease in exposure (loss of efficacy)  

### Actors in DDIs

**perpetrator**  
substance (e.g., drug) that causes the DDI  

- inhibit or induce metabolic enzymes or transporters  
- potency measured through in vitro assays  
- inhibitors — reversible or time-dependent  
- assays may include liver microsomes, hepatocytes, or cells expressing the transporter of interest

**victim**  
drug affected by the perpetrator

### Level of DDI risk

**reversible CYP inhibition**

- **low risk**: IC\_{50} > 10 μM  
- **moderate risk**: IC\_{50} 1-10 μM  
- **high risk**: IC\_{50} < 1 μM  

### Victim DDI liability assessment

- requires thorough understanding of a compound’s:  
  - elimination  
  - clearance & fraction metabolized  
  - dependence upon transporter proteins

- victim DDI studies:  
  - often use liver microsomes + inhibitors  
  - recombinant CYP 450 enzymes  
  - identify active CYP isoform and fraction metabolized

### Effect of drug-drug interactions

1. **Drug A alone**  
   - The concentration of drug A (C\_p) follows a normal pharmacokinetic profile.  
   - The drug reaches a peak concentration, then gradually decreases over time.  
   - Ideally, the concentration remains within the therapeutic window (between efficacy and toxicity lines).

2. **Drug A + inhibitor**  
   - Inhibitors can increase the concentration of drug A by slowing its metabolism or elimination.  
   - As a result, the C\_p increases, potentially crossing the toxicity threshold, increasing the risk of adverse effects.  
   - The concentration remains higher for a longer period, which can be dangerous if the drug is not adjusted.

3. **Drug A + inducer**  
   - Inducers can lower the concentration of drug A by speeding up its metabolism or elimination.  
   - This results in a lower C\_p, which may drop below the efficacy line, making the drug less effective or completely ineffective.  
   - The drug may need a higher dose or more frequent administration to maintain therapeutic levels.

#### Notes

- **Inhibitors**: Common in drug-drug interactions, especially with drugs metabolized by enzymes like CYP450. They slow down the breakdown of drugs, leading to increased concentrations.
- **Inducers**: Increase enzyme activity, causing drugs to be cleared more quickly, reducing their therapeutic effects.
- **Toxicity vs. Efficacy**: The balance between the therapeutic dose (effective) and harmful dose (toxic) is crucial in managing drug interactions.

## Pharmacokinetic/Pharmacodynamic Relationships

### Learning objectives

- Define PK/PD relationship (PK: body does to drug; PD: drug does to body)
- List the roles of PK/PD studies during drug discovery
- Differentiate between direct and indirect PK/PD relationships

### PK, PD, & PK/PD

- **Pharmacokinetics (PK)**: Focuses on drug exposure, represented by concentration (Conc.) over time.  
  - ADME (Absorption, Distribution, Metabolism, and Excretion) affects how the drug concentration changes over time.  
  - The left graph shows how drug concentration peaks and decreases as the drug is absorbed and then eliminated.

- **Pharmacodynamics (PD)**: Focuses on the effect of the drug over time.  
  - The graph on the right shows how the effect increases, plateaus, and decreases over time.  
  - This represents how the drug's efficacy is linked to its concentration and how long it remains effective in the body.

- **PK/PD Relationship**: Links the exposure (PK) to the effect (PD).  
  - The middle graph shows the exposure-effect relationship, illustrating how increased drug concentration correlates with increased effect, up to a certain point where the effect levels off.

#### PK/PD links

- **Concentration**
- **Effect**
- **Time**  

The balance between these factors is crucial for understanding how a drug works and optimizing dosing regimens.

### Roles of PK/PD

**Preclinical phases**  

- Assist in the design of pharmacology studies  
- Select the most promising compound  
- Ensure target engagement  
- Predict human PK/PD

**Clinical phases**  

- Define drug sampling times  
- Determine dosing regimen

### PK/PD → Direct relationship

- Plasma concentration (C) and effect (R) are linked with **no time lag**.
- The concentration and effect relationship is described using models such as linear, log-linear, and E\_max models.

In the graphs:

- The top graph shows that the effect (R) closely follows the plasma concentration (C) over time, with no delay.
- The bottom graph illustrates the relationship between drug concentration and effect, where EC\_{50} represents the concentration that produces 50% of the maximum effect (E\_max).

This direct relationship indicates that changes in drug concentration immediately affect the pharmacodynamic response.

### PK/PD → Indirect relationship

- In an indirect relationship, there is a **delay** between plasma concentration (C) and effect (R).
- The effect lags behind the concentration, often forming a hysteresis curve (seen in the graph).

#### Delays arise from

- **Distribution lags**: The drug takes time to distribute to the site of action.
- **Active metabolite formation**: The drug's active form may need to be produced through metabolism.
- **Downstream signaling**: Time required for cellular signaling pathways to trigger effects.
- **Gene expression regulation**: Time needed for transcriptional or translational processes to produce the drug's intended effect.

In the graph:

- The top graph shows the time-lagged relationship between concentration (C) and effect (R), where effect peaks after concentration.
- The bottom graph depicts the hysteresis curve, illustrating how the effect trails behind changes in concentration.

This relationship shows that the effect does not directly follow changes in drug concentration but is delayed due to various physiological processes.

### Is PD driven by C\_{max} or AUC?

**Dose fractionation study**  

- **Group 1**: Receives a single, large dose (blue curve).
- **Group 2**: Receives multiple, small doses (red curve).

#### Key points

- **C\_{max} differs** between the two groups, with the single large dose reaching a higher C\_{max} than the fractionated doses.
- **AUC is the same** for both groups, meaning the total drug exposure over time is equivalent.
- **AUC-driven PD** is more common than C\_{max}-driven PD, suggesting that the overall exposure (AUC) often correlates better with pharmacodynamic effects than the peak concentration (C\_{max}).

In the graph, the single large dose reaches a high C\_{max} but rapidly declines, while the fractionated doses show multiple smaller peaks, maintaining overall AUC equivalence.

## Anticipated Human Dose

### Learning objectives

- Define anticipated human dose (AHD)
- List data that allow prediction of AHD
- Describe the importance of AHD

### Anticipated human dose (AHD)

- **Volume (Vd)** and **clearance (CL)** are used to calculate the drug's **half-life (t₁/₂)** and **bioavailability (%F)**, which influence drug exposure.
- **Exposure (AUC, C\_{max}, C\_{min})** is determined by pharmacokinetic parameters and is linked to the desired PK/PD target.
- The **PK/PD target** (AUC, C\_{max}, C\_{min}) helps define dose and dosing frequency through **quantitative PK/PD modeling**.
- Data for these calculations are predicted from preclinical studies, including animal pharmacology, preclinical PK studies, and in vitro PKPD models.

#### Sources for AHD prediction

- **Animal PK studies**
- **In vitro PK models**
- **Animal pharmacology**
- **In vitro PKPD models**

By integrating these predictions, the anticipated human dose can be estimated to guide clinical dosing strategies.

### Keys to successful anticipated human dose prediction

#### Human PK prediction

- **Physiochemical properties**: Understanding the chemical and physical characteristics of the drug.
- **Mechanistic models for clearance (CL)**: Predicting how the drug will be cleared from the body.
- **In vitro to in vivo correlation**: Bridging laboratory data with expected outcomes in living organisms.
- **Cross-species PK**: Using data from animal models to predict human pharmacokinetics.
- **Physiologically based PK models (PBPK)**: Advanced models incorporating organ-specific drug distribution and metabolism.

#### Human PK/PD

- **PK/PD link to inform targeted exposure**: Using the PK/PD relationship to determine the correct dose for therapeutic efficacy.
- **In vitro/in vivo potency (K\_D, K\_on, K\_off, EC\_{90})**: Key pharmacodynamic parameters that inform drug activity at the target.
- **Expression data across species**: Evaluating drug target expression in different species to aid in dose prediction.
- **Human disease knowledge, competitor data & underlying assumptions**: Leveraging clinical insights and comparative data to fine-tune dose estimates.

#### Quantitative PK/PD Models

These models integrate the above data to predict the **anticipated human dose** that will meet the **PD target for efficacy**, ensuring adequate target engagement at the optimal dose.

The graph illustrates how dose correlates with target engagement, with the predicted dose achieving the desired pharmacodynamic response.

### Importance of anticipated human dose

**Clinical candidate selection**

- **Determining first-in-human dose**: Identifying the appropriate starting dose for clinical trials.
  
- **Answering PK-related questions**:
  - **Drug accumulation**: Does the drug accumulate in the body over time?
  - **Dose non-linearity**: Is the dose-exposure relationship proportional?

- **Answering safety-related questions**:
  - **Safety margin**: The range between the effective dose and the dose that causes side effects.
  - **Exposure in preclinical toxicity studies**: Assessing exposure levels observed in animal studies.
  - **Drug-drug interaction liability**: Assessing risks of interactions with other medications.
  - **Off-target effects**: Identifying unintended effects on other biological targets.

- **Answering efficacy-related questions**:
  - **Degree of target occupancy**: Evaluating how much of the target is bound by the drug at the anticipated dose.

- **Understanding the impact on**:
  - **Patient variability**: Accounting for differences in how patients respond to the drug.
  - **Cost of goods**: Understanding the cost implications of the dosing regimen.
  - **Patient compliance**: Ensuring that the dosing schedule is manageable for patients.
  - **Compatible schedules for drug combinations**: Adjusting dosing to work with other drugs.
  - **Formulation**: Considering how the drug is delivered (e.g., tablet, injection).
