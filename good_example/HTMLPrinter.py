from .AbstractPrinter import AbstractPrinter

class HTMLPrinter(AbstractPrinter):
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

    def print(self, book):
        print (HTMLPrinter.htmlTemplate.format(book.id, book.title, book.author, book.publisher))
