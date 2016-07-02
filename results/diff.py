#!/usr/bin/env python
import sys
from difflib import SequenceMatcher

filename = sys.argv[1].strip()

with open(filename + '_results.tsv', 'r') as results_file, \
        open(filename + '_scores.tsv', 'r') as scores_file, \
        open(filename + '-FINAL.txt', 'w') as finals:

    results = [cluster.split('\t')[0].strip() for cluster in
               results_file.readlines()]
    scores = [cluster.split('\t')[0].strip() for cluster in
              scores_file.readlines()]

    matcher = SequenceMatcher(None, results, scores)
    diff = matcher.ratio()
    print diff
    finals.write('Final result from <{}> is "{}"\n'.format(filename, diff))
