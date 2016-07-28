#!/usr/bin/env python

import numpy.random as r

def create_removal(no_removal, border, standard):
    gene = no_removal.pop()  # To start the while loop
    no_removal.add(gene)  # To start the while loop

    while gene in no_removal:
        new_idx = int(r.random_integers(0, border - 1, 1))
        gene = standard[new_idx].split('\t')[0].strip()

    return gene

with open('golden_std_cancer.tsv', 'r') as golden,\
        open('../results/clusters_cancer.tsv', 'r') as network,\
        open('golden_std_cv_cancer.tsv', 'w') as cv,\
        open('cross_validation_cancer.txt', 'w') as cross_validation:

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
    removals = list()
    removed = 0

    while removed != percentage:
        gene = create_removal(no_removal, border, standard)

        if len(clusters[gene_to_cluster[gene]]) > 1:
            clusters[gene_to_cluster[gene]].remove(gene)
            del gene_to_cluster[gene]
            no_removal.add(gene)

            removals.append(gene)
            removed += 1

    for line in standard:
        gene_only = line.split('\t')[0].strip()
        if gene_only in removals:
            cross_validation.write('{}\n'.format(gene_only))
        else:
            cv.write('{}'.format(line))
