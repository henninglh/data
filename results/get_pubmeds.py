#!/usr/bin/env python

import urllib
import xml.etree.ElementTree as ET
import sys

gene = sys.argv[1].strip()
url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=cancer+' + gene
site = urllib.urlopen(url)
xml_string = site.read()
site.close()
root = ET.fromstring(xml_string)
count = root[0].text
with open('genes/' + gene + '.txt', 'w') as gene_file:
    gene_file.write('{}\n'.format(count))
