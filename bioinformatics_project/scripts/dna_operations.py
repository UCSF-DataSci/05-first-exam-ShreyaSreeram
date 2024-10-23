import sys

def complement_seq(sequence):
    """Returns the complement of a DNA sequence."""
    comp_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp_dict[base] for base in sequence.upper())

def reverse_seq(sequence):
    """Returns the reverse of a DNA sequence."""
    return sequence[::-1]

def reverse_complement(sequence):
    """Returns the reverse complement of a DNA sequence."""
    return reverse_seq(complement_seq(sequence))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dna_operations.py <sequence>")
        sys.exit(1)

    sequence = sys.argv[1]
    print(f"Original sequence: {sequence}")
    print(f"Complement: {complement_seq(sequence)}")
    print(f"Reverse: {reverse_seq(sequence)}")
    print(f"Reverse complement: {reverse_complement(sequence)}")