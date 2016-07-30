#!/usr/bin/env python

import numpy as np

dist_files = [
        'cv_distribution_cancer1.tsv',
        'cv_distribution_cancer2.tsv',
        'cv_distribution_cancer3.tsv',
        'cv_distribution_cancer4.tsv',
        'cv_distribution_cancer5.tsv',
        'cv_distribution_cancer6.tsv',
        'cv_distribution_cancer7.tsv',
        'cv_distribution_cancer8.tsv',
        'cv_distribution_cancer9.tsv',
        'cv_distribution_cancer10.tsv',
        ]
comparisons = 10
clusters = 1340
ranks = np.zeros((comparisons,clusters), dtype=np.float64)

for idx, dist in enumerate(dist_files):
    with open(dist.strip(), 'r') as distribution:
        for line in distribution.readlines():
            info = line.split('\t')
            rank = int(info[0].strip())
            count = float(info[1].strip())
            ranks[idx][rank-1] = count

print ranks.sum(axis=0)
rank = 1
with open('cv_total_dist.tsv', 'w') as full_dist:
    for frequency in ranks.sum(axis=0):
        full_dist.write('{}\t{}\n'.format(rank, frequency))
        rank += 1
