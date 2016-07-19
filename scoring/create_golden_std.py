#!/usr/bin/env python

import sys

with open('disgen_clean.tsv', 'r') as disgen,\
        open('dragon_clean.txt', 'r') as dragon,\
        open('golden_standard.tsv', 'w') as golden_standard:

    disgen.readline()
    dragon.readline()
    golden_standard.write('gene_names\tscore\n')


    markers = dict()

    for line in disgen.readlines():
        gene, score = line.split('\t')
        markers[gene] = float(score)

    maximum = max(markers.itervalues())
    minimum = min(markers.itervalues())
    average = (maximum + minimum) / 2
    sane_max = average + ((maximum - average) / 4)

    for line in dragon.readlines():
        gene = line.strip()
        if gene not in markers:
            markers[gene] = sane_max
        else:
            markers[gene] = minimum

    for marker in markers:
        golden_standard.write('{}\t{}\n'.format(marker, markers[marker]))
