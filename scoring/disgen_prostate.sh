#!/bin/bash
bash prostate_only.sh "$1"
python averager.py "$1"
rm "$1"
