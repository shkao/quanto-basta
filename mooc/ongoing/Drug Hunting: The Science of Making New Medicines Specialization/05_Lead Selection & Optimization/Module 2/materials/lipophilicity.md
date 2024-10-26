Early in a drug discovery program, one physicochemical property is often mentioned more than others. That one property is _lipophilicity_. Lipophilicity is the ability of a compound to dissolve in a non-polar solvent or medium.

In a drug program, lipophilicity is most often quantified through a parameter called log _P. P_ stands for the _partition coefficient_ and represents the position of the equilibrium of a compound between immiscible polar and non-polar solvents. The identity of the solvents can vary, but in drug discovery, the polar solvent is almost always water, and the non-polar solvent is normally 1-octanol. Sometimes _P_ is written as _P_<sub><span>o/w</span></sub> to specify an octanol/water solvent system, which closely mimics the interface between cell membranes and an aqueous environment. The partition coefficient is calculated by taking the ratio of the concentration of the compound in the octanol layer over the concentration in the water layer. Because values for _P_ can vary across many orders of magnitude, lipophilicity is normally reported as log _P_.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/E8tpC3P0SAKWZVHqW9Aeag_604dc391679a421ebc29543389431ea1_image.png?expiry=1729987200000&hmac=nhC4rSVShIfz9JeMXlYIJXcb-UPK-ZJUdR4sIbOdUvc)

Why are discussions about lipophilicity so prevalent in lead selection and optimization? Lipophilicity often correlates inversely with aqueous solubility and can even be predictive of membrane permeability and therefore oral absorption. In some cases, high lipophilicity is associated with higher toxicity. Log _P_ values for a molecule can often be accurately predicted without requiring any experimental _P_ measurement. These predicted or calculated log _P_ values are often written as clog _P_ (pronounced see-log _P_). Calculations are indeed so common and easy to perform that most reported log _P_ values, whether recorded as log _P_ or clog _P_, are calculated and not determined experimentally. Lipophilicity is therefore a physicochemical parameter that is both very easy to calculate and provides insight into ADME properties.

For small molecule, orally-delivered drugs, the goal of a drug-hunting team is often to maintain the log _P_ or clog _P_ of compounds in the lead series at or below 5.0. A low log _P_ value, however, does not guarantee oral absorption just as a high log _P_ value does not prohibit absorption. The log _P_ value of less than 5.0 is simply a common guideline. Absorption and oral availability will ultimately be confirmed through more informative in vitro ADME and in vivo PK studies. Because the lipophilicity of a compound tends to increase during lead optimization as both potency and target selectivity are improved, many medicinal chemists advocate for hits to a log _P_ of 3.0 or less. This restriction provides some headroom for likely lipophilicity gains during optimization so that the final lead can still have a log _P_ below 5. Note that hits and leads can have too low of lipophilicity to passively diffuse across membranes, but the challenge for most hits and leads, which are organic molecules, is that lipophilicity tends to be too high.

Many hits, leads, and drugs contain acidic or basic groups. The partitioning of acidic and basic molecules between octanol and water is greatly affected by ionized functional groups. For example, an acidic molecule will be almost completely ionized at pH 7, and only the neutral form will significantly partition into the octanol layer. The values of clog _P_ only estimate the partitioning of the neutral form and overlook any effects of ionization. To more completely describe the partitioning and lipophilicity of both the neutral and charged forms, scientists use a parameter called log _D_. _D_ stands for the _distribution coefficient_, which is completely unrelated to the volume of distribution. The distribution coefficient tries to include the concentration of all species in both layers. Very often, the concentration of ionized forms in the octanol layer is assumed to be 0.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/T0vG2Wd3QLqVUzfp43vi9g_deb0c74c3ee6454fbc71c9310e272fa1_image.png?expiry=1729987200000&hmac=48vmptHrt4sdqCv8v51yzLirsZ2-fwEEVVRXFNfjvnU)

With this assumption, log _D_ values can be calculated based on a compound’s clog _P_ and the pK<sub><span>a</span></sub> of any functional groups in the molecule. The log _D_ of an ionized molecule will always be lower than its log _P._ If a compound is not ionized, then log _P_ and log _D_ will be equal. Because the ionization of acidic and basic groups depends on the pH of the medium, log _D_ values often include a subscript to denote the pH, e.g., log _D_<sub><span>7.4</span></sub>. A drug-hunting team may focus on log _D_ instead of log _P_ if the team feels that log _D_ is a better predictor of how a compound will perform in future evaluations.

Many websites provide calculations of lipophilicity, normally as log _P_. One such site is [SwissADME](http://www.swissadme.ch/index.php), which calculates many other properties as well. To use SwissADME, navigate to the site. The molecule you want to analyze can be entered in one of two ways. One, the molecule can be drawn through a simple drawing tool. Two, a text form of the molecule (called a SMILES – simplified molecular-input line-entry system) can be copied-pasted into an input box. We will use option two for the questions below.

First, get comfortable using SwissADME. The text form of aspirin or acetylsalicylic acid is CC(=O)OC1=CC=CC=C1C(=O)O. Copy this text (the entire text but not the period at the end) and paste it into the SMILES input box on SwissADME.

Press the red “Run!” button, allow the page to refresh, and scroll down to see the predicted properties of aspirin. (Note: depending on your browser settings, you may or may not see a structure shown for the molecule)

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/YJ9AUbDnRjWHOi4VyWZKXQ_eb58bd3b7e574918a8c3e04015f262a1_image.png?expiry=1729987200000&hmac=h_755mNCIzjkhXWZJoHfvUHIuVkd9TES07GyJKBltB8)

To the bottom left of the calculated properties is a list of multiple calculated log _P_ values based on different calculation methods. The last line is the “consensus” value and is the average of the other values. The consensus log _P_ of aspirin is 1.28.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Ed_cJx6RTuiC3YYdwMrCog_3b81712c4f2e45cfa270f4b7205efda1_image.png?expiry=1729987200000&hmac=ewsumB84y31ylGHWbFzt21FXG_BIkyO9dqPLFNcargg)