from module_1 import parse_fasta_string
from module_2 import generate_searchable_strands
from module_3 import find_comprehensive_orfs
from module_4 import analyze_protein_properties
from module_5 import filter_and_annotate_proteins
from module_6 import generate_final_report
from information import *

def main():
    fasta_content_valid = """>educational_input | protein_len_5_and_4
# This sequence contains junk characters and two potential proteins
AGCT NNN ATG AAA GCA TTT GGG TAG GTC
# The sequence for the reverse protein is embedded here
TCA GGA GGA GGA CAT
"""
    
    print("----------- STARTING BIOFORGE PIPELINE -----------")
    
    print("\n--- [MODULE 1] PARSING INPUT ---")
    parsed_data = parse_fasta_string(fasta_content_valid)
    print(f"Output of Module 1: {parsed_data}")
    
    print("\n--- [MODULE 2] GENERATING STRANDS ---")
    strands = generate_searchable_strands(parsed_data['sequence'])
    print(f"Output of Module 2: {strands}")
    
    print("\n--- [MODULE 3] FINDING ORF CANDIDATES ---")
    orf_candidates = find_comprehensive_orfs(strands, CODON_MAP)
    print(f"Output of Module 3: {orf_candidates}")
    
    print("\n--- [MODULE 4] ANALYZING PROTEIN PROPERTIES ---")
    analyzed_proteins = analyze_protein_properties(orf_candidates)
    print(f"Output of Module 4: {analyzed_proteins}")
    
    print("\n--- [MODULE 5] FILTERING & ANNOTATING ---")
    final_proteins = filter_and_annotate_proteins(analyzed_proteins, min_len=4)
    print(f"Output of Module 5: {final_proteins}")
    
    print("\n--- [MODULE 6] GENERATING FINAL REPORT ---")
    final_report = generate_final_report(final_proteins)
    print("\n>>>>>>>>>> FINAL REPORT <<<<<<<<<<")
    print(final_report)
    print("----------------------------------------------------")

if __name__ == "__main__":
    main()