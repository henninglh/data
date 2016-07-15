#!/usr/bin/env python

import pandas as pd

table = pd.read_csv('ccgd_results.csv')
cols = ['Relative Rank', 'Cancer Type', 'COSMIC', 'CGC']
table = table.set_index('Human Symbol')
table.to_csv('nodup_ccgd.csv', columns=cols, na_rep='-')
