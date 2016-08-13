#!/usr/bin/env python

import sys
d = sys.argv[1] + '/'
test = sys.argv[2]

with open(d + 'clusters_full.tsv', 'r') as clean,\
        open(test, 'r') as test_set,\
        open(d + 'lethal_final.tsv', 'w') as core:

    clean.readline()
    test_set.readline()
    clean_genes = filter(lambda x: float(x.split('\t')[1]) > 0.0, 
            [line for line in clean.readlines()])
    test_genes = set([line.strip() for line in test_set.readlines()]) 
    matched = 0
    core.write('rank\ttest biomarkers\ttest candidates\tremaining biomarkers\tremaining candidates\n')

    rank = 1
    for line in clean_genes:
        info = line.split('\t')
        biomarkers = set([a.split(':')[0] for a in 
                filter(lambda x: float(x.split(':')[1].strip()) != 0.0, 
                [i for i in info[2].split(',')])])
        candidates = set([a.split(':')[0] for a in 
                filter(lambda x: float(x.split(':')[1].strip()) == 0.0, 
                [i for i in info[2].split(',')])])
        tested = test_genes.intersection(biomarkers)
        candids = test_genes.intersection(candidates)
        matched += len(tested) + len(candids)
        test_marker = ','.join(tested)
        test_cand = ','.join(candids)
        non_test_marker = ','.join(biomarkers - tested)
        non_test_cand = ','.join(candidates - candids)

        if (len(test_marker) + len(test_cand)) > 0:
            if len(non_test_marker) == 0:
                non_test_marker = '-'
            if len(non_test_cand) == 0:
                non_test_cand = '-'
            if len(test_marker) == 0:
                test_marker = '-'
            if len(test_cand) == 0:
                test_cand = '-'
            core.write('{}\t{}\t{}\t{}\t{}\n'.format(rank, test_marker, test_cand,
                non_test_marker, non_test_cand))
        rank += 1
    print matched
