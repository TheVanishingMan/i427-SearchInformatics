import sys
import nltk

#accumulator = 0

# Consider how to process an arbitrary number of inputs:
# http://stackoverflow.com/questions/3559477/handling-arbitrary-number-of-command-line-arguments-in-python
arg_list = []
for arg in sys.argv[1:]:
    arg_list.append(arg)

def input_test():
    if len(arg_list) < 2:
        print "\033[0;31mError, invalid number of arguments, you need at least a mode and a word\033[0m"
        exit()
    else:
        print "\033[1;32mNumber of arguments is valid.\033[0m"
    if arg_list[0] not in ['or', 'and', 'most']:
        print "\033[0;31mError, mode is invalid (you chose: " + str(arg_list[0]) + "), please select from (or, and, most).\033[0m"
        exit()
    else:
        print "\033[1;32mMode is valid.\033[0m"

input_test()

sentence = "Hello my name is Elder Price"
tokens = nltk.word_tokenize(sentence)
print tokens
# mode options:
#  - or:   return pages that have any of the keywords
#  - and:  return pages that have all of the keywords
#  - most: return pages that have at least half of the keywords (with odd numbers, use your best judgement)

def test_var_args(f_arg, *argv):
    print "the mode: ", f_arg
    for arg in argv:
        print "word to check: : ", arg

#test_var_args('yasoob', 'python', 'eggs', 'toast', 'bacon')
#test_var_args(arg_list)

print arg_list
print "the mode:", arg_list[0]
arg_list = arg_list[1:]
print arg_list
