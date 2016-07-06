#!/usr/bin/env sh
# x is filename to run through clean.py
# $1 is clustering algorithm abbreviation in upper case letters
# $2 is ranking algorithm in upper case letters

for x in *.csv; do
    ./clean.py x "$1 $2";
done
