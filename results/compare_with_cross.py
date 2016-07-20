#!/usr/bin/env python

import sys

with open('clusters.tsv', 'r') as clean,\
        open('../scoring/cross_validation.txt', 'r') as cross_validation,\
        open('cross_validation_matched.txt', 'w') as matched,\
        open('cross_validation_unmatched.txt', 'w') as unmatched:

    clean.readline()
    cross_validation.readline()
    matched.write('gene_names\n')
    clean_genes = [line for line in clean.readlines()]
    cross_val_genes = set([line.strip() for line in cross_validation.readlines()]) 
    identified_genes = set()
    hits = 0

    for line in clean_genes:
        info = line.split('\t')
        genes = set(info[2].split(','))
        intersect = list(cross_val_genes.intersection(genes))
        map(lambda x: identified_genes.add(x), intersect)
        hits += len(intersect)

    for gene in identified_genes:
        matched.write('{}\n'.format(gene))

    for gene in (cross_val_genes - identified_genes):
        unmatched.write('{}\n'.format(gene))

    # Percentage of hits
    print 'total possible matches:', len(cross_val_genes)
    print 'matches:', hits
    print 'percentage:',float(hits) / float(len(cross_val_genes))