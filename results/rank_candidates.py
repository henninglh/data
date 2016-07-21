#!/usr/bin/env python

with open('jensen_cancerous.tsv', 'r') as jensen,\
        open('candidates_only.tsv', 'r') as clean,\
        open('jensen_candidates_zvals.tsv', 'w') as zvals,\
        open('jensen_candidates_scores.tsv', 'w') as zvals,\
        open('jensen_candidates_creds.tsv', 'w') as zvals,\

    clean.readline()
