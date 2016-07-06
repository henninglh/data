#!/usr/bin/env python
with open('dragon.txt', 'r') as dragon_file,\
        open('dragon_clean.txt', 'w') as dragon_clean,\
        open('dragon_scores.tsv', 'w') as dragon_scores:
    dragon_clean.write('gene_names\n')
    dragon_scores.write('gene_names\tscores\n')

    for line in dragon_file:
        clean = ''.join(line.split(';')[1:-1]).replace('&nbsp', '')
        dragon_clean.write('{}\n'.format(clean))
        dragon_scores.write('{}\t{}\n'.format(clean, str(1)))

