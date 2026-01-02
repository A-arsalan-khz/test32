def parse_fasta_string(fasta_content):
    lines = fasta_content.strip().split('\n')
    
    if not lines or not lines[0].startswith('>'):
        raise ValueError("Input content does not have standard FASTA format.")
    
    seq_id = lines[0][1:].strip()
    
    raw_sequence = "".join(lines[1:]).upper()
    
    cleaned_sequence = ""
    for base in raw_sequence:
        if base in "ATCG":
            cleaned_sequence += base
            
    return {'id': seq_id, 'sequence': cleaned_sequence}