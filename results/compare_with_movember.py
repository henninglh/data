#!/usr/bin/env python

import sys

with open('clusters.tsv', 'r') as clean,\
        open('../scoring/movember_corrected.txt', 'r') as movember,\
        open('movember_matched.txt', 'w') as matched,\
        open('movember_unmatched.txt', 'w') as unmatched:

    clean.readline()
    movember.readline()
    clean_genes = [line for line in clean.readlines()]
    movember_genes = set([line.strip() for line in movember.readlines()]) 
    identified_genes = set()
    hits = 0

    for line in clean_genes:
        info = line.split('\t')
        genes = set([i.split(':')[0].strip() for i in info[2].split(',')])
        intersect = list(movember_genes.intersection(genes))
        map(lambda x: identified_genes.add(x), intersect)
        hits += len(movember_genes.intersection(genes))

    for gene in identified_genes:
        matched.write('{}\n'.format(gene))

    for gene in (movember_genes - identified_genes):
        unmatched.write('{}\n'.format(gene))

    # Percentage of hits
    print 'total possible matches:', len(movember_genes)
    print 'matches:', hits
    print 'misses:', len(movember_genes) - hits
    print 'percentage:',float(hits) / float(len(movember_genes))
