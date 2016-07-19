#!/usr/bin/env python

with open('disgen_clean.tsv', 'r') as disgen,\
        open('dragon_clean.txt', 'r') as dragon,\
        open('golden_standard.tsv', 'w') as golden_standard:

    disgen.readline()
    dragon.readline()
    golden_standard.write('gene_names\tscore\n')

    markers = dict()

    for line in disgen.readlines():
        gene, score = line.split('\t')
        markers[gene] = float(0.5)

    for line in dragon.readlines():
        gene = line.strip()
        if gene in markers:
            markers[gene] += float(0.5)
        else:
            markers[gene] = float(0.5)

    for marker in markers:
        golden_standard.write('{}\t{}\n'.format(marker, markers[marker]))
