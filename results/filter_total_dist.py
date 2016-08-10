#!/usr/bin/env python

import sys
d = sys.argv[1].strip() + '/'
with open(d + 'cv_total_dist.tsv','r') as distribution,\
        open(d + 'cv_total_dist_filtered.tsv','w') as filtered:
    for line in distribution.readlines():
        rank, score = [i.strip() for i in line.split('\t')]
        if score == "0.0":
            filtered.write('{}\t\n'.format(rank))
        else:
            filtered.write('{}\t{}\n'.format(rank, score))


