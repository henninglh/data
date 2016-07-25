#!/usr/bin/env python

import matplotlib.pyplot as plt
    
found_in_cluster = list()
possible_in_cluster = list()

with open('cross_validation.txt', 'r') as possible,\
        open('cv_20_percent.tsv', 'r') as found:

    possible.readline()
    found.readline()

    possible_genes = set([line.strip() for line in possible.readlines()])
    identified = 0
    possibles = 0


    for line in found.readlines():
        info = line.split('\t')
        cluster = int(float(info[0].strip()))
        genes_with_scores = info[2].split(',')
        genes = set(tuple(map(lambda x: x.split(':')[0], genes_with_scores)))
        genes_identified = possible_genes.intersection(genes)
        identified += len(genes_identified)
        possibles += len(genes)

        found_in_cluster.append(len(genes_identified))
        possible_in_cluster.append(len(genes))

    print 'Percentage found in the top 20% genes:',((float(identified)
        / float(possibles)) * 100)

print found_in_cluster
print len(found_in_cluster)

ax = plt.subplot(111)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.xticks(range(0, len(found_in_cluster) + 1, 1), fontsize=14)
plt.yticks(range(0, 5, 1), fontsize=14)

plt.title('Genes in top 20 percent that was removed by cross validation', fontsize=20)
plt.xlabel('Cluster rank', fontsize=16)
plt.ylabel('Number of genes', fontsize=16)

plt.hist(found_in_cluster, color='#3F5D7D')
plt.savefig('removed_by_cv.png', bbox_inches='tight')
