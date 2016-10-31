#!/bin/bash

TOTAL=0
CORRECT=0
ERRORS=0

for file in testing-set/*.txt; do
    ACTUALFILECLASS=$(echo $file | cut -f 2 -d '/' | cut -f 1 -d '-')
    OUTPUT=$(python classify.py $file)
    if [[ $OUTPUT = $ACTUALFILECLASS ]]; then
	VAL=true
	CORRECT=$[$CORRECT+1]
    else
	VAL=false
	ERRORS=$[$ERRORS+1]
    fi
    TOTAL=$[$TOTAL+1]
    printf "$file | $ACTUALFILECLASS | $OUTPUT | $VAL | TCE=$TOTAL/$CORRECT/$ERRORS\n"
done
