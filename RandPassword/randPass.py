from os import symlink
import random
import string

# Input number of digits
passLen = int(input("Enter number of digits for password: "))

# Defining the data needed 
lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

# Joining it all together
combined = lowerLetters + upperLetters + numbers + symbols

# Using random to select random characters and telling the length of password
joinedPass = random.sample(combined, passLen)

# Creating the password
password = "".join(joinedPass)

print("Your password is: ", password)