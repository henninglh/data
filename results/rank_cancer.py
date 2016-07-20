#!/usr/bin/env python

#import pandas as pd
#import sys
from collections import OrderedDict
import operator
from difflib import SequenceMatcher
from itertools import combinations
from scipy.stats import ttest_ind, f_oneway

# First argument is clean result file to use

#table = pd.read_table(sys.argv[1].strip(), sep='\t')
#sort = table.sort_values(by=['PRWP_single'])
#sort.to_csv('ranked_cancer_genes.tsv', sep='\t', columns=['name',
#    'PRWP_single'])

no_gene = '__NO_GENE__'

with open('cancerous.tsv', 'r') as cancer_file,\
        open('res1.tsv', 'r') as results_file,\
        open('zvals.tsv', 'w') as zvals,\
        open('scores.tsv', 'w') as scores,\
        open('creds.tsv', 'w') as creds_file:

    cancer_file.readline()
    results_file.readline()
 
    ranks = list()
    genes = dict()
 
    for line in results_file.readlines():
        info = line.split('\t')
        genes[info[0].strip()] = float(info[1].strip())
 
    for line in cancer_file.readlines():
        gene = no_gene
        info = line.split('\t')
        candidate_id1 = info[0].strip()
        candidate_id2 = info[1].strip()
        disease = info[3].strip()
        zval = float(info[4].strip())
        cred = float(info[5].strip())
 
        if candidate_id1 in genes:
            gene = candidate_id1
        elif candidate_id2 in genes:
            gene = candidate_id2
 
        if gene != no_gene:
            ranks.append([gene, genes[gene], float(zval), float(cred), disease])
 
 
    score_sorted = [s[0] for s in sorted(ranks, key=operator.itemgetter(1,0), reverse=True)]
    z_sorted = [s[0] for s in sorted(ranks, key=operator.itemgetter(2,0), reverse=True)]
    cred_sorted = [s[0] for s in sorted(ranks, key=operator.itemgetter(3,0), reverse=True)]

    score_z = SequenceMatcher(None, score_sorted, z_sorted)
    score_cred = SequenceMatcher(None, score_sorted, cred_sorted)
    z_cred = SequenceMatcher(None, z_sorted, cred_sorted)


    print 'score vs z: <',score_z.ratio(),'>'
    print 'score vs cred: <',score_cred.ratio(),'>'
    print 'z vs cred: <',z_cred.ratio(),'>'

    for idx in range(len(score_sorted)):
        scores.write('{}\n'.format(score_sorted[idx]))
        zvals.write('{}\n'.format(z_sorted[idx]))
        creds_file.write('{}\n'.format(cred_sorted[idx]))
