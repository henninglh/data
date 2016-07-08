#!/usr/bin/env python
import pandas as pd

# Filenames
mitab_name = 'mitab_lite.tsv'

# Clean MITAB-MINI file from iRefWeb
mitab_table = pd.read_table('mitab_lite.txt')
mitab_table.to_csv(mitab_name, sep='\t', columns=['a_alias', 'b_alias'],
        index=False)

protein_to_gene = dict()

# Fill the protein_to_gene dictionary
with open('hgnc2.txt', 'r') as hgnc_file:
    hgnc_file.readline()
    
    for line in hgnc_file.readlines():
        info = line.split(' ')

        if len(info) > 1:
            for protein in info[1:]:
                protein_to_gene[protein.strip()] = info[0].strip()
        else:
            print info

# Replace protein symbols with gene symbols - results in mitab_final.tsv
with open(mitab_name, 'r') as mitab_file,\
        open('mitab_final.tsv', 'w') as mitab_final:

    mitab_final.write(mitab_file.readline())

    for line in mitab_file.readlines():
        interaction = line.split('\t')

        source = interaction[0].strip()
        target = interaction[1].strip()

        if (source in protein_to_gene) and (target in protein_to_gene):
            mitab_final.write('{}\t{}\n'.format(protein_to_gene[source], 
                                                protein_to_gene[target]))
