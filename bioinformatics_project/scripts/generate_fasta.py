import random
import textwrap

def generate_random_dna_sequence(length):
    """This function generates a random DNA sequence of specified length."""
    bases = 'ACGT'
    return ''.join(random.choices(bases, k=length))

def save_sequence_to_fasta(sequence, filename):
    """This function saves a DNA sequence to a FASTA file with specified formatting."""
    with open(filename, 'w') as file:
        file.write('>RandomSequence\n')
        formatted_sequence = '\n'.join(textwrap.wrap(sequence, 80))
        file.write(formatted_sequence)


random_sequence = generate_random_dna_sequence(1000000)

save_sequence_to_fasta(random_sequence, 'bioinformatics_project/data/random_sequence.fasta')

#Print confirmation message 
print("Random DNA sequence generated and saved to random_sequence.fasta")