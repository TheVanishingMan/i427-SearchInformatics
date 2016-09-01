# Medium Problem 1: python/Introduction/"Write a function"

def is_leap(year):
    # Write your logic here
    leap = False
    cond1 = year % 4 == 0
    cond2 = year % 100 != 0 or year % 400 == 0
    if cond1 and cond2:
        leap = True
    return leap

year1 = 1990
print "Is 1990 a leap year?"
print is_leap(year1)
