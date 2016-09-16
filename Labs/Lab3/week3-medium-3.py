# Question: K Candy Store
# Link: https://www.hackerrank.com/challenges/k-candy-store

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

# I figured combinations would be important here, turns out there isn't
# a great built-in version though.  It looks like 'itertools' has an 
# implementation for lists, but that wasn't really useful here.
# 'Mark Tolonen' suggested just writing the function:
# http://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python


# I kept failing tests cases and had to check the discussion section for the suggestion
# to convert from int to string then back again after taking [-9:], I glossed over the
# suggestion at the top to only print the last 9 digits if the number exceeded the limit.


# Once again this answer is fairly built into the raw_input(), so I will not include a 
# demonstration in this code.


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

total = int(raw_input())
while total:
    N = int(raw_input())
    K = int(raw_input())
    print int((str(nCr((N+K-1),K)))[-9:])
    total = total - 1
