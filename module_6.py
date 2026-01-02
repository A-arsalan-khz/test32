def generate_final_report(final_proteins):
    sorted_proteins = sorted(final_proteins, key=lambda p: p.get('mw', 0), reverse=True)
    
    if not sorted_proteins:
        return "======= BioForge Analysis Report =======\nNo significant proteins found."
        
    summary = "======= BioForge Analysis Report =======\n"
    summary += f"{'ID':<12}{'Length':<8}{'MW (kDa)':<12}{'Strand':<20}\n"
    summary += "-" * 52 + "\n"
    for p in sorted_proteins:
        mw_kda = p.get('mw', 0) / 1000
        summary += f"{p['protein_id']:<12}{p['length']:<8}{mw_kda:<12.2f}{p.get('strand', ''):<20}\n"
        
    return summary