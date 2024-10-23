#!/bin/bash

# Creating the main proejct directory - I created a folder called "bioinformatics_projects" within the parent directory
mkdir -p bioinformatics_project/data bioinformatics_project/scripts bioinformatics_project/results

#creating the empty scripts withiin the folder: 
touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

#empty results file
touch bioinformatics_project/results/cutsite_summary.txt

#empty data file
touch bioinformatics_project/data/random_sequence.fasta

#README.md with project description
echo "This project structure organizes a bioinformatics workflow including data handling, script execution, and result summarization." > bioinformatics_project/README.md

#Making script executable
chmod +x setup_projects.sh

#Confirmation message
echo "Project directory structure created successfully:"
find bioinformatics_project/ -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'