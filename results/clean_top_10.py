#!/usr/bin/env python

import sys

d = sys.argv[1].strip() + '/'
with open(d + 'clusters_full.tsv', 'r') as clusters,\
        open(d + 'top10.tsv', 'w') as top:
    clusters.readline()
    top.write('cluster_number\tscore\tgenes\n')

    count = 0
    while count < 10:
        line = clusters.readline()
        info = map(lambda x: x.strip(), line.split('\t'))
        rank = int(info[0])
        score = float(info[1])
        genes = [x.split(':')[0].strip() for x in info[2].split(',')]
        top.write('{}\t{}\t{}\n'.format(rank, score, ','.join(genes)))
        count += 1
