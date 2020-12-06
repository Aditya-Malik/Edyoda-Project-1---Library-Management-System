# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:04:38 2020

@author: adity
"""
from Book import Book
from Catalog import Catalog
from User import Member, Librarian
import sys


print("Testing Book.py:","\n")
b1 = Book('Shoe Dog','Phil Knight', '2015',312)
b1.addBookItem('123hg','H1B2')
b1.addBookItem('124hg','H1B3')
b1.printBook()
print("\n\n")
sys.stdout.flush()


print("Testing Catalog.py:","\n")
catalog = Catalog()
b = catalog._addBook('Shoe Dog','Phil Knight', '2015',312)
catalog._addBookItems(b, '123hg','H1B2')
catalog._addBookItems(b, '124hg','H1B4')
catalog._addBookItems(b, '125hg','H1B5')
b = catalog._addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog._addBookItems(b, '463hg','K1B2')
catalog._addBookItems(b, '466hg','K1B5')
catalog.displayAllBooks()
catalog._removeBookItem('124hg')
catalog.displayAllBooks()
catalog.searchByName('Shoe Dog')
catalog.searchByAuthor("Phil Knight")
catalog.searchByPublishDate("2015")
catalog.searchBookByMinPages(300)
catalog._removeBook("Shoe Dog")
catalog.displayAllBooks()
print("\n\n")
sys.stdout.flush()


print("Testing User.py:","\n")
print("\n")
print("Testing Librarian and its functions:","\n")
librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
print (librarian)
librarian.addBook('Shoe Dog','Phil Knight', '2015',312)
librarian.addBookItem("Shoe Dog", '123hg','H1B2')
librarian.addBookItem("Shoe Dog", '124hg','H1B4')
librarian.addBookItem("Shoe Dog", '125hg','H1B5')
librarian.addBook('Moonwalking with Einstien','J Foer', '2017',318)
librarian.addBookItem('Moonwalking with Einstien', '463hg','K1B2')
librarian.addBookItem('Moonwalking with Einstien', '466hg','K1B5')
librarian.displayAllBooks()
librarian.removeBookItemFromCatalog("125hg")
librarian.displayAllBooks()
librarian.removeBook("Shoe Dog")
librarian.displayAllBooks()
librarian.addBook('Shoe Dog','Phil Knight', '2015',312)
librarian.addBookItem("Shoe Dog", '123hg','H1B2')
librarian.addBookItem("Shoe Dog", '124hg','H1B4')
librarian.addBookItem("Shoe Dog", '125hg','H1B5')
librarian.displayAllBooks()
librarian.searchBook()
print("\n\n")

print("Testing Student and its functions:","\n")
m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
print (m1)
m1.issueBook("Moonwalking with Einstien",5)
m1.books_issued
m1.displayAllBooks()
m1.returnBook("466hg")
m1.books_issued
m1.displayAllBooks()
librarian.viewMembers()
m2 = Member("Aditya","Delhi",21,'dkbcwibwei23','std1234')
print (m2)
m2.issueBook("Shoe Dog")
m2.books_issued
m2.returnBook("123hg")
m2.books_issued
m2.searchBook()


librarian.viewMembers()