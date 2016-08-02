#!/usr/bin/env python

import operator

with open('human_disease_textmining_full.tsv', 'r') as f,\
        open('disease_text_scores.tsv', 'w') as clean:

    f.readline()
    clean.write('gene\tzscore\n')
    genes = dict()

    for line in f.readlines():
        _,gene,_,_,zscore,_,_ = map(lambda x: x.strip(), line.split('\t'))
        genes[gene] = float(zscore)

    sort_g = sorted(genes.items(), key=operator.itemgetter(1), reverse=True)

    for gene in sort_g:
        clean.write('{}\t{}\n'.format(gene[0], gene[1]))
