#!/usr/bin/env python

with open('cross_validation.txt', 'r') as possible,\
        open('cv_20_percent.tsv', 'r') as found:

    possible.readline()
    found.readline()

    possible_genes = set([line.strip() for line in possible.readlines()])
    identified = 0
    possibles = 0

    for line in found.readlines():
        info = line.split('\t')
        genes_with_scores = info[2].split(',')
        genes = set(tuple(map(lambda x: x.split(':')[0], genes_with_scores)))
        identified += len(possible_genes.intersection(genes))
        possibles += len(genes)

    print 'Percentage found in the top 20% genes:',((float(identified)
        / float(possibles)) * 100)
