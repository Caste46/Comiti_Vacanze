def to_rna(dna_strand):
    rna = ""
    for k in range(len(dna_strand)):
        if(dna_strand[k] == 'G'):
            rna = rna + 'C'
        elif(dna_strand[k] == 'C'):
            rna = rna + 'G'
        elif(dna_strand[k] == 'T'):
            rna = rna + 'A'
        elif(dna_strand[k] == 'A'):
            rna = rna + 'U'
    return rna