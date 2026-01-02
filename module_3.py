def find_comprehensive_orfs(strands, codon_map):
    orf_candidates = []
    stop_codons = {'UAA', 'UAG', 'UGA'}
    start_codon = 'AUG'

    for strand_name, dna_strand in strands.items():
        for frame_index in range(3):
            mrna = dna_strand[frame_index:].replace('T', 'U')
            
            i = 0
            while i < len(mrna):
                codon = mrna[i : i+3]
                if codon == start_codon:
                    protein_sequence = []
                    for j in range(i, len(mrna), 3):
                        codon = mrna[j : j+3]
                        if len(codon) < 3:
                            break
                        
                        if codon in stop_codons:
                            if protein_sequence:
                                orf_data = {
                                    'sequence': "".join(protein_sequence),
                                    'strand': strand_name,
                                    'start_pos': i + frame_index
                                }
                                orf_candidates.append(orf_data)
                            break
                        
                        amino_acid = codon_map.get(codon, '?')
                        protein_sequence.append(amino_acid)
                i += 1
                
    return orf_candidates