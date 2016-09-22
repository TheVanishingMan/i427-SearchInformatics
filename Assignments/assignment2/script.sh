#!/bin/sh
DIRECTORY=$1
for file in $DIRECTORY/*; do V=`cat $file` && echo $V > TEMPO.tmp && echo $file && python a2.py TEMPO.tmp && rm -f TEMPO.tmp; done
