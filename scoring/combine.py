#!/usr/bin/env python
import sys

dragon_filename = sys.argv[1]
disgen_filename = sys.argv[2]
combined_filename = sys.argv[3]

with open(dragon_filename, 'r') as dragon,\
        open(disgen_filename, 'r') as disgen,\
        open(combined_filename, 'w') as combined:

    dragon.readline() # remove header
    disgen.readline() # remove header
    approved_genes = set((line.rstrip() for line in dragon.readlines()))

    for line in disgen.readlines():
        gene_name, score  = line.split('\t')

        if gene_name in approved_genes:
            combined.write(line)

