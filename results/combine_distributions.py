#!/usr/bin/env python

import sys
import numpy as np

dist_files = sys.argv[1:]

distributions = []
comparisons = 10
clusters = 440
ranks = np.zeros((comparisons,clusters), dtype=np.int64)

for idx, dist in enumerate(dist_files):
    with open(dist.strip(), 'r') as distribution:
        for line in distribution.readlines():
            rank, count = map(lambda x: int(x.strip()), line.split('\t'))
            ranks[idx][rank-1] = count

print ranks.sum(axis=0)
rank = 1
with open('cv_total_dist.tsv', 'w') as full_dist:
    for frequency in ranks.sum(axis=0):
        full_dist.write('{}\t{}\n'.format(rank, frequency))
        rank += 1
