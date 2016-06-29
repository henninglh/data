#!/usr/bin/env python
with open('mitab_nodup.txt', 'r') as f,\
        open('mitab_nodup_no-rogid.txt', 'w') as out:
    for line in f.readlines():
        if not 'rogid' in line:
            l = line.split('\t')
            out.write('{}\t{}\n'.format(l[1].strip(), l[2].strip()))
