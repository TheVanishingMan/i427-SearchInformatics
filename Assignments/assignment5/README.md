####Alexander L. Hayes, Assignment 5
#####hayesall(at)indiana(dot).edu

I'll keep this pretty short (README may need some additional explanation at some point).

How to run the code: `python retrieve2.py theater cat garage`

  * A quick comment because self-plagiarism is a thing: almost all of this code was based on my implementation of retrieve.py in assignment4. Similarities between that code and the code presented here are by design, the largest difference is the removal of the modes and implementation of term-frequency.

I based my understanding of term frequency off the Wikipedia page: https://en.wikipedia.org/wiki/tf-idf
A maximum of 25 items are returned, sorted by the term frequency. The term frequency is the number on the left, reduced to three decimal places to make the output easier to read.

If you run:

`python retrieve2.py garage`:

Results will be of the form (21 not listed here):

  0.077) http://bloomington.craigslist.org/apa/5838647764.html  -----  "Large Stand-Alone Home with 2-car Garage"

  0.077) http://bloomington.craigslist.org/apa/5838650563.html  -----  "Spacious Luxury Paired Home w/ Oversized 2-car garage"

  0.038) http://bloomington.craigslist.org/apa/5838631088.html  -----  "Open & Spacious Layout -- Exciting Master Suite"

  0.038) http://bloomington.craigslist.org/apa/5836757371.html  -----  "***ULTRA NICE LARGE 4BR/GREAT LOCATION!!***"
