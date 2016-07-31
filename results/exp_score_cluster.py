#!/usr/bin/env python

from collections import defaultdict
import operator
import sys

directory = sys.argv[1].strip() + '/'
is_cancer = len(sys.argv) == 3
cancer_prefix = ''
if is_cancer:
    cancer_prefix = '_cancer'

with open('disease_exp_scores.tsv', 'r') as score_file,\
        open(directory + 'clusters_full' + cancer_prefix + '.tsv', 'r') as cluster_file,\
        open(directory + 'exp_ranks' + cancer_prefix + '.tsv', 'w') as ranks:

    score_file.readline()
    cluster_file.readline()

    clusters = defaultdict(float)
    scores = defaultdict(float)

    for line in score_file.readlines():
        gene, score = line.split('\t')
        score = float(score.strip())
        scores[gene] = score

    rank = 1
    for cluster in cluster_file.readlines():
        num,_,genes = map(lambda x: x.strip(), cluster.split('\t'))
        genes_only = [i.split(':')[0] for i in genes.split(',')]
        score = 0.0
        if num == '0':
            continue
        for gene in genes_only:
            score += scores[gene] / float(len(genes_only))
        if score > 0.0:
            ranks.write('{}\t{}\n'.format(rank, score))
        rank += 1

    #for cluster in cluster_file.readlines():
    #    num,_,genes = map(lambda x: x.strip(), cluster.split('\t'))
    #    num = int(num)
    #    gene_set = set([i.split(':')[0] for i in genes.split(',')])
    #    if num != 0:
    #        for gene in gene_set:
    #            clusters[num] += scores[gene] / float(len(gene_set))

    #sorted_clusters = sorted(clusters.items(), key=operator.itemgetter(1))
    #for cluster in sorted_clusters:
    #    ranks.write('{}\t{}\n'.format(cluster[0], cluster[1]))
