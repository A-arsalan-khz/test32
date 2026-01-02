def filter_and_annotate_proteins(protein_list, min_len=4):
    final_proteins = []
    protein_counter = 0
    for p in protein_list:
        p['length'] = len(p.get('sequence', ''))
        
        if p['length'] >= min_len:
            protein_counter += 1
            p['protein_id'] = f"BFG_{protein_counter:03d}"
            final_proteins.append(p)
            
    return final_proteins