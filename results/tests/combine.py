#!/usr/bin/env python
import sys

file1 = sys.argv[1].strip()
file2 = sys.argv[2].strip()
file_out = sys.argv[3].strip()

with open(file1, 'r') as f1,\
        open (file2, 'r') as f2,\
        open (file_out, 'w') as out:

    f1.readline() # Remove header
    f2.readline() # Remove header
    out.write('gene_names\n')

    gene1 = set((line.strip() for line in f1.readlines()))
    gene2 = set((line.strip() for line in f2.readlines()))

    for intersected in set.intersection(*[gene1, gene2]):
        out.write(intersected + '\n')
