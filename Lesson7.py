"""
	Lesson 7: Sample programs for the python.
	Source Code Location: https://github.com/ViswanathanRamasamy/PythonSamplePgm.git
	Author Name: Viswanathan Ramasamy
	Email id: rviswawt@gmail.com
"""
===================================================
class Book:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def define_class_method(cls, name, age):
        return cls(name, age)
        
    @staticmethod
    def ex_static_function(instance, age):
        if instance.age > age:
            print(f"{instance.name} is an adult")
        else:
            print(f"{instance.name} is a minor")
            
my_book = Book.define_class_method("Viswa", 32)
print(my_book.name, my_book.age)
Book.ex_static_function(my_book, 18)
==========================
Viswa 32
Viswa is an adult
======================================================
class cname:
    BOOK_TYPE = ("newspaper","school","childrens", "college")
    __booklist = None
    #class method asccessing the class attribute
    @classmethod
    def getbooktype(cls):
        print(cls.BOOK_TYPE)
    
    def __init__(self,name,author,btype):
        self.name = name
        self.author = author
        if (btype not in cname.BOOK_TYPE):
            raise ValueError(f"{btype} is not listed")
        else:
            self.btype = btype
    @staticmethod
    def getList():
        if (cname.__booklist == None):
            cname.__booklist = [];
        return (cname.__booklist)
        
mycname1 = cname("viswa", "viswa1","school")
#mycname2 = cname("viswa", "viswa1","school1") ValueError
mycname2 = cname("viswa", "viswa1","college")

cname.getbooktype() #('newspaper', 'school', 'childrens', 'college')

#static method also needs to acessed using the class name
booklist1= cname.getList()
booklist1.append(mycname1)
booklist1.append(12)
print(booklist1) #[<__main__.cname object at 0x7f061ce4beb0>, 12]
=======================================

======================================
Types of inheritance

Single Level Inheritance:
B====>A

multiple Inheritance
--------------------
C is derived from B and A
class Son(Mother, Father):
----------------------------
Multilevel Inheritance

C ====>B===>A
B is derived from A and C is derived from B
============================
Hierarchical inheriance
===================
B====>A
C====>A

Hybrid Inheriance:
=====================
B====>A
C====>A
D ===> C and B
=================================


 
class parent:      
    def geeks(self):
        print("parent class")
        
    def pgeeks(self):
        print("pparent class") 

class child1(parent):
    def geeks(self):
        print("child1 class")
    
    def c1geeks(self):
        print("c1child1 class")
        
class child2(parent):
    def geeks(self):
        print("child2 class")

    def c2geeks(self):
        print("c2child2 class")
        
class child(child1,child2):
    def geeks(self):
        print("child class") 
    
    def cgeeks(self):
        print("c2child class")
        
# Driver code
ochild = child()
ochild.geeks() #Though the child1, 2 has the same function , child function will be called
ochild.c2geeks() #call the child2 class function since the child has no such function
ochild.c1geeks() #call the child1 class function since the child has no such function
============================
child class
c2child2 class
c1child1 class
=========================
==========================================
 
class parent:      
    def geeks(self):
        pass
 
class child(parent):
    def geeks(self):
        pass
 
# Driver code
print( issubclass(child, parent)) # True
print( isinstance(child(), parent)) #True

==============================================
#to create the abstract class we need the abc modules
#ABSTRACT CLASS WILL NOT HAVE ANY object
#ABSTRACT FUNCTION WILL BE OVERWRITTEN IN THE DRIVED CLASS
#if the instance attribute is present in bot the parent class and in the current class then intance variable name value will be printed. 
#if the instance attribute is present in bot the parent class but not in the current class then the first parent class intance variable name value will be 
#printed. child class will have all the instance attributes of the parent class

class A: # or class A():
    def __init__(self):
       print("aaaaa")
       self.a= "aaa"
       self.name = "foo"
       super().__init__()

class B():
    def __init__(self):
        print("bbbb")
        self.b= "bbb"
        self.name = "bar"
        super().__init__()
        
      
class C(A,B): #here super will call b since b is given first in the list
    def __init__(self):
        super().__init__() #if the super().__init__() is not present in both the parent then only A class will be called
        print("viswa")

    def getname(self):
        print(self.a)
        print(self.b)
        print(self.name) # method resolution order
mc = C()
mc.getname()
print(C.__mro__) #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
======================
aaaaa
bbbb
viswa
aaa
bbb
bar
======================
============================

class A:
    def __init__(self):
       print("aaaaa")

class B():
    def __init__(self):
        print("bbbb")
      
class C(B,A):
    def __init__(self):
        A.__init__(self)  #aaa

MC = C()
======================================================
#to create the abstract class we need the abc modules
#ABSTRACT CLASS WILL NOT HAVE ANY object
#ABSTRACT FUNCTION WILL BE OVERWRITTEN IN THE DRIVED CLASS
#abc is abstract module present in python
from abc import ABC, abstractmethod

class Graphics(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def area(self):
        pass
    
    def area1(self):
        print("viswa");

class Square(Graphics):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        print(self.side*self.side)

class Circle(Graphics):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        print(3.14*self.side**2)

mysquare = Square(19)
mysquare.area();
mysquare.area1();
======================
361
viswa
================================================
interface class:
==================
#it is not necessary to have the init function in the abstract class all the time if the attributes are initialized
## {{ is required when we want to print {
from abc import ABC, abstractmethod

class Jsonnotify(ABC):
    @abstractmethod
    def notify(self):
        pass
    
class Graphics(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def area(self):
        pass

class Circle(Graphics,Jsonnotify):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return (3.14*self.side**2)

    def notify(self):
        print (f"circle : {self.area()}") #circle : 12.56
        print (f"{{\" circle\":{str(self.area())} }}") #{" circle":12.56 }
		 print ("{\" circle\":str(self.area())  }") #" circle":str(self.area())  }

mysquare = Circle(2)
mysquare.notify();
==========================
composition build on other object and has the relation ship.
==========================================
cclass author:
    def __init__(self,bname,lname):
        self.bname = bname
        self.lname = lname
    
    def __str__(self):
        return (f"{self.lname} {self.bname}")
        
class chapter:
    def __init__(self,cname,npages):
        self.cname = cname
        self.npage = npages

class book:
    def __init__(self, nbook,publisher, author):
        self.nbook = nbook
        self.publisher = publisher
        self.author = author
        self.lchapter = []
    
    def append(self,chapter):
        self.lchapter.append(chapter)
    
    def getbookpage(self):
        total = 0;
        for c in self.lchapter:
            total += c.npage
        return (total)
        
oauthor = author("Viswanathan", "Ramasamy")
mybook = book("LetusC++","Hindupublisher",oauthor)
mybook.append(chapter("lesson1",180))
mybook.append(chapter("lesson2",10)) 
print(mybook.author) #Ramasamy Viswanathan
print(oauthor) #Ramasamy Viswanathan
print(mybook.getbookpage()) #190

===========================================
Ramasamy Viswanathan
190
========================================================
class Publication:
    def __init__(self, title,author):
        self.title = title
        self.author = author

class Periodical(Publication):
    def __init__(self,title,author,period,publisher):
        super().__init__(title,author)
        self.period = period
        self.publisher = publisher

class book(Publication):
    def __init__(self,title,author,pages):
        super().__init__(title,author)
        self.pages = pages
        
class Magazine(Periodical):
    def __init__(self,title,author,period,publisher):
        super().__init__(title,author,period,publisher)
        
class Newspaper(Periodical):
    def __init__(self,title,author,period,publisher):
        super().__init__(title,author,period,publisher)

newspapaper = Newspaper("hindu","viswanathan",1,"hindu")
print(newspapaper.title, newspapaper.author, newspapaper.period, newspapaper.publisher)
===============================
hindu viswanathan 1 hindu

=================================

 
class grandparent:      
    def __init__(self, grandfather):
        self.grandfather = grandfather
        
class parent(grandparent):
    def __init__(self,parentname,grandfather):
        self.parentname = parentname
        grandparent.__init__(self,grandfather)
    
class child(parent):
    def __init__(self,childname,parentname,grandfather):
        self.childname = childname
#how to call the base class function using the paerent class name or super()
        #super().__init__(parentname,grandfather) or
        parent.__init__(self,parentname,grandfather)
        
# Driver code
ochild = child("richick","viswa","ramasamy")
print(ochild.childname)
print(ochild.parentname)
print(ochild.grandfather)
========================================
richick
viswa
ramasamy
=========================================================================
class MyInt:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Create an instance of the custom integer class
my_int = MyInt(42)

# Now, when you print the object, it will use the custom string representation
print(my_int)  # This will print: 42
===================================================
================================
class A:
    def __init__(self):
       print("aaaaa")

class B():
    def __init__(self):
        print("bbbb")
      
class C(B,A): #here super will call b since b is given first in the list
    def __init__(self):
        super().__init__()

MC = C()
=============
bbbbbbbbbbbb
=========
class A:
    def __init__(self):
       print("aaaaa")
       super().__init__()

class B():
    def __init__(self):
        print("bbbb")
        super().__init__()
      
class C(B,A): #here super will call b since b is given first in the list
    def __init__(self):
        super().__init__()

MC = C()
========================
bbbbbbbbbbbb
aaaaa

==============================
	class book:
    def __init__(self,name,author,price,discount):
        self.name = name
        self.author = author
        self.price = price
        self.discount = discount
    
    #getattribute will be called when the we we try to access the instance attribute     
    def __call__(self,name,author,price,discount):
        self.name = name
        self.author = author
        self.price = price
        self.discount = discount  
        
    def __str__(self):
        return(f"{self.name} {self.author} {self.price} {self.discount}")

mybook = book("test","viswa",36.35,0.1) # will call __init__
# is use to change more instance attribute at oneshot
mybook("test1","viswa1",136.35,10.1) # will call the __call__

print(mybook) # will call __str__
=======================================
test1 viswa1 136.35 10.1
=====================================
#compare 2 objects
class book:
    def __init__(self, name,author):
        self.name = name
        self.author =author
    
    #str method return the string
    def __eq__(self,value):
        if not isinstance(value, book):
            raise ValueError("value class name is not correct")
        return ((self.name == value.name) and
                (self.author == value.author))

mybook1 = book("Test","viswa")
mybook2 = book("Test","viswa")
print(mybook1 == mybook2) //TRUE
=================