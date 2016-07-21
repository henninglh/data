#!/usr/bin/env python

with open('jensen_cancerous.tsv', 'r') as jensen,\
        open('cancers_only.tsv', 'r') as clean,\
        open('jensen_cancer_zvals.tsv', 'w') as zvals,\
        open('jensen_cancer_scores.tsv', 'w') as scores,\
        open('jensen_cancer_creds.tsv', 'w') as creds:

    clean.readline()

    
