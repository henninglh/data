#!/usr/bin/env python

import operator

"""
Assumes prostate cancer filtered information (no "samples")
"""

with open('human_disease_experiments_full.tsv', 'r') as f,\
        open('disease_exp_scores.tsv', 'w') as clean:

    f.readline()
    clean.write('gene\tscore\n')
    genes = dict()

    for line in f.readlines():
        _,gene,_,_,_,score,_ = map(lambda x: x.strip(),
                line.split('\t'))
        if len(gene) != 15:
            score = float(score.split(' ')[-1])
            genes[gene] = {'score': score}
    
    sort_g = sorted(genes.items(), key=operator.itemgetter(1, 0))
    for gene in sort_g:
        clean.write('{}\t{}\n'.format(gene[0], gene[1]['score']))
