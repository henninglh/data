#!/usr/bin/env python

import matplotlib as plt

distribution = []
with open('../results/cv_total_dist.tsv', 'r') as dist_file:
    distribution = [int(i.split('\t')[1].strip()) for i in dist_file.readlines()]
print distribution[8]

