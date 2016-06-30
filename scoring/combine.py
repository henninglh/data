#!/usr/bin/env python
import sys

if len(sys.argv) < 4:
    sys.exit('./combine.py <gene-file> <score-file> <output-file>')
    exit()

genes_filename = sys.argv[1]
scores_filename = sys.argv[2]
combined_filename = sys.argv[3]

with open(genes_filename, 'r') as genes,\
        open(scores_filename, 'r') as scores,\
        open(combined_filename, 'w') as combined:

    genes.readline() # remove header
    scores.readline() # remove header
    approved_genes = set((line.rstrip() for line in genes.readlines()))

    for line in scores.readlines():
        gene_name, score  = line.split('\t')

        if gene_name in approved_genes:
            combined.write(line)

