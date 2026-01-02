def generate_searchable_strands(dna_sequence):
    forward_strand = dna_sequence
    
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement_strand = ""
    for base in forward_strand:
        complement_strand += complement_map[base]
        
    reverse_complement_strand = complement_strand[::-1]
    
    return {'forward': forward_strand, 'reverse_complement': reverse_complement_strand}