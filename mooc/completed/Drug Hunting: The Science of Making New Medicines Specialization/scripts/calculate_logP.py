import argparse
from rdkit import Chem
from rdkit.Chem import Descriptors

# Set up argument parser
parser = argparse.ArgumentParser(
    description="Calculate the logP of a molecule from a SMILES string."
)
parser.add_argument("smiles", type=str, help="SMILES string of the molecule")

# Parse the arguments
args = parser.parse_args()

# Create a molecule object from the SMILES string
molecule = Chem.MolFromSmiles(args.smiles)

# Calculate the logP (lipophilicity)
logP = Descriptors.MolLogP(molecule)

# Output the consensus log P to two decimal places
print(f"Consensus log P: {logP:.2f}")
