#!/usr/bin/env python

import sys

with open(sys.argv[1].strip(), 'r') as genes,\
        open('genes.txt', 'w') as single_genes:

    genes.readline()

    for line in genes.readlines():
        g = line.split('\t')[2]
        if len(g) > 1:
            for gene in g.split(','):
                single_genes.write('{}\n'.format(gene.strip()))
