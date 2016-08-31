#!/bin/python

import sys
import os

def lastLetter(word):
    lastletter = word[-1:]
    lasttwo = word[-2:] #not elegant, but it works.
    secondtolast = lasttwo[:1]
    return lastletter + " " + secondtolast

print(lastLetter("APPLE"))
#should print: E L

print(lastLetter("EMACSRULES"))
#should print: S E

print(lastLetter("ILOVEBASH"))
#should print: H S

#commenting these out because strange behavior
#f = open(os.environ['OUTPUT_PATH'], 'w')

#_word = raw_input()

#res = lastLetter(_word);
#f.write(res + "\n")
#f.close()
