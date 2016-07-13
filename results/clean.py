#!/usr/bin/env python
import pandas as pd
import sys

unclean = sys.argv[1].strip()
clustering = sys.argv[2].strip() # clustering algorithm
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
#cols.remove('score')  # make this more dynamic?
#cols.remove('Unnamed: 0')
table.fillna(value=0)
table = table[table[ranking] != -1]
table.to_csv('clean/' + clustering + '/' + clean_filename, na_rep=-1,
             index=False, sep='\t', columns=list(cols))
