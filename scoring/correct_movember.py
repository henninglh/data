#!/usr/bin/env python

with open('putative_prognostic_prostate_markers.csv', 'r') as movember,\
        open('../network/mitab_lite_109276_final.txt', 'r') as network,\
        open('movember_corrected.txt', 'w') as corrected:

    movember.readline()
    network.readline()
    network_genes = set()
    corrected.write('gene_names\n')

    for line in network.readlines():
        gene1, gene2 = line.split('\t')
        network_genes.add(gene1.strip())
        network_genes.add(gene2.strip())
    
    for line in movember.readlines():
        if line.strip() in network_genes:
            corrected.write(line)
