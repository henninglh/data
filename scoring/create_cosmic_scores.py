#!/usr/bin/env python

with open('CosmicHGNC.tsv', 'r') as cosmic,\
        open('cosmic_scores.tsv', 'w') as scores:

    cosmic.readline()
    cosmic_genes = set([i.split('\t')[1].strip() for i in cosmic.readlines()])

    for gene in cosmic_genes:
        if '_' in gene:
            gene = gene.split('_')[0]
        scores.write('{}\t1\n'.format(gene.strip()))
