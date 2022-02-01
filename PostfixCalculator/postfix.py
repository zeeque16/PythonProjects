postfixExpression = "231*+9-"

stack = []

count = 0
while (count < len(postfixExpression)):                                     # Looped until end of string
    if (postfixExpression[count].isdigit()):                                # Check to see if the string is a digit. If so, then append in list
        stack.append(postfixExpression[count])
    else:                                                                   # Else, pop the value from the list and perform calculation
        val1 = stack.pop()
        val2 = stack.pop()
        stack.append(str(eval(val2 + postfixExpression[count] + val1)))     # After calculation, append the answer back into the list
    count += 1

print("Your answer is: ", stack[0])