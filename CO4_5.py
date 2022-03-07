"""
5. Create a class Publisher (name). Derive class Book from Publisher with attributes title and
author. Derive class Python from Book with attributes price and no_of_pages. Write
a program that displays information about a Python book. Use base class constructor invocation and
method overriding.
"""
class Publisher:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("Book name is ",self.name)

class Book(Publisher):
    title=" "
    author=" "
    def __init__(self,title,author):
        self.title=title
        self.author=author

class Python(Book):
    price=0.0
    no_of_pg=0
    def __init__(self,price,no_of_pg):
        self.price=price
        self.no_of_page=no_of_pg
        Book.__init__(self,'rahul','rah')
        Publisher.__init__(self,'rahulms')
    def display(self):        
        print("inside book")
    
py=Python(10,20)

py.display()