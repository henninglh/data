#!/usr/bin/env python

with open('human_disease_knowledge_full.tsv', 'r') as f,\
        open('disease_know_scores.txt', 'w') as clean:
    f.readline()
    clean.write('genes\n')

    for line in f.readlines():
        _,gene,_,_,_,_,_ = map(lambda x: x.strip(), line.split('\t'))
        clean.write('{}\n'.format(gene))

