#!/usr/bin/python3

class Book:
    htmlTemplate = '''
<html>
    <head>Book</head>
    <body>
        Id: {} </br>
        Title: {} </br>
        Author: {} </br>
        Publisher: {} </br>
    </body>
</html>
    '''

    def __init__(self, id, title, author, publisher):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher 

    def print(self):
        print ("Id: %s" % self.id)
        print ("Title: %s" % self.title)
        print ("Author: %s" % self.author)
        print ("Publisher: %s" % self.publisher)

    def printHTML(self):
        print (Book.htmlTemplate.format(self.id, self.title, self.author, self.publisher))

if __name__ == '__main__':
    book = Book(1, 'La insoportable levedad del ser', 'Milan Kundera', 'Maxi Tusquets')
    book.print()
    book.printHTML()    
    
