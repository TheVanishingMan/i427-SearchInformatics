# Complete the function below.
# got really stuck on this one, some later inspiration came from:
# http://interactivepython.org/runestone/static/pythonds/BasicDS/BalancedSymbols(AGeneralCase).html
left = "([{"
right = ")]}"
output = []

def match(open, close):
    return left.index(open) == right.index(close)

def braces(values):
    total = len(values)
    print total
    for paren_string in values:
        balanced = True # true until false
        stack = [] #last in, first out
        counter = 0
        while (counter < len(paren_string)) and balanced:
            current_paren = paren_string[counter] # ()()[1] --> )
            if current_paren in left:
                stack.append(current_paren)
            else:
                if not stack:
                    balanced = False
                else:
                    top = stack.pop()
                    if not match(top, current_paren):
                        balanced = False
            counter = counter + 1
        if balanced and not stack: #if it's balanced and empty
            output.append("YES")
        else:
            output.append("NO")
    return output


test = []
test.append("()()()")
test.append("([)]")
test.append("{{(([[]]))}}")
print braces(test)
