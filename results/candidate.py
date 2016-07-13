#!/usr/bin/env python

import sys
from collections import OrderedDict

clean_file = sys.argv[1]
scores_file = sys.argv[2]

with open(clean_file, 'r') as results_file,\
        open(scores_file, 'r') as scores_file,\
        open('biomarkers.txt', 'r') as biomarker_file,\
        open('candidates.tsv', 'w') as candidate_file:

    biomarker_file.readline()  # remove header
    biomarkers = set([line.strip() for line in biomarker_file.readlines()])
    results_file.readline()
    clusters = OrderedDict()
    non_clustered = list()


    for line in scores_file.readlines():
        info = line.split('\t')
        cluster = int(float(info[0].strip()))
        score = float(info[1].strip())
        
        if cluster == -1:
            continue

        clusters[cluster] = dict()
        clusters[cluster]['score'] = score

    for line in results_file.readlines():
        info = line.split('\t')
        cluster = int(float(info[0]))
        gene = info[1].strip()
        
        if cluster == -1:
            continue

        if not 'genes' in clusters[cluster]:
            clusters[cluster]['genes'] = set()

        clusters[cluster]['genes'].add(gene)

    for cluster in clusters:
        line = ''
        for gene in clusters[cluster]['genes']:
            if gene not in biomarkers:
                line += ', ' + gene
        candidate_file.write('{}{}\n'.format(cluster, line))
    




    #clusters_sorted = OrderedDict(sorted(clusters.items(),
    #                                     key=lambda x: (x[1]['score'],
    #                                         -float(x[0])),
    #                                    reverse=True))
