#!/usr/bin/env python

with open('golden_standard_cv.tsv', 'r') as golden,\
        open('../network/mitab_lite_109276_final.txt', 'r') as network,\
        open('golden_standard_cv_corrected.tsv', 'w') as corrected:

    golden.readline()
    network.readline()
    network_genes = set()

    corrected.write('gene_names\tscore\n')

    for line in network.readlines():
        gene1, gene2 = line.split('\t')
        network_genes.add(gene1.strip())
        network_genes.add(gene2.strip())

    for line in golden.readlines():
        if line.split('\t')[0].strip() in network_genes:
            corrected.write(line)
