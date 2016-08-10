#!/usr/bin/env python
import sys

d = sys.argv[1].strip() + '/'

for i in xrange(1, 11):
    number = str(i)
    is_cancer = len(sys.argv) == 3
    if is_cancer:
        number = '_cancer' + number

    with open(d + 'clusters' + number + '.tsv', 'r') as clean,\
            open(d + 'cross_validation' + number + '.txt', 'r') as cross_validation,\
            open(d + 'cross_validation_matched' + number + '.txt', 'w') as matched,\
            open(d + 'cross_validation_unmatched' + number + '.txt', 'w') as unmatched,\
            open(d + 'cv_distribution' + number + '.tsv', 'w') as distribution:

        clean.readline()
        cross_validation.readline()
        matched.write('gene_names\n')
        clean_genes = filter(lambda x: float(x.split('\t')[1]) > 0.0,
                [line for line in clean.readlines()])
        cross_val_genes = set([line.strip() for line in
            cross_validation.readlines()])
        identified_genes = set()
        hits = 0
        ranks = []
        clusters = []

        for line in clean_genes:
            info = line.split('\t')
            genes = set([i.split(':')[0].strip() for i in info[2].split(',')])
            candidates = set([a.split(':')[0] for a in 
                    filter(lambda x: float(x.split(':')[1].strip()) == 0.0, 
                    [i for i in info[2].split(',')])])
            intersect = list(cross_val_genes.intersection(candidates))
            map(lambda x: identified_genes.add(x), intersect)
            hits += len(intersect)
            ranks.append(float(len(intersect)) / float(len(genes)))
	    cluster_line = info[0].strip() + '_' + info[2].strip() + '(' + ''.join(intersect) + ')'
            clusters.append(cluster_line)

        for gene in identified_genes:
            matched.write('{}\n'.format(gene))

        for gene in (cross_val_genes - identified_genes):
            unmatched.write('{}\n'.format(gene))

        rank = 1
        for idx, candidates in enumerate(ranks):
            distribution.write('{}\t{}\t{}\n'.format(rank, candidates, clusters[idx]))
            rank += 1

        print '======================='
        print 'total possible matches:', len(cross_val_genes)
        print 'matches:', hits
        print 'misses:', len(cross_val_genes) - hits
        print 'percentage:',float(hits) / float(len(cross_val_genes))
