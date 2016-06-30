#!/usr/bin/env python
distinct_set = set()
with open('mitab_nodup_no-rogid.txt', 'r') as f,\
        open('mitab_clean.txt', 'w') as clean,\
        open('mitab_distinct.txt', 'w') as distinct:
    f.readline() # remove header
    for fline in f.readlines():
        line = fline.split('\t')
        source = line[0].split(':')[1].strip()
        target = line[1].split(':')[1].strip()

        distinct_set.add(source)
        distinct_set.add(target)
        
        clean.write('{}\t{}\n'.format(source, target))

    for unique in distinct_set:
        distinct.write('{}\n'.format(unique))
