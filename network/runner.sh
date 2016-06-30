#!/bin/sh
./filter.py # Filter duplicates
./filter2.py # Filter 'rogid'
./filter3.py # Split and clean ID's
./format_hgnc.py # Insert NaN values
./combine.py # combines mitab and HGNC
./links.py # Create gene links
echo "Results is in <gene_links_final.txt>"
