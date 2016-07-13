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

    candidate_file.write('rank\tcluster\tcandidates\n')

    for line in scores_file.readlines():
        info = line.split('\t')
        cluster = int(float(info[0].strip()))
        score = float(info[1].strip())
        
        if cluster == -1:
            continue

        clusters[cluster] = dict()

        if score == 0.0:
            break

        clusters[cluster]['score'] = score

    for line in results_file.readlines():
        info = line.split('\t')
        cluster = int(float(info[0]))
        gene = info[1].strip()
        
        if cluster == -1 or cluster not in clusters:
            continue

        if not 'genes' in clusters[cluster]:
            clusters[cluster]['genes'] = set()

        clusters[cluster]['genes'].add(gene)

    rank = 1
    for cluster in clusters:
        candidates = []
        for gene in clusters[cluster]['genes']:
            if gene not in biomarkers:
                candidates.append(gene)
        candidate_format = ','.join(candidates)
        candidate_file.write('{}\t{}\t{}\n'.format(rank, cluster,
            candidate_format))
        rank += 1
    




    #clusters_sorted = OrderedDict(sorted(clusters.items(),
    #                                     key=lambda x: (x[1]['score'],
    #                                         -float(x[0])),
    #                                    reverse=True))
