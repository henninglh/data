#!/usr/bin/env python

from collections import OrderedDict

with open('mcl-1.8_prwp_a-8_i-1000_links-43706_mean_clean.tsv', 'r') as clean,\
        open('clusters.tsv', 'w') as cluster_file:
    clean.readline()

    cluster_file.write('clusters\tscore\tgenes\n')
    clusters = dict()

    for line in clean.readlines():
        info = line.split('\t')
        cluster = int(float(info[0].strip()))
        gene = info[1].strip()
        score = float(info[2].strip())

        if cluster not in clusters:
            clusters[cluster] = {'genes': set(), 'score': 0.0}
            clusters[cluster]['score'] = score

        clusters[cluster]['genes'].add(gene)

    clusters_sorted = OrderedDict(sorted(clusters.items(),
                                         key=lambda x: (x[1]['score'],
                                             -float(x[0])),
                                         reverse=True))

    for cluster, info in clusters_sorted.iteritems():
        genes = ','.join(info['genes'])
        cluster_file.write('{}\t{}\t{}\n'.format(str(cluster), info['score'], genes))