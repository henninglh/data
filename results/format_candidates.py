#!/usr/bin/env python

with open('candidates.tsv', 'r') as candidates,\
        open('candidates_only.txt', 'w') as cand_only:

    candidates.readline()  # Remove header
    genes = []
    singles = 0

    for line in candidates.readlines():
        info = line.split('\t')
        if len(info) == 3 and len(info[2].strip()) > 0:
            g = info[2].strip()
            genes.append(g)
            singles += len(g.split(','))


    cand_only.write('candidates\ttotal:{}\n'.format(singles))

    for gene in genes:
        cand_only.write('{}\n'.format(gene))
