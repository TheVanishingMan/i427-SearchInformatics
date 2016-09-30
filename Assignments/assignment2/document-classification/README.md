# Alexander L. Hayes: bash commands for splitting and creating test and training sets.

# create a single training set of 2225 files; each command starts from the file of origin (i.e. run business in the business/ directory)
for file in *.txt; do cp $file ../all-documents/business-$file; done
for file in *.txt; do cp $file ../all-documents/entertainment-$file; done
for file in *.txt; do cp $file ../all-documents/politics-$file; done
for file in *.txt; do cp $file ../all-documents/sport-$file; done
for file in *.txt; do cp $file ../all-documents/tech-$file; done

# all-documents/ : get all words in .txt files onto one line (for easier scraping)
for file in *.txt; do echo $file && TEMP=`cat $file` && echo $TEMP > TEMPO.tmp && mv TEMPO.tmp $file; done

# randomly split files into training and test set (70% 30%):
(all-documents/ contains a randomsplit.sh script, run with 'bash randomsplit.sh' while in the all-documents directory)
#randomsplit.sh function:


```
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
	cp $file /u/hayesall/classes/i427/Assignments/assignment2/document-classification/training-set
	TOTALTRUE=$[$TOTALTRUE+1]
	TOTAL=$[$TOTAL+1]
	echo $TOTAL
    else
	#echo "FALSE $VAR"
	cp $file /u/hayesall/classes/i427/Assignments/assignment2/document-classification/testing-set
	TOTALFALSE=$[$TOTALFALSE+1]
	TOTAL=$[$TOTAL+1]
	echo $TOTAL
    fi
done
echo "$TOTALTRUE documents added to the training set"
echo "$TOTALFALSE documents added to the test set"
```

# Now we need to build a great training set with all of the words from each type of document (sports, tech, politics, etc.)
# Preprocess all of the documents from their respective categories (remove all punctuation so we are just left with the lower-
# case versions of all of the words separated by spaces).

for file in training-set/business-*; do echo $file && bash makeOneLine.sh $file > TEMPO.tmp && python preprocess.py TEMPO.tmp >> business-words.txt && rm -f TEMPO.tmp; done

# (repeat for entertainment, tech, sports, and politics)

# But we forgot something! After using this method to extract all of the words, everything is on different lines again!
# Luckily we can use the same trick on the same file (then if we do `wc -l business-words.txt` we will see everything is on 1 line)

bash makeOneLine.sh business-words.txt > TEMPO.tmp && mv TEMPO.tmp business-words.txt

# To be fair we need to do the same thing for all the files in the testing set:

[hayesall@tank testing-set]$ for file in *.txt; do echo $file && bash makeOneLine.sh $file > TEMPO.tmp && python preprocess.py TEMPO.tmp > TEMPI.tmp && mv TEMPI.tmp $file && rm -f TEMPO.tmp; done

# `wc -l *.txt` should produce 1 for every file.

# Now that my testing and training data was set up, I just needed to write the classifier.