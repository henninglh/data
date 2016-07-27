#!/usr/bin/env python

import sys

with open('clusters_full.tsv', 'r') as clean,\
        open('../scoring/movember_corrected.txt', 'r') as movember,\
        open('movember_matched.txt', 'w') as matched,\
        open('movember_unmatched.txt', 'w') as unmatched,\
        open('movember_distribution.tsv', 'w') as distribution:

    clean.readline()
    movember.readline()
    clean_genes = filter(lambda x: float(x.split('\t')[1]) > 0.0, 
            [line for line in clean.readlines()])
    movember_genes = set([line.strip() for line in movember.readlines()]) 
    identified_genes = set()
    hits = 0
    ranks = []

    for line in clean_genes:
        info = line.split('\t')
        candidates = set([a.split(':')[0] for a in 
                filter(lambda x: float(x.split(':')[1].strip()) == 0.0, 
                [i for i in info[2].split(',')])])
        intersect = list(movember_genes.intersection(candidates))
        map(lambda x: identified_genes.add(x), intersect)
        hits += len(intersect)
        ranks.append(intersect)

    for gene in identified_genes:
        matched.write('{}\n'.format(gene))

    for gene in (movember_genes - identified_genes):
        unmatched.write('{}\n'.format(gene))

    rank = 1
    for candidate in ranks:
        distribution.write('{}\t{}\n'.format(rank, candidate))
        rank += 1

    # Percentage of hits
    print 'total possible matches:', len(movember_genes)
    print 'matches:', hits
    print 'misses:', len(movember_genes) - hits
    print 'percentage:',float(hits) / float(len(movember_genes))
