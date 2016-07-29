#!/usr/bin/env python

from collections import defaultdict
import operator

with open('disease_text_scores.tsv', 'r') as score_file,\
        open('clusters_full.tsv', 'r') as cluster_file,\
        open('txt_ranks.tsv', 'w') as ranks:

    score_file.readline()
    cluster_file.readline()

    clusters = defaultdict(float)
    scores = defaultdict(float)

    for line in score_file.readlines():
        gene, score = line.split('\t')
        score = float(score.strip())
        scores[gene] = score

    for cluster in cluster_file.readlines():
        num,_,genes = map(lambda x: x.strip(), cluster.split('\t'))
        num = int(num)
        if num != 0:
            for gene in [i.split(':')[0] for i in genes.split(',')]:
                clusters[num] += scores[gene]

    sorted_clusters = sorted(clusters.items(), key=operator.itemgetter(1), reverse=True)
    for cluster in sorted_clusters:
        ranks.write('{}\t{}\n'.format(cluster[0], cluster[1]))
