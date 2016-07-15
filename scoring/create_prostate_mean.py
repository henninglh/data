#!/usr/bin/env python

import pandas as pd

table = pd.read_table('1-rel_prostate.tsv')
table = table.set_index('geneName')
table = table.groupby(table.index).mean()
table.to_csv('prostate_mean.tsv', sep='\t', columns=['score'])
