#!/usr/bin/env python
import pandas as pd

table = pd.read_table('mitab_lite.txt')
table.to_csv('mitab_lite.tsv', sep='\t', columns=['a_alias', 'b_alias'],
        index=False)
