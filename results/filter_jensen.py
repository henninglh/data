#!/usr/bin/env python

import operator

no_gene = '__NO_GENE__'

with open('jensen_cancerous.tsv', 'r') as diseases,\
        open('genes.txt', 'r') as clean_file,\
        open('z-values.tsv', 'w') as z_vals,\
        open('credibility.tsv', 'w') as creds,\
        open('cancers.tsv', 'w') as cancers,\
        open('unused.txt', 'w') as unused_file:

    clean_file.readline()
    jensen_genes = dict()
    genes = set()
    used = set()
    results = []
    z_vals.write('gene\tz-value\tcredibility\tdisease\n')
    creds.write('gene\tz-value\tcredibility\tdisease\n')
    cancers.write('gene\tz-value\tcredibility\tdisease\n')

    for line in clean_file.readlines():
        gene = line.strip()
        genes.add(gene)

    for line in diseases.readlines():
        gene = no_gene
        info = line.split('\t')
        candidate_id1 = info[0].strip()
        candidate_id2 = info[1].strip()
        disease = info[3].strip()
        zval = float(info[4].strip())
        credibility = float(info[5].strip())

        if candidate_id1 in genes:
            gene = candidate_id1
        elif candidate_id2 in genes:
            gene = candidate_id2

        if gene != no_gene:
            results.append([gene, zval, credibility, disease])
            used.add(gene)

    z_sort = sorted(results, key=operator.itemgetter(1, 2, 0), reverse=True)
    cred_sort = sorted(results, key=operator.itemgetter(2, 1, 0), reverse=True)
    gene_sort = sorted(results, key=operator.itemgetter(0, 1, 2), reverse=True)
    disease_sort = sorted(results, key=operator.itemgetter(3, 1, 2), reverse=True)
    unused = genes - used

    for gene in unused:
        unused_file.write('{}\n'.format(gene))

    for idx in range(len(results)):
        z_vals.write('{}\t{}\t{}\t{}\n'.format(z_sort[idx][0], z_sort[idx][1],
            z_sort[idx][2], z_sort[idx][3]))
        creds.write('{}\t{}\t{}\t{}\n'.format(cred_sort[idx][0], 
            cred_sort[idx][1], cred_sort[idx][2], cred_sort[idx][3]))
        cancers.write('{}\t{}\t{}\t{}\n'.format(disease_sort[idx][0],
            disease_sort[idx][1], disease_sort[idx][2], disease_sort[idx][3]))
