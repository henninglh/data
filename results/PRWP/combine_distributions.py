#!/usr/bin/env python

import numpy as np

dist_files = [
        'cv_distribution1.tsv',
        'cv_distribution2.tsv',
        'cv_distribution3.tsv',
        'cv_distribution4.tsv',
        'cv_distribution5.tsv',
        'cv_distribution6.tsv',
        'cv_distribution7.tsv',
        'cv_distribution8.tsv',
        'cv_distribution9.tsv',
        'cv_distribution10.tsv',
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
        #if frequency != 0.0:
        full_dist.write('{}\t{}\n'.format(rank, frequency))
        rank += 1
