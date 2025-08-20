# PolyA Finder

A simple bioinformatics tool to detect polyadenylation signals like `AATAAA` in mRNA sequences.

## Features

- Detects positions of polyadenylation motifs in a given sequence  
- Easily extendable (e.g., mutation detection, FASTA import)  
- Tested with `pytest`  
- Structured as a Python package  

## Installation

```bash
git clone https://github.com/afrakoma-dev/polya_finder.git
cd polya_finder
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

## Example 

```python
from polya_finder.core import find_motifs

seq = "GGCAATAAAGGGAATAAATTT"
print(find_motifs(seq))  # Output: [3, 11]
```

## Run Tests

pytest 

## Project Structure

polya_finder/
├── polya_finder/
│   └── __init__.py
│   └── core.py
│   └── utils.py
├── tests/
│   └── conftest.py
│   └── test_core.py
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt

## Motivation 

This project was created as preparation for a bioinformatics internship focused on polyadenylation site analysis and mutation detection in RNA sequences. 

## ToDo

- Detect point mutations in PolyA motifs (e.g., AATAAA -> AATGAA)
- Read sequences from FASTA files (using Biopython)
- Visualize motif locations 