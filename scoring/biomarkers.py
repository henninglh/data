#!/usr/bin/env python

with open('disgen_clean.tsv', 'r') as disgen,\
        open('dragon_clean.txt', 'r') as dragon,\
        open('putative_prognostic_prostate_markers.csv', 'r') as movember,\
        open('biomarkers.txt', 'w') as biomarkers:

    disgen.readline()
    dragon.readline()
    movember.readline()
    biomarkers.write('gene_names\n')

    markers = set()

    for line in disgen.readlines():
        gene, score = line.split('\t')
        markers.add(gene.strip())

    for line in dragon.readlines():
        markers.add(line.strip())

    for line in movember.readlines():
        markers.add(line.strip())

    for marker in markers:
        biomarkers.write('{}\n'.format(marker))
