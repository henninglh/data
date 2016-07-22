#!/usr/bin/env python

import numpy.random as r

def create_removal(no_removal, border, standard):
    gene = no_removal.pop()  # To start the while loop
    no_removal.add(gene)  # To start the while loop
    new_idx = ''  # start as string!

    while gene in no_removal:
        new_idx = int(r.random_integers(0, border - 1, 1))
        gene = standard[new_idx].split('\t')[0].strip()

    return new_idx, gene

with open('golden_standard_corrected.tsv', 'r') as golden,\
        open('../results/clusters_full.tsv', 'r') as network,\
        open('golden_standard_cv.tsv', 'w') as cv,\
        open('cross_validation.txt', 'w') as cross_validation:

    golden.readline()
    cv.write('gene_names\tscore\n')
    cross_validation.write('gene_names\n')

    no_removal = set()

    clusters = dict()
    gene_to_cluster = dict()

    network.readline()
    for line in network.readlines():
        info = line.split('\t')
        cluster = info[0].strip()
        genes = info[2].split(',')
        scores = map(lambda x: [x.split(':')[0], float(x.split(':')[1])], genes)
        weighted_genes = filter(lambda gene: gene[1] != 0.0, scores)
        if cluster == '0' or len(weighted_genes) < 2:
            map(lambda x: no_removal.add(x[0]), weighted_genes)
            continue
        clusters[cluster] = set()
        map(lambda x: clusters[cluster].add(x[0]), weighted_genes)
        for gene in weighted_genes:
            gene_to_cluster[gene[0]] = cluster

    standard = [line for line in golden.readlines()]
    border = len(standard)
    percentage = int(border / 10)
    removals = set()
    removed = 0

    while removed != percentage:
        new_removal, gene = create_removal(no_removal, border, standard)
        if new_removal not in removals and len(clusters[gene_to_cluster[gene]]) > 1:
            clusters[gene_to_cluster[gene]].remove(gene)
            removals.add(new_removal)
            removed += 1

    for idx in xrange(border):
        gene_only = standard[idx].split('\t')[0].strip()
        if idx in removals:
            cross_validation.write('{}\n'.format(gene_only))
        else:
            cv.write('{}'.format(standard[idx]))
