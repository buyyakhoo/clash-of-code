nucleotide = {'A' : 0, 'C' : 0, 'G': 0, 'T': 0}
for i in input():
    nucleotide[i] += 1
print(nucleotide['A'], nucleotide['C'], nucleotide['G'], nucleotide['T'])