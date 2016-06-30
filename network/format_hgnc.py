#!/usr/bin/env python
import pandas as pd

table = pd.read_table('hgnc.txt')
table = table[table.Status == 'Approved']
table.to_csv('hgnc_formatted.txt', sep='\t', na_rep='-', index=False)
