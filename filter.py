#!/usr/bin/env python
import pandas as pd

table = pd.read_table('mitab-2.txt')
table = table.drop_duplicates(subset=['uidA', 'uidB'])
table.to_csv('mitab_nodup.txt', sep='\t', columns=['uidA', 'uidB'])
