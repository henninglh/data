#!/usr/bin/env python

"""
Use with the cancer network
"""

with open('golden_standard.tsv', 'r') as golden,\
        open('../network/cancer_network.txt', 'r') as network,\
        open('golden_std_cancer.tsv', 'w') as corrected:

    golden.readline()
    network.readline()
    network_genes = set()

    corrected.write('gene_names\tscore\n')

    for line in network.readlines():
        map(lambda x: network_genes.add(x.strip()), line.split('\t'))

    for line in golden.readlines():
        if line.split('\t')[0].strip() in network_genes:
            corrected.write(line)
