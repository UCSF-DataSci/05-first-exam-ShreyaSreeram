This project structure organizes a bioinformatics workflow including data handling, script execution, and result summarisation.

How to run the different scripts: 

1) setup_projects.sh - In the parent directory, execute: 
bash setup_project.sh

2) generate_fasta.py - make sure you're in the parent directory of the project and execute using: 
python bioinformatics_project/scripts/generate_fasta.py 

3) dna_operations.oy 0 - make you're in the bioinformatics_project directory, and execute using: 
python scripts/dna_operations.py "CCTCAGC" 

4) find_cutsites.py - make sure you're in the bioinformatics_project directory and execute using: 
python scripts/find_cutsites.py data/random_sequence.fasta "G|GATCC"