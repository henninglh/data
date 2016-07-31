#!/usr/bin/env python

from collections import defaultdict
import operator
import sys

directory = sys.argv[1].strip() + '/'
is_cancer = len(sys.argv) == 3
cancer_prefix = ''
if is_cancer:
    cancer_prefix = '_cancer'

with open('disease_know_scores.txt', 'r') as score_file,\
        open(directory + 'clusters_full' + cancer_prefix + '.tsv', 'r') as cluster_file,\
        open(directory + 'know_ranks' + cancer_prefix + '.tsv', 'w') as ranks:

    score_file.readline()
    cluster_file.readline()

    clusters = defaultdict(float)
    scores = set([i.strip() for i in score_file.readlines()])

    rank = 1
    for cluster in cluster_file.readlines():
        num,_,genes = map(lambda x: x.strip(), cluster.split('\t'))
        if num == '0':
            continue
        genes_only = [i.split(':')[0] for i in genes.split(',')]
        score = float(len(scores.intersection(genes_only))) / float(len(genes))
        if score > 0.0:
            ranks.write('{}\t{}\n'.format(rank, score))
        rank += 1

    #for cluster in cluster_file.readlines():
    #    num,_,genes = map(lambda x: x.strip(), cluster.split('\t'))
    #    num = int(num)
    #    if num != 0:
    #        genes = set([i.split(':')[0] for i in genes.split(',')])
    #        found = float(len(scores.intersection(genes)))
    #        clusters[num] += found / float(len(genes))

    #sorted_clusters = sorted(clusters.items(), key=operator.itemgetter(1), reverse=True)
    #for cluster in sorted_clusters:
    #    ranks.write('{}\t{}\n'.format(cluster[0], cluster[1]))
