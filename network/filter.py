#!/usr/bin/env python
import pandas as pd

table = pd.read_table('mitab_10267.txt')
table = table.drop_duplicates(subset=['uidA', 'uidB'])
table.to_csv('mitab_nodup.txt', sep='\t', columns=['uidA', 'uidB'])
