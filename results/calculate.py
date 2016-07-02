#!/usr/bin/env python
import sys
from collections import OrderedDict

clean_filename = sys.argv[1].strip()
genes_filename = sys.argv[2].strip()
algorithm = sys.argv[3].strip()
results_filename = genes_filename[:-4] + '_results.tsv'

with open('clean/' + algorithm + '/' + clean_filename, 'r') as clean, \
        open('tests/' + genes_filename, 'r') as genes, \
        open(results_filename, 'w') as results:
    genes.readline()  # remove header
    clean.readline()  # remove header

    # Add known driver genes
    driver_genes = set()
    for line in genes.readlines():
        driver_genes.add(line.strip())

    clusters = dict()

    entries = clean.readlines()
    for entry in entries:
        info = entry.split('\t')

        if not info[0] in clusters:
            clusters[info[0]] = {'biomarkers': 0, 'member_count': 1,
                                 'score': 0.0}
        else:
            clusters[info[0]]['member_count'] += 1

        if info[1].strip() in driver_genes:
            clusters[info[0]]['biomarkers'] += 1

    if '-1' in clusters:
        del clusters['-1']

    for key, val in clusters.iteritems():
        val['score'] = float(val['biomarkers'] / val['member_count'])

    clusters_sorted = OrderedDict(sorted(clusters.items(), key=lambda x: x[1][
        'score'], reverse=True))

    for cluster, info in clusters_sorted.iteritems():
        results.write('{}\t{}\n'.format(str(cluster)[:-2], info['score']))
