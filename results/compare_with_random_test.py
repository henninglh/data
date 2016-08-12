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
    core.write('rank\tbiomarkers\tcandidates\tcluster\n')

    rank = 1
    for line in clean_genes:
        info = line.split('\t')
        genes = set([i.split(':')[0].strip() for i in info[2].split(',')])
        candidates = set([a.split(':')[0] for a in 
                filter(lambda x: float(x.split(':')[1].strip()) == 0.0, 
                [i for i in info[2].split(',')])])
        biomarkers = test_genes.intersection(genes - candidates)
        candids = test_genes.intersection(candidates)
        ident_non = ','.join(genes - candids - biomarkers)
        ident_marker = ','.join(biomarkers)
        ident_candid = ','.join(candids)

        if (len(ident_marker) + len(ident_candid)) > 0:
            if len(ident_non) == 0:
                ident_non = '-'
            if len(ident_marker) == 0:
                ident_marker = '-'
            if len(ident_candid) == 0:
                ident_candid = '-'
            core.write('{}\t{}\t{}\t{}\n'.format(rank, ident_marker, ident_candid,
                ident_non))
        rank += 1
