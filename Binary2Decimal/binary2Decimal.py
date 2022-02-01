def decimalToBinary(n):
    binary = ""                 # String variable is declared to append the values
    while (n > 0):              # Looped till the value is zero
        binary += str(n%2)
        n = n//2
    
    return binary[::-1]         # Returned string is reversed so that the correct binary value is returned

def binaryToDecimal(n):         
    decimalVal, count = 0, 0    # 2 variables are declared, one for the decimal value that would be returned and count which will incremented once           
    while (n != 0):             # Looped through till value is zero
        decimalVal += ((n%10) * (2 ** count))
        count += 1
        n = (n // 10)
    
    return decimalVal

print(decimalToBinary(13))
print(binaryToDecimal(110))