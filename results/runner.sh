#!/usr/bin/env sh
# $1 is algorithm abbreviation in upper case letters
for x in *.csv; do
    ./clean.py x "$1";
done