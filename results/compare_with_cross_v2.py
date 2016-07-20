#!/usr/bin/env python

import sys

with open('clusters.tsv', 'r') as clean,\
        open('../scoring/cross_validation.txt', 'r') as cross_validation,\
        open('cross_results.txt', 'w') as result:

    clean.readline()
    cross_validation.readline()
    clean_genes = filter(lambda x: float(x.split('\t')[1].strip()) > 0.0, [line for line in
        clean.readlines()])
    cross_val_genes = set([line.strip() for line in cross_validation.readlines()]) 
    hits = 0

    for line in clean_genes:
        info = line.split('\t')
        genes = set(info[2].split(','))
        intersect = cross_val_genes.intersection(genes)
        hits += len(cross_val_genes.intersection(genes))

    # Percentage of hits
    print float(hits) / float(len(cross_val_genes))
