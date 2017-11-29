#!/bin/bash
dim=3
min=-5
max=5

rm -rf priv pub
mkdir priv
mkdir pub
python gen_b_no_lll.py $dim $min $max | fplll > lll.txt
python gen_keys.py
rm lll.txt

