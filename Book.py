# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:01:57 2020

@author: aditya
"""
from BookItem import BookItem


class Book:

    def __init__(self, title, author, publish_date, pages):

        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []
        
    def addBookItem(self, isbn, rack):
        b = BookItem(self, isbn, rack)
        self.book_item.append(b)
        self.total_count += 1
        
    def printBook(self):
        print(self.title, self.author)
        for book_item in self.book_item:
            print(book_item.isbn)
            
    def searchBookItem(self, isbn):
        for book_item in self.book_item:
            if isbn.strip() == book_item.isbn:
                return book_item
            
    def removeBookItem(self, title, book_item):
        if book_item in self.book_item:
            print(title," ",book_item,"successfully removed.")
            self.book_item.remove(book_item)
            self.total_count -= 1
            
    def __repr__(self):
        return self.title + ' ' + self.author
    
