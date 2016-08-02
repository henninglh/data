#!/usr/bin/env python

import numpy as np
import sys

d = sys.argv[1].strip() + '/'
is_cancer = len(sys.argv) == 4
clusters = int(sys.argv[2].strip())
prefix = ''
if is_cancer:
    prefix = '_cancer'

dist_files = [
        d + 'cv_distribution' + prefix + '1.tsv',
        d + 'cv_distribution' + prefix + '2.tsv',
        d + 'cv_distribution' + prefix + '3.tsv',
        d + 'cv_distribution' + prefix + '4.tsv',
        d + 'cv_distribution' + prefix + '5.tsv',
        d + 'cv_distribution' + prefix + '6.tsv',
        d + 'cv_distribution' + prefix + '7.tsv',
        d + 'cv_distribution' + prefix + '8.tsv',
        d + 'cv_distribution' + prefix + '9.tsv',
        d + 'cv_distribution' + prefix + '10.tsv',
        ]
comparisons = len(dist_files)  # Default: 10
ranks = np.zeros((comparisons,clusters), dtype=np.float64)
rank_to_cluster = dict()

for idx, dist in enumerate(dist_files):
    with open(dist.strip(), 'r') as distribution:
        for line in distribution.readlines():
            info = line.split('\t')
            rank = int(info[0].strip())
            count = float(info[1].strip())
            ranks[idx][rank-1] = count
            rank_to_cluster[rank] = info[1].strip()

print ranks.sum(axis=0)
rank = 1
with open(d + 'cv_total_dist' + prefix + '.tsv', 'w') as full_dist:
    for frequency in ranks.sum(axis=0):
        full_dist.write('{}\t{}\n'.format(rank, frequency))
        rank += 1
