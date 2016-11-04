###Assignment 4: Indexing

Alexander Hayes / hayesall

#####Part 1: `index.py`

Simple Instruction:

  0. Easy mode: `./buildindex.sh`
  1. Not easy mode:
    
    * `rm -f docs.dat` (this is done to ensure additional lines are not appended to the existing file)
    * `rm -f invindex.dat`
    * `python index.py pages/ index.dat`

There was a lot of stackoverflow/documentation checking in this section. At first I thought I would be able to use some old code I had for extracting text from html, but since the focus on this project was to get a representative set of text for the document I spent quite a bit of time trying to make sure that extra stuff wasn't slipping through (for example, comments <!-- --> or if statements checking for the type of browser).

I also ended up spending a considerable amount of time making sure that user inputs wouldn't cause errors. It's not the cleanest method, but the top 50-ish lines checking for things like number of inputs, the directory the user was pointing to, and the files contained within it.

Something interesting was that the order of input statements mattered in this that I hadn't really seen before. I imported `sys` and `os` at the top to do unit tests, but if I also imported nltk (for instance) in the same block, it would take longer to run the program. To compensate, I imported specific things for specific blocks of the code. I can act like my code is written in different files (by exiting if unit tests are not passed before any imports occur), even when in reality it's one.

The way I kept track of which files had been seen and the respective number of occurances of a word in that file was handled in a rather uncharacteristic way. Unique words (around 2994 of them) were stored as keys in the dictionary, where the value was a string of documents and the number of time that word appeared in the document (for example: '1.html:3 2.html:9 3.html:4'). I really just wanted to store a list, but obviously couldn't because lists can be altered. Later I realized that a tuple would probably have been helpful in this situation, but I hadn't thought of that by the time I had the code worked out in my head.

One notable thing I did for the docs.dat had to do with the title of the page. All " were removed and all spaces were converted into underscores. This was meant to make it easier if docs.dat was eventually read back into a dictionary (perhaps in retrieve.py) in order to make it easier to split on the spaces (for example: '3 bed, 1.5 bath' --> "3_bed,_1.5_bath"). You will see this reflected in docs.dat.

#####Part 2: `retrieve.py`

Simple Instructions:

  0. Easy mode:
    
    * as with life, sometimes there isn't any easy mode.

  1. Hard mode:

    * `python retrieve.py most parking theater cat`
    * as with life, sometimes that which looks difficult turns out to be easy.

I'll come out and say it, my solution is a mess. It works, I'm even pretty sure it's accurate, but it's a mess because most of the solutions I thought of changed drastically when I realized I also needed to take other small things into account. The code here has some few decent ideas combined with band-aids I used to patch the errors.

The first 80ish lines are mostly reading in files (docs.dat and invindex.dat) and making sure the user didn't drop bad data into the program.

Starting at line 85 we start seeing where the search takes place:

  * 'or' is the easiest conceptually: for each word the user queries it creates a set of files that appear in the inverted index.
  * 'and' uses sets in a somewhat clever way that may not immediatly obvious. For the first user-queried word, it creates a set of files that word appears in. For each subsequent word, a new set is created and the intersection is taken to ensure that only words that appear in each make it into the final list.
  * 'most' creates a new dictionary that keeps track of how many times the file appears in the inverted index for a particular word. After it runs through each file and each word, 'most' is calculated with `if v >= int(math.ceil(number_of_inputs/2))`