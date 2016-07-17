#!/usr/bin/env python

from collections import defaultdict
import operator

grades = {'A': 1.0,
        'B': 0.75,
        'C': 0.50,
        'D': 0.25,
        'Not Ranked': 0.0}

with open('nodup_ccgd.csv', 'r') as ccgd_file,\
        open('pubmeds.tsv', 'r') as pubmed_file:

    pubmed_file.readline()
    ccgd_file.readline()
    ccgd = defaultdict(list)
    genes = dict()
    values = defaultdict(list)

    for line in pubmed_file.readlines():
        key, count = line.split('\t')
        genes[key] = float(count.strip())

    # Normalize the counts
    minimum = min(genes.values())
    maximum = max(genes.values())
    for key in genes:
        genes[key] = (genes[key] - minimum) / (maximum - minimum)

    for line in ccgd_file.readlines():
        info = line.split(',')
        key = info[0].strip()
        if key in genes:
            genes[key] += grades[info[1]]
    
    ordered_scores = sorted(genes.items(), key=operator.itemgetter(1),
            reverse=True)
    for score in ordered_scores:
        print score
