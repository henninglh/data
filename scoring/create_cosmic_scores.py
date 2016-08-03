#!/usr/bin/env python

with open('CosmicHGNC.tsv', 'r') as cosmic,\
        open('cosmic_scores.txt', 'w') as scores:

    cosmic.readline()
    cosmic_genes = set([i.split('\t')[1].strip() for i in cosmic.readlines()])

    for gene in cosmic_genes:
        scores.write('{}\n'.format(gene))
