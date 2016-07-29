#!/usr/bin/env python
import pandas as pd
import sys

unclean = sys.argv[1].strip()
ranking = sys.argv[3].strip() # ranking algorithm
scorings = sys.argv[4:]
clean_filename = unclean[:-4] + '_clean.tsv'
print clean_filename

table = pd.read_csv(unclean)
cols = set(table)  # Create set from table headers
cols.remove('SUID')
cols.remove('shared name')
cols.remove('selected')
for score in scorings:
    cols.remove(score.strip())
table.fillna(value=0)
#table = table.sort_values(by=['PRWP', '__mclCluster', 'name'], ascending=[False,
table = table.sort_values(by=['MAA', '__mclCluster', 'name'], ascending=[False,
    True, True])
table.to_csv(clean_filename, na_rep=0.0, index=False, sep='\t',
        #columns=['__mclCluster', 'name', 'PRWP', 'score', 'PRWP_single'])  # PRWP
        columns=['__mclCluster', 'name', 'MAA', 'score'])  # MAA
