#!/usr/bin/env python
import sys
import Levenshtein
from sklearn.metrics import jaccard_similarity_score
from difflib import SequenceMatcher

print 'Usage: <prefix-to-file> | example: ./diff.py dragon'

filename = sys.argv[1].strip()

def levenshtein(x, y):
    a = 0
    b = 0

    if len(x) > len(y):
        b = len(x)
        a = len(y)
    else:
        a = len(x)
        b = len(y)

    cur = range(a+1)
    for i in range(1, b + 1):
        prev = cur
        cur = [i]+[0]*a

        for j in range(1, a + 1):
            add_action = prev[j] + 1
            del_action = cur[j-1] + 1
            substitution = prev[j-1]

            if x[j-1] != y[i-1]:
                substitution += 1

            cur[j] = min(add_action, del_action, substitution)
    return cur[a]


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
    #diff = len(matcher.get_opcodes())
    diff = matcher.ratio()
    result_string = 'Final result from <{}> is "{}"'.format(filename, diff)
    print result_string
    print jaccard_similarity_score(results, scores)
    print len(matcher.get_opcodes())
    print levenshtein(results, scores)
    print Levenshtein.seqratio(results, scores)
    finals.write(result_string)
