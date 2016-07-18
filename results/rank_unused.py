#!/usr/bin/env python

with open('unused.txt', 'r') as unused_file,\
        open('candidates_only.txt', 'r') as candidate_file,\
        open('unused_ranked.txt', 'w') as ranked_file:

    candidate_file.readline()
    unused = [line.strip() for line in unused_file.readlines()]
    ranked_file.write('gene\trank\n')

    rank = 1
    for line in candidate_file.readlines():
        candidates = line.split(',')
        if len(candidates) > 1:
            for candidate in candidates:
                if candidate.strip() in unused:
                    ranked_file.write('{}\t{}\n'.format(candidate.strip(), rank))
        else:
            if candidates[0].strip() in unused:
                ranked_file.write('{}\t{}\n'.format(candidates[0].strip(),
                    rank))
        rank += 1

