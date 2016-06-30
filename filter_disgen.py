import sys

disgen_filename = sys.argv[1].strip()
prostate_filename = sys.argv[2].strip()

with open(disgen_filename, 'r') as disgen,\
        open(prostate_filename, 'r') as prostate,\
        open('prostate_genes_with_scores.tsv', 'w') as pscores:

    disgen.readline() # remoe the header
    prostate.readline() # remove the header
    pscores.write('geneID\tscore\n') # write header

    prostate_genes = set(line.rstrip() for line in prostate.readlines())

    for line in disgen.readlines():
        info = line.split('\t')
        gene_name = info[3].strip()
        score = info[2].strip()

        if gene_name in prostate_genes:
            pscores.write('{}\t{}\n'.format(gene_name, score))
            prostate_genes.remove(gene_name)

