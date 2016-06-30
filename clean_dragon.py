#!/usr/bin/env python
with open('dragon.txt', 'r') as dragon_file,\
        open('dragon_clean.txt', 'w') as dragon_clean:
    dragon_clean.write('gene_names\n')
    for line in dragon_file:
        clean = ''.join(line.split(';')[1:-1]).replace('&nbsp', '')
        dragon_clean.write('{}\n'.format(clean))

