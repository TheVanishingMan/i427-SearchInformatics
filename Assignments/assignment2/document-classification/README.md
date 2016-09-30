####Alexander L. Hayes / Document Classification

Using a combination of python and bash scripts

#####Step 1:

Create a single training set of 2225 files; each command starts from the file of origin (i.e. run business in the business/ directory)

```bash
for file in *.txt; do cp $file ../all-documents/business-$file; done
for file in *.txt; do cp $file ../all-documents/entertainment-$file; done
for file in *.txt; do cp $file ../all-documents/politics-$file; done
for file in *.txt; do cp $file ../all-documents/sport-$file; done
for file in *.txt; do cp $file ../all-documents/tech-$file; done
```

It would also be nice if all words were stored on a single line (for easier scraping):


# all-documents/ : get all words in .txt files onto one line (for easier scraping)
for file in *.txt; do echo $file && TEMP=`cat $file` && echo $TEMP > TEMPO.tmp && mv TEMPO.tmp $file; done

#####Step 2:

Randomly split files into training and test sets (70% 30%):

Run with 'bash randomsplit.sh' while in the all-documents directory (I've moved files around for easier viewing).


```bash
#!/bin/bash

# Quick highlight of the randomsplit.sh code

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

#####Step 3:

Now we need to build a great training set with all of the words from each type of document (sports, tech, politics, etc.)

Preprocess all of the documents from their respective categories (remove all punctuation so we are just left with the lower case versions of all of the words separated by spaces).  Repeat for entertainment, tech, sports, and politics.

```bash
for file in training-set/business-*; do echo $file && bash makeOneLine.sh $file > TEMPO.tmp && python preprocess.py TEMPO.tmp >> business-words.txt && rm -f TEMPO.tmp; done
```

But we forgot something! After using this method to extract all of the words, everything is on different lines again!

Luckily we can use the same trick on the same file (then if we do `wc -l business-words.txt` we will see everything is on 1 line)

```bash
bash makeOneLine.sh business-words.txt > TEMPO.tmp && mv TEMPO.tmp business-words.txt
```

#####Step 4:

To be fair we need to do the same thing for all the files in the testing set:

```bash
for file in *.txt; do echo $file && bash makeOneLine.sh $file > TEMPO.tmp && python preprocess.py TEMPO.tmp > TEMPI.tmp && mv TEMPI.tmp $file && rm -f TEMPO.tmp; done
```

`wc -l *.txt` should produce 1 for every file.

#####Step 5:

Now that testing and training data is set up, we can run the classifier.  It looks for tech-words.txt, etc. in the same directory as it is run in.