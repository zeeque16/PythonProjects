import re

file = open('D:\\Project\\XflowInternship\\FileSearch\\randomFile.txt', mode='r')

sentences = file.read()

searchString = (input("Enter a string that you want to search: "))

if (searchString in sentences):
    print("The string that you are looking for can be found at: ")
    for match in re.finditer(searchString, sentences):
        print("\t", match.span())
else:
    print("Your desired string was not found in the file")

file.close() 