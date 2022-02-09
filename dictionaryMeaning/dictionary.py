from nltk.corpus import wordnet

# Getting input from user for a word that they need defination for
word = input("Enter word that you want the defination for: ")

# Using nltk to get defination for the word
wordDef = wordnet.synsets(word)

# Using try catch in case a word that does not have defination is enetered
try:
    print(wordDef[0].definition())
except:
    print("Word not found")