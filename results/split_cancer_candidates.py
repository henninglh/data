#!/usr/bin/env python

import pandas as pd

table = pd.read_table('mcl-1.8_prwp_a-8_i-1000_links-43706_mean_clean.tsv',
        sep='\t')
cancers = table[table['score'] != 0.0]
candidates = table[table['score'] == 0.0]
candidates = candidates[candidates['PRWP'] != 0.0]

cancers.to_csv('cancers_only.tsv', sep='\t', index=False)
candidates.to_csv('candidates_only.tsv', sep='\t', index=False)
