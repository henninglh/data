#!/usr/bin/env python
import sys

with open('curated_gene_disease_associations.tsv', 'r') as disgen,\
        open('disgen_clean.tsv', 'w') as pscores:

    disgen.readline() # remoe the header
    pscores.write('geneID\tscore\n') # write header

    for line in disgen.readlines():
        info = line.split('\t')
        gene_name = info[3].strip()
        score = info[2].strip()

        pscores.write('{}\t{}\n'.format(gene_name, score))
