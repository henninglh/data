#!/usr/bin/env python

import numpy.random as r

def create_removal(no_removal, border, standard):
    remove = no_removal.pop()
    no_removal.add(remove)
    new_idx = ''  # start as string!

    while remove in no_removal:
        new_idx = int(r.random_integers(0, border - 1, 1))
        remove = standard[new_idx].split('\t')[0].strip()

    return new_idx

with open('golden_standard_corrected.tsv', 'r') as golden,\
        open('../results/clusters.tsv', 'r') as network,\
        open('golden_standard_cv.tsv', 'w') as cv,\
        open('cross_validation.txt', 'w') as cross_validation:

    golden.readline()
    cv.write('gene_names\tscore\n')
    cross_validation.write('gene_names\n')

    no_removal = set()

    network.readline()
    for line in network.readlines():
        info = line.split('\t')
        genes = info[2].split(',')
        scores = map(lambda x: [x.split(':')[0], float(x.split(':')[1])], genes)
        weighted_genes = filter(lambda gene: gene[1] != 0.0, scores)
        if len(weighted_genes) < 2:
            map(lambda x: no_removal.add(x[0]), weighted_genes)

    standard = [line for line in golden.readlines()]
    golden_cv = []

    border = len(standard)
    percentage = int(border / 10)
    removals = set()
    removed = 0

    while removed != percentage:
        new_removal = create_removal(no_removal, border, standard)
        if new_removal not in removals:
            removals.add(new_removal)
            removed += 1

    for idx in xrange(border):
        gene_only = standard[idx].split('\t')[0].strip()
        if idx in removals:
            cross_validation.write('{}\n'.format(gene_only))
        else:
            cv.write('{}'.format(standard[idx]))
