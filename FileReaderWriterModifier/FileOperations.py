# Creating a new file and writing a string to it
file = open("D:\\Project\\XflowInternship\\FileReaderWriterModifier\\NewFile.txt", mode="w")
file.write("This is a random text")
file.close()

# Reading a file
file = open("D:\\Project\\XflowInternship\\FileReaderWriterModifier\\NewFile.txt", mode="r")

itemInFile = file.read()
print("Item in string is:")
print('\t' + itemInFile)

file.close()

# Modifing a file
file = open("D:\\Project\\XflowInternship\\FileReaderWriterModifier\\NewFile.txt", mode="a")

file.write("\nThis is another line in the text")

file.close()