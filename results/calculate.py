#!/usr/bin/env python
import sys

clean_filename = sys.argv[1].strip()

with open(clean_filename, 'r') as clean,\
        open('fasit.txt', 'r') as fasit,\
        open('results.txt', 'w') as results:

    fasit.readline() # remove header
    clean.readline() # remove header

    # Add genes
    driver_genes = set()
    for line in fasit.readlines():
        driver_genes.add(line.strip())

    clusters = dict()
    gene_to_cluster = dict()

    entries = clean.readlines()
    for entry in entries:
        info = entry.split('\t')

        if not info[1] in clusters:
            clusters[info[1]] = {'total': info[2], 'member_count': 1}
        else:
            clusters[info[1]]['total'] += info[2]
            clusters[info[1]]['member_count'] += 1


        gene_to_cluster[info[0]] = info[1]

