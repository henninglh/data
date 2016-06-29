#!/usr/bin/env python
import pandas as pd
import sys

unclean = sys.argv[1].strip()
ranking = sys.argv[2].strip()
clustering = sys.argv[3].strip()
score = sys.argv[4].strip()
clean_filename = '{}_clean.txt'.format(unclean)
unique_id = 'name'

print 'File to clean: {}'.format(unclean)
print 'Ranking algorithm: {}'.format(ranking)
print 'Clustering algorithm: {}'.format(clustering)
print 'Scoring attribute: {}'.format(score)


table = pd.read_csv(unclean)
#table.pop('SUID')
#table.pop('shared name')
#table.pop('selected')
#table.pop(score)
# columns argument also decides the order
table.to_csv(clean_filename, index=False, sep='\t', \
        columns=[unique_id, clustering, ranking])

