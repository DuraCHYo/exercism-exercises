def to_rna(dna_strand):
    codes = {
        'G':'C',
        'C':'G',
        'T':'A',
        'A':'U'
    }
    return ''.join([codes[x] for x in dna_strand])