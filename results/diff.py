#!/usr/bin/env python
import sys
from difflib import SequenceMatcher

print 'Usage: <prefix-to-file> | example: ./diff.py dragon'

filename = sys.argv[1].strip()

with open(filename + '_results.tsv', 'r') as results_file, \
        open(filename + '_scores.tsv', 'r') as scores_file, \
        open(filename + '-FINAL.txt', 'w') as finals:

    results = []
    for line in results_file.readlines():
        info = line.split('\t')
        line = info[0].strip()
        results.append(line)

    scores = [line.split('\t')[0].strip() for line in scores_file.readlines()]

    matcher = SequenceMatcher(None, results, scores)
    diff = matcher.ratio()
    result_string = 'Final result from <{}> is "{}"\n'.format(filename, diff)
    print result_string
    finals.write(result_string)
