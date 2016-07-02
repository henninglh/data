#!/usr/bin/env python
import sys
from difflib import SequenceMatcher

filename = sys.argv[1].strip()

with open(filename + '_results.tsv', 'r') as results_file, \
        open(filename + '_scores.tsv', 'r') as scores_file, \
        open(filename + '-FINAL.txt', 'w') as finals:

    results = []
    for line in results_file.readlines():
        info = line.split('\t')
        line = info[0].strip()
        score = float(info[1].strip())

        if score > 0.0:
            results.append(line)

    scores = [line.split('\t')[0].strip() for line in scores_file.readlines()]
    scores = scores[:len(results)]

    matcher = SequenceMatcher(None, results, scores)
    diff = matcher.ratio()
    print diff
    finals.write('Final result from <{}> is "{}"\n'.format(filename, diff))
