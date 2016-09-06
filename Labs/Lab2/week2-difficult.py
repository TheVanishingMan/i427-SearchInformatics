# Hackerrank: (python/itertools/Maximize It!)
# I'm 100% sure there's a cleaner way to do this, after I got the solution worked out
# there was a lot of time spent adapting old code to fit the updates I kept making.

# I had a brief moment of panick when I only passed 1 testcase, turns out I missed adding
# modulo to the maximum in line 28.  Crisis averted.

# Like a lot of the other problems this will not work well in it's current form on Burrow
# (results in an error if I am correct).  However, it does pass all test cases on Hackerrank.

from itertools import product

# this handles the first line (3 1000)
a,b = raw_input().split()
K = int(a) # --> 3
M = int(b) # --> 1000

input_list = []
while K: # handles the next K lines, ['2 5 4'] ['3 7 8 9'] ['5 5 7 8 9 10']
    input_list.append(raw_input())
    K -= 1 # turns them all into a single list: [['2 5 4'],['3 7 8 9'],['5 5 7 8 9 10']]

first = input_list[0].split()

output_list = []
# these weird, deranged blocks of code were a messy way to convert string arrays into arrays of ints
for i in range (0,len(input_list)):
    this_line = map(int, input_list[i].split())
    temporary = []
    for j in range(0,len(this_line)): # if you're reading this I am so sorry
        temporary.append(this_line[j] ** 2)
    output_list.append(temporary[1:]) # seriously, please forgive me, I can barely explain to myself
    i += 1 #how I solved this
    
permutations = map(list, product(*output_list)) # These last couple lines is really where the bulk of the 
maximum = 0                                     # work is done, just checking if a permutation is greater than maximum.
for number_list in permutations: # the end of 'house of leaves' was less confusing than this.
    if (sum(number_list) % M) > maximum:
        maximum = sum(number_list) % M
    else:
        continue
        
print maximum #print the final maximum and return it to the output
