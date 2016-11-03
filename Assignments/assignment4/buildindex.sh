#!/bin/bash
if [[ -e docs.dat ]]; then
    rm -f docs.dat
fi
if [[ -e invindex.dat ]]; then
    rm -f invindex.dat
fi
python index.py pages/ index.dat
sort invindex.dat > sortedinvindex.dat && mv sortedinvindex.dat invindex.dat
