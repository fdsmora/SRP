from .AbstractPrinter import AbstractPrinter

class ConsolePrinter(AbstractPrinter):
    def print(self, book):
        print ("Id: %s" % book.id)
        print ("Title: %s" % book.title)
        print ("Author: %s" % book.author)
        print ("Publisher: %s" % book.publisher)    