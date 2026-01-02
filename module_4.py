from information import AMINO_ACID_WEIGHTS, WATER_MW

def analyze_protein_properties(orf_list):
    analyzed_list = []
    for protein_data in orf_list:
        seq = protein_data['sequence']
        
        total_weight = 0
        for amino_acid in seq:
            total_weight += AMINO_ACID_WEIGHTS.get(amino_acid, 0)
        
        mw = total_weight - (len(seq) - 1) * WATER_MW if seq else 0
        protein_data['mw'] = round(mw, 2)
        
        analyzed_list.append(protein_data)
            
    return analyzed_list