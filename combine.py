#!/usr/bin/env python
with open('mitab_distinct.txt', 'r') as mitab,\
        open('hgnc_formatted.txt', 'r') as hgnc,\
        open('approved_genes.txt', 'w') as genes:

    hgnc.readline() # remove header
    lines1 = mitab.readlines()
    lines2 = hgnc.readlines() # we need to iterate several times

    for line1 in lines1:
        mline = line1.strip()
        for line2 in lines2:
            hline = line2.strip()
            if mline in hline:
                gene_symbol = hline.split('\t')[1]
                genes.write('{}\t{}\n'.format(mline, gene_symbol))
                break
