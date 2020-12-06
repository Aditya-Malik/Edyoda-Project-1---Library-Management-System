# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:04:10 2020

@author: adity
"""
from Book import Book

class Catalog:
    
    issuedBooks=[]
    Books=[]
    books=[]
    different_book_count=0
    
    @classmethod
    def addBookList(cls,book):
        cls.books.append(book)
    
    def __init__(self):
        #self.different_book_count = 0
        #self.books = []
        print("Catalog created.")
        
    #Only available to admin
    def _addBook(self,title,author,publish_date,pages):
        b = Book(title,author,publish_date,pages)
        #self.different_book_count += 1
        Catalog.different_book_count += 1
        #self.books.append(b)
        Catalog.books.append(b)
        Catalog.Books.append(title)
        return b
    
    #Only available to admin
    def _addBookItems(self,book,isbn,rack):
        book.addBookItem(isbn, rack)
        
    #Only available to admin
    def _addBookItem(self,title, isbn, rack):
        for book in Catalog.books:
            if book.title == title:
                Book.addBookItem(book, isbn, rack)
                print("Book Item {} has been added successfully!".format(isbn))
        
        
    def searchByName(self,title):
        for book in Catalog.books:
            if title.strip() == book.title:
                return book
    # done
    def searchByAuthor(self,author):
        for book in Catalog.books:
            if author.strip() == book.author:
                return book
            
    def searchByPublishDate(self,publish_date):
        val=False
        for book in Catalog.books:
            if int(book.publish_date) == int(publish_date):
                print(book.title,"on/in",book.publish_date)
                val=True
                break
        if val == False:
            print("No book published on the date stated.")
    
    def searchBookByMinPages(self,pages):
        l1=[]
        for book in Catalog.books:
            if int(book.pages) >= int(pages):
                l1.append(book.title)
        if len(l1)==0:
            print("No book of this length exists here.")
        else:
            print(l1)
        
    def displayAllBooks(cls):
        print ('Different Book Count',Catalog.different_book_count)
        c = 0
        for book in Catalog.books:
            c += book.total_count
            book.printBook()
        print ('Total Book Count',c)
        print(Catalog.books)
    
    def _removeBook(self,title):
        for book in Catalog.books:
            if book.title == title:
                Catalog.books.remove(book)
                Catalog.different_book_count -= 1
                print("Book",title,"has been removed from the catalog!")
        
    def _removeBookItem(self,isbn):
        for book in Catalog.books:
            for book_item in book.book_item:
                if book_item.isbn == isbn:
                    book.book_item.remove(book_item)
                    book.total_count -= 1
                    print("Item:",isbn,"of",book.title,"has been removed from the catalog!")
        
        
    def addToIssued(book_item):
        Catalog.issuedBooks.append(book_item)