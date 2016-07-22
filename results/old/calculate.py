#!/usr/bin/env python
import sys
import operator
from collections import OrderedDict

if len(sys.argv) < 3:
    print 'Usage: <clean-file> tests/<genes-file>'
    exit(0)

clean_filename = sys.argv[1].strip()
genes_filename = sys.argv[2].strip()
results_filename = genes_filename[:-4] + '_results.tsv'
scores_filename = genes_filename[:-4] + '_scores.tsv'


def calculate_results(entries_list):
    '''
    Calculates and sorts the average biomarker cluster score
    :param entries_list: the cluster entries we go through
    :return: Nil - writes all results to file!
    '''

    # Add known driver genes
    driver_genes = set()
    for line in genes.readlines():
        driver_genes.add(line.strip())

    clusters = dict()

    for entry in entries_list:
        info = entry.split('\t')
        cluster = info[0].strip()

        if not cluster in clusters:
            clusters[cluster] = {'biomarkers': 0, 'member_count': 1,
                                 'mean': 0.0}
        else:
            clusters[cluster]['member_count'] += 1

        if info[1].strip() in driver_genes:
            clusters[cluster]['biomarkers'] += 1

    if '-1' in clusters:
        del clusters['-1']

    for key, val in clusters.iteritems():
        val['mean'] = float(val['biomarkers']) / float(val['member_count'])

    # Sort after cluster score descending, then cluster number ascending
    clusters_sorted = OrderedDict(sorted(clusters.items(),
                                         key=lambda x: (x[1]['mean'],
                                             -float(x[0])),
                                         reverse=True))

    for cluster, info in clusters_sorted.iteritems():
        results.write('{}\t{}\n'.format(str(cluster)[:-2], info['mean']))


def calculate_scores(entries_list):
    '''
    Calculates cluster scores and writes them in a descending (by score)
    order to file
    :param entries_list: the cluster entries we go through
    :return: Nil - writes all results to file
    '''

    cluster_scores = dict()
    for entry in entries_list:
        info = entry.split('\t')
        cluster = info[0].strip()
        score = info[2].strip()

        if not cluster in cluster_scores:
            cluster_scores[cluster] = float(score)

    if '-1' in cluster_scores:
        del cluster_scores['-1']

    # Sort after cluster score descending, then cluster number ascending
    cluster_scores_sorted = OrderedDict(sorted(cluster_scores.items(),
                                           key=lambda x: (x[1], -float(x[0])),
                                           reverse=True))

    for cluster, score in cluster_scores_sorted.iteritems():
        scores.write('{}\t{}\n'.format(str(cluster)[:-2], score))


with open(clean_filename, 'r') as clean, \
        open('tests/' + genes_filename, 'r') as genes, \
        open(results_filename, 'w') as results, \
        open(scores_filename, 'w') as scores:

    genes.readline()  # remove header
    clean.readline()  # remove header

    entries = clean.readlines()
    calculate_results(entries)
    calculate_scores(entries)
