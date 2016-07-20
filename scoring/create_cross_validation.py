#!/usr/bin/env python

import numpy.random as r

with open('golden_standard.tsv', 'r') as golden,\
        open('golden_standard_cv.tsv', 'w') as cv,\
        open('cross_validation.tsv', 'w') as cross_validation:

    golden.readline()
    cv.write('gene_names\tscore\n')
    cross_validation.write('gene_names\tscore\n')

    standard = [line for line in golden.readlines()]
    golden_cv = []

    border = len(standard)
    percentage = int(border / 10)
    removals = r.random_integers(0, border - 1, percentage)

    print border
    a = 1
    b = 1
    for idx in xrange(border):
        if idx in removals:
            cross_validation.write('{}'.format(standard[idx]))
            a += 1
        else:
            cv.write('{}'.format(standard[idx]))
            b += 1

    print a
    print b
