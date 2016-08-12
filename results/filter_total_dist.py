#!/usr/bin/env python

import sys
d = sys.argv[1].strip() + '/'
with open(d + 'cv_total_dist.tsv','r') as distribution,\
        open(d + 'cv_total_dist_filtered.tsv','w') as filtered:
    for line in distribution.readlines():
        info = line.split('\t')
        rank = int(info[0].strip())
        score = float(info[1].strip())
        if score == 0.0:
            score = ''
        filtered.write('{}\t{}\n'.format(rank, score))


