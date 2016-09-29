#!/bin/bash

function generate_random_number {
    number=$RANDOM
    RANGE=10
    let "number %= $RANGE"
    echo $number
}

TOTAL=0
TOTALTRUE=0
TOTALFALSE=0

for file in *.txt; do
    VAR=$(generate_random_number)
    if [[ $VAR -lt 7 ]]; then
	#echo "TRUE $VAR"
	cp $file ../training-set/
	TOTALTRUE=$[$TOTALTRUE+1]
	TOTAL=$[$TOTAL+1]
	echo $TOTAL
    else
	#echo "FALSE $VAR"
	cp $file ../testing-set/
	TOTALFALSE=$[$TOTALFALSE+1]
	TOTAL=$[$TOTAL+1]
	echo $TOTAL
    fi
done
echo "$TOTALTRUE documents added to the training set"
echo "$TOTALFALSE documents added to the test set"
