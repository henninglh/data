#!/usr/bin/env python

from collections import defaultdict
import operator

with open('disease_know_scores.txt', 'r') as score_file,\
        open('clusters_full.tsv', 'r') as cluster_file,\
        open('know_ranks.tsv', 'w') as ranks:

    score_file.readline()
    cluster_file.readline()

    clusters = defaultdict(float)
    scores = set([i.strip() for i in score_file.readlines()])

    for cluster in cluster_file.readlines():
        num,_,genes = map(lambda x: x.strip(), cluster.split('\t'))
        num = int(num)
        if num != 0:
            genes = set([i.split(':')[0] for i in genes.split(',')])
            found = float(len(scores.intersection(genes)))
            clusters[num] += found / float(len(genes))

    sorted_clusters = sorted(clusters.items(), key=operator.itemgetter(1), reverse=True)
    for cluster in sorted_clusters:
        ranks.write('{}\t{}\n'.format(cluster[0], cluster[1]))
