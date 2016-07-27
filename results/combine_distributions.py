#!/usr/bin/env python

import sys
import numpy as np

dist_files = sys.argv[1:]

distributions = []
ranks = np.zeros((10,440))

for idx, dist in enumerate(dist_files):
    with open(dist.strip(), 'r') as distribution:
        for line in distribution.readlines():
            rank, count = map(lambda x: int(x.strip()), line.split('\t'))
            ranks[idx][rank-1] = count

print ranks.sum(axis=0)
