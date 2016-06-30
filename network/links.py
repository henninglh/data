#!/usr/bin/env python
import sys

with open('mitab_clean.txt', 'r') as mitab_file,\
        open('approved_genes.txt', 'r') as gene_file,\
        open('links/' + sys.argv[1].strip(), 'w') as links_file:

    genes = dict((line.strip().split('\t') for line in gene_file.readlines()))
    
    for line in mitab_file.readlines():
        splitline = line.split('\t')
        source = splitline[0].strip()
        target = splitline[1].strip()

        if source in genes and target in genes:
            links_file.write('{}\t{}\n'.format(genes[source], genes[target]))
