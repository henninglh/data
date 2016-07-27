#!/usr/bin/env python

import sys

with open('clusters.tsv', 'r') as clean,\
        open('../scoring/cross_validation.txt', 'r') as cross_validation,\
        open('cross_validation_matched.txt', 'w') as matched,\
        open('cross_validation_unmatched.txt', 'w') as unmatched,\
        open('cv_distribution.tsv', 'w') as distribution:

    clean.readline()
    cross_validation.readline()
    matched.write('gene_names\n')
    clean_genes = filter(lambda x: float(x.split('\t')[1]) > 0.0,
            [line for line in clean.readlines()])
    cross_val_genes = set([line.strip() for line in
        cross_validation.readlines()])
    identified_genes = set()
    hits = 0
    ranks = []

    for line in clean_genes:
        info = line.split('\t')
        genes = set([i.split(':')[0].strip() for i in info[2].split(',')])
        candidates = set([a.split(':')[0] for a in 
                filter(lambda x: float(x.split(':')[1].strip()) == 0.0, 
                [i for i in info[2].split(',')])])
        intersect = list(cross_val_genes.intersection(genes))
        map(lambda x: identified_genes.add(x), intersect)
        hits += len(intersect)
        ranks.append(intersect)

    for gene in identified_genes:
        matched.write('{}\n'.format(gene))

    for gene in (cross_val_genes - identified_genes):
        unmatched.write('{}\n'.format(gene))

    rank = 1
    for candidate in ranks:
        distribution.write('{}\t{}\n'.format(rank, candidate))
        rank += 1

    # Percentage of hits
    print 'total possible matches:', len(cross_val_genes)
    print 'matches:', hits
    print 'misses:', len(cross_val_genes) - hits
    print 'percentage:',float(hits) / float(len(cross_val_genes))
