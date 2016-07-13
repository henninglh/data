#!/usr/bin/env python

import sys
import pandas as pd

table = pd.read_table(sys.argv[1].strip())
table = table.set_index('geneName')
table = table.groupby(table.index).mean()
table.to_csv('prostate_mean.tsv', sep='\t', columns=['score'])

