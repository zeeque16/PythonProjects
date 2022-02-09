class Book:

    # Initializing the class
    def __init__(self, title, author, ISBN, ID):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.ID = ID

    # Function to print out the book details
    def __str__(self):
        return f"--------------------------\n{self.ID}. The book is {self.title}, written by {self.author} with ISBN number: {self.ISBN}\n-----------------------"

    # Function to update all the details in a book
    def updateBook(self, updateTitle, updateAuthor, updateISN):
        self.title = updateTitle
        self.author = updateAuthor
        self.ISBN  = updateISN

    # Function to update book title
    def updateBookTitle(self, updateTitle):
        self.title = updateTitle

    # Function to update book author
    def updateBookAuthor(self, updateAuthor):
        self.author = updateAuthor

    # Function to update ISBN
    def updateBookISBN(self, updateISBN):
        self.ISBN = updateISBN

class Library:

    # Initializing the library class with a list of books
    def __init__(self, bookList):
        self.bookList = bookList

    # Function to add book
    def addBook(self, title, author, ISBN):
        if (self.bookList):                         # To check if the list is empty, if it is not then set it to the length of list
            ID = len(self.bookList)
        else:                                       # Else start from 0
            ID = 0

        newBook = Book(title, author, ISBN, ID)
        self.bookList.append(newBook)

    # To view items in library
    def printLibrary(self):                         
        for books in self.bookList:
            print(books)

    # To view a particular book
    def printBook(self, ID):
        print(self.bookList[ID])
    
    # To delete a particular book in library
    def deleteBook(self, ID):                       
        self.bookList.pop(ID)
    
    # To update all details of a particular book using ID
    def updateAllBookDetails(self, ID, updateTitle, updateAuthor, updateISBN):
        self.bookList[ID].updateBook(updateTitle, updateAuthor, updateISBN)

    # To update author of a particular book
    def updateBookAuthor(self, ID, updateAuthor):
        self.bookList[ID].updateBookAuthor(updateAuthor)
    
    # To update title of a particular book
    def updateBookTitle(self, ID, updateTitle):
        self.bookList[ID].updateBookTitle(updateTitle)

    # To update ISBN of a particular book
    def updateBookISBN(self, ID, updateISBN):
        self.bookList[ID].updateBookISBN(updateISBN)
    
# Main function for a list of options to be shown to user
def mainFunc():
    bookList = []

    library = Library(bookList)

    # Loop until user wants to exit
    while (True):
        option = int(input("Choose from the following optins:\n1. Add a book\n2. View Library\n3. View a Book\n4. Remove a Book\n5. Update a Book\n6. Exit\nEnter option:"))

        if (option == 1):
            title = input("Enter a title: ")
            author = input("Enter an author: ")
            ISBN = input("Enter an ISBN: ")
            library.addBook(title, author, ISBN)
            print("Book added")
        elif (option == 2):
            library.printLibrary()
        elif (option == 3):
            ID = int(input("Enter ID of book: "))
            library.printBook(ID)
        elif (option == 4):
            ID = int(input("Enter ID of book: "))
            library.deleteBook(ID)
            print("Book removed")
        elif (option == 5):
            ID = int(input("Enter ID of book you want to update: "))

            updateOptions = int(input("Do you want to:\n1. Update Title\n2.Update Author\n3. Update ISBN\n4. Update all details\nEnter option:"))

            if (updateOptions == 1):
                updateTitle = input("Enter new title: ")
                library.updateBookTitle(ID, updateTitle)
                print("Title updated")
            elif (updateOptions == 2):
                updateAuthor = input("Enter new author: ")
                library.updateBookAuthor(ID, updateAuthor)
                print("Author updated")
            elif (updateOptions == 3):
                updateISBN = input("Enter new ISBN: ")
                library.updateBookISBN(ID, updateISBN)
                print("ISBN updated")
            elif (updateOptions == 4):
                updateTitle = input("Enter new title: ")
                updateAuthor = input("Enter new author: ")
                updateISBN = input("Enter new ISBN: ")
                library.updateAllBookDetails(ID, updateTitle, updateAuthor, updateISBN)
                print("All book details updated")
        
        elif (option == 6):
            break
        
        else:
            print("Choose a valid option")
    
if __name__ == '__main__':
    
    mainFunc()