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
        open(directory + 'clusters_cosmic' + cancer_prefix + '.tsv', 'r') as cluster_file,\
        open(directory + 'know_ranks_split_cosmic' + cancer_prefix + '.tsv', 'w') as ranks:

    score_file.readline()
    cluster_file.readline()

    clusters = defaultdict(float)
    scores = set([i.strip() for i in score_file.readlines()])

    rank = 1
    for cluster in cluster_file.readlines():
        num,_,genes = map(lambda x: x.strip(), cluster.split('\t'))

        if num == '0':
            continue

        genes = genes.split(',')
        genes_only = [i.split(':')[0].strip() for i in filter(lambda x: float (x.split(':')[1]) > 0.0, genes)]
        candidates_only = [i.split(':')[0].strip() for i in filter(lambda x: float(x.split(':')[1]) == 0.0, genes)]
        gene_score = float(len(scores.intersection(genes_only))) / float(len(genes))
        cand_score = float(len(scores.intersection(candidates_only))) / float(len(genes))

        if (gene_score + cand_score) > 0.0:
            if gene_score == 0.0 and cand_score != 0.0:
                ranks.write('{}\t\t{}\n'.format(rank, cand_score))
            elif cand_score == 0.0 and gene_score != 0.0:
                ranks.write('{}\t{}\t\n'.format(rank, gene_score))
            else:
                ranks.write('{}\t{}\t{}\n'.format(rank, gene_score, cand_score))
        rank += 1
