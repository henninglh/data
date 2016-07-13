#!/usr/bin/env sh
head -n 1 "curated_gene_disease_associations.tsv" > $1
grep -i "prostatic\|prostate" curated_gene_disease_associations.tsv >> $1
