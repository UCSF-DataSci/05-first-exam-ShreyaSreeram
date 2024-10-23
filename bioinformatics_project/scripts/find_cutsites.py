import sys

def read_fasta_file(filepath):
    """This function reads a FASTA file and return the sequence, stripping header and newlines."""
    with open(filepath, 'r') as file:
        return ''.join(line.strip() for line in file if not line.startswith('>'))

def find_cut_sites(sequence, cut_site):
    """This function reads all the start indices of the cut site in the sequence."""
    start = 0
    locations = []
    while True:
        start = sequence.find(cut_site, start)
        if start == -1:
            break
        locations.append(start)
        start += 1  # Move to the next character after the current match
    return locations

def find_pairs(cut_sites, min_distance, max_distance):
    """This function reads all pairs of indices where the distance is within the specified range."""
    pairs = []
    for i in range(len(cut_sites)):
        for j in range(i + 1, len(cut_sites)):
            distance = cut_sites[j] - cut_sites[i]
            if min_distance <= distance <= max_distance:
                pairs.append((cut_sites[i], cut_sites[j], distance))  # I included distance for debugging purposes
    return pairs

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python find_cutsites.py <fasta_path> <cut_site>")
        sys.exit(1)

    fasta_path = sys.argv[1]
    cut_site = sys.argv[2].replace('|', '')
    sequence = read_fasta_file(fasta_path)
    cut_sites = find_cut_sites(sequence, cut_site)

    print(f"Analyzing cut site: {cut_site}")
    print(f"Total cut sites found: {len(cut_sites)}")

    pairs = find_pairs(cut_sites, 80000, 120000)  # Ensure these values are in base pairs
    print(f"Cut site pairs 80–120 kbp apart: {len(pairs)}")
    print("First 5 pairs with distances:")
    for index, pair in enumerate(pairs[:5]):
        print(f"{index + 1}. {pair[0]} - {pair[1]}, Distance: {pair[2]} bp")