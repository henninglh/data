#!/usr/bin/env python

import matplotlib.pyplot as plt

with open('candidates.tsv', 'r') as candidate_file:
    candidate_file.readline()

    ranks = []
    candidates = []

    rank = 1
    for line in candidate_file.readlines():
        info = line.split('\t')
        if len(info) == 3:
            candidates.append(len(info[2].split(',')))  # Sum of candidates
            ranks.append(rank)
            rank += 1



    ax = plt.subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    plt.xticks(range(0, len(candidates) + 1, 1), fontsize=14)
    plt.yticks(range(0, (len(ranks) + 20), 10), fontsize=14)

    plt.title('Candidate biomarker distribution', fontsize=20)
    plt.xlabel('Biomarkers', fontsize=16)
    plt.ylabel('Cluster ranks', fontsize=16)

    plt.hist(candidates, color='#3F5D7D', bins=max(candidates))
    print max(candidates)

    plt.savefig('candidates.png', bbox_inches='tight')
