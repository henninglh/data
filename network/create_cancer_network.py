#!/usr/bin/env python

with open('CosmicHGNC.tsv', 'r') as cosmic,\
        open('mitab_lite_109276_final.txt', 'r') as mitab,\
        open('cancer_network.txt', 'w') as cancer_network:

    mitab.readline()
    cosmic.readline()
    cosmic_genes = set([i.split('\t')[1].strip() for i in cosmic.readlines()])

    for line in mitab.readlines():
        gene1, gene2 = map(lambda x: x.strip(), line.split('\t'))

        if gene1 in cosmic_genes and gene2 in cosmic_genes:
            cancer_network.write(line)
