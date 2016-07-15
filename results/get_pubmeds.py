#!/usr/bin/env python

import urllib
import xml.etree.ElementTree as ET

def write_pubmed_count(gene):
    term = 'term=cancer+AND+' + gene
    query = 'entrez/eutils/esearch.fcgi?db=pubmed&' + term
    url = 'https://eutils.ncbi.nlm.nih.gov/' + query
    site = urllib.urlopen(url)
    xml_string = site.read()
    site.close()
    root = ET.fromstring(xml_string)
    count = root[0].text
    string = '{}\t{}'.format(gene, count)
    print string

if __name__ == '__main__':
    with open('genes.txt', 'r') as genes:
        print 'Gene\tCount'
        for gene in genes.readlines():
            write_pubmed_count(gene.strip())
else:
    print 'This module is to be run standalone!'
