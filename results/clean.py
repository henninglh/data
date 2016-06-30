#!/usr/bin/env python
import pandas as pd
import sys

unclean = sys.argv[1].strip()
algorithm = sys.argv[2].strip()
clean_filename = unclean[:-4] + '_clean.tsv'
print clean_filename

table = pd.read_csv(unclean)
cols = set(table) # Create set from table headers
cols.remove('SUID')
cols.remove('shared name')
cols.remove('selected')
cols.remove('score')
table.to_csv('clean/' + algorithm + '/' + clean_filename, index=False,\
        sep='\t', columns=list(cols))

