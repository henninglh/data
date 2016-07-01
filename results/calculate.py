#!/usr/bin/env python
import sys

clean_filename = sys.argv[1].strip()
genes_filename = sys.argv[2].strip()
results_filename = genes_filename[:-4] + '_results.tsv'

with open(clean_filename, 'r') as clean, \
        open(genes_filename, 'r') as genes, \
        open(results_filename, 'w') as results:

    genes.readline()  # remove header
    clean.readline()  # remove header

    # Add known driver genes
    driver_genes = set()
    for line in genes.readlines():
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
