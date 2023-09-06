python work on different platform like windows, mac, linux, raspherry-pi. python is easy to learn. 
python needs few lines of code when compare to other language.
python is used in google, netflex, facebook and spotify
in python there is no intermediate executable file or binary file. in python compiler convert the
 source file into bytecode and then interpretor run on it.
python is general purpose programming langauge  and cabaple of scripting as well.
python package has python modules. python module consists of class and function.
python object takes heap memory and release by garbage collector when it is not in use. 
python can be used as object oridented programming as well structural oridented programming.
python support several libraries and frame work like NumPy and SciPy, Django
NumPy and SciPy are used for scientific computation
SciPy uses the NumPy,
Django: web framework, clean, programatic and design

Highly Supportive Community and instead open parthesis python uses intention.
========================================
c0mment statement

#This is a comment
#written in
#more than just one line

======>
"""
This is a comment
written in
more than just one line
"""
===============
=======================
some datastructures present in python:
list => mutable ie can be modified l = ["viswa","hi"],
list:Negative indexing means start from the end.
thislist.remove("banana") #If "banana" is found in the list, it will be remove the first occurance of the banana, and the list will be modified in place.
#If "banana" is not in the list, it will raise a ValueError exception
l = thislist.pop(1) //index # will return the poped element
thislist.pop() last element 
del thislist[0] # no return of the removed element.  you try to execute del thislist[0] on an empty list (a list with no elements), it will raise an IndexError
del thislist //delete the variable
thislist.clear() //clear only the content but empty list still available
tuple => immutable , cannot be modified l= ("viswa","hi")
directory => map l={1:"viswa",2:"hi"} A dictionary is a collection which is ordered*, changeable and 
do not allow duplicates.
set => {"viswa","hi"}

data types:
string
list
tuple
directory
set
array
==============
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
================================
list:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  

storing the fruits with letter a in 2nd list:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
============================
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

or

list3 = list1 + list2
or
list1.extend(list2)
==================================
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)

output:
dict_keys(['brand', 'model', 'year'])
========================================
how to change the tuple element?
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
("apple", "kiwi", "cherry")
==========================================
#.keys is reference hence it is getting updated based on the new element
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) //see here we are not refering to the key again

car["brand"] == car.get("brand")
output:
==========
dict_keys(['brand', 'model', 'year'])
dict_keys(['brand', 'model', 'year', 'color'])
========================================

thisdict.update({"year": 2020}) /// we can update ie edit or add the new key value pair the dict
==================
thisdict.popitem()  will remove the last element
del thisdict["model"] ////delete any element
del thisdict //delete the entire list
thisdict.clear() //clear all the key and value and leave the empty list
======================
 
#dict .keys, .values both will give the list 
thisdict =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print (thisdict.keys())
for x in thisdict.keys(): or for x in thisdict:
  print(thisdict[x])
​
dict_keys(['brand', 'model', 'year'])
Ford
Mustang
1964
=============
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

brand Ford
model Mustang
year 1964
=======================
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values(): //dict_values(['Ford', 'Mustang', 1964])
  print(x)
  
Ford
Mustang
1964
========================

copy the dictonary
mydict = thisdict.copy()
mydict = dict(thisdict)
Python Decorator:
==================

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
​
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
​
print(myfamily)
​
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
=======================
python decorator are used to change the behaviour of the class or the function. 
It is used to wrap the function inorder to increase the functionality.
function are objects in c

# first method that return second method
def A(number):
	print("Inside the method A.", number)

returned_function = A(12) #return value none is assigned

output
Inside the method A. 12
-----------------------------
# first method that return second method
def A():
	print("Inside the method A.")
	# return second method
#	return B(number)

# form a object of first method
# i.e; second method
returned_function = A() #return value

# call second method by first method
returned_function
output
Inside the method A.
==============================================

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

('apple', 'banana', 'cherry', 'orange')
===========
fruits = ("apple", "banana", "cherry")

green, yellow, red = fruits // or (green, yellow, red) = fruits 

print(green)
print(yellow)
print(red)
====
apple
banana
cherry
==================================================
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

====
('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
======================

Python uses indentation to indicate a block of code.
===============================================
def A():
	print("Inside the method A.")
	# return second method
#	return B(number)

# form a object of first method
# i.e; second method
returned_function = A

# call second method by first method
returned_function()
output
Inside the method A.

=================================================
def str1():
    print("PythonGeeks")
def func1():
    return str1
var1 = func1() #here the str1 function name is assigned to the var1
var1()
pythonGeeks
===================================================
# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
    return text.upper() 
    
print(shout('Hello')) 
    
yell = shout 
    
print(yell('Hello'))
output
HELLO
HELLO 
=======================================================
print("Hello World", end=" hi ")
print("Hello World") 
//output will be Hello world hi Hello world

==================================================
//NESTED Function
def math():
    def square(num):
        return num**2
    print(square(2))
math()

output
4
=================================================
non local variable
def math(num): #num is non local variable
    def square(): # closure function
        return num**2
    print(square())
math(2)

==============================
str = "Viswanathan good"
str.split() ==> ['Viswanathan','good']

======================================
def html(func):
    def wrapper(*args, **kwargs): # variable arguments
        print("<html>")
        func(*args, **kwargs)
        print("</html>")
    return wrapper

def body(func):
    def wrapper(*args, **kwargs):
        print("<body>")
        func(*args, **kwargs)
        print("</body>")
    return wrapper

@html
@body
def text_printer(text):
    print(text)

text_printer("This is my text")

output
<html>
<body>
this is my test
<body>
<html>

==========
@html
@body
def text_printer(text):
    print(text)
    
can also be changed to 
text_printer = html(body(text_printer))
text_printer(This is my text")
========================================
def my_decor(func):
    def my_wrap(str1, str2):
        print("Decorator Function")
        return func(str1, str2)
    return my_wrap
    
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)

my_function = my_decor(my_function)
my_function("Mangoes", "Sweet")

output:
Decorator Function
Main Function
Mangoes are Sweet
======================================
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)

my_function = my_decor(my_function)
my_function("Mangoes", "Sweet")

can be changed to
@my_decor
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)

my_function("Mangoes", "Sweet")
====================================
def dollar(func):
    def wrapper():
        print("$$$$$")
        func()
        print("$$$$$")
    return wrapper

def hello():
    print("Hello World!")
hello = dollar(hello)
hello()
output:
$$$$$
Hello World!
$$$$$

=============================

def my_decor(func):
    def my_wrap(*args, **kwargs):
        print("Decorator Function")
        print(args,kwargs)
        return func(*args, **kwargs)
    return my_wrap
@my_decor
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)
my_function("Mangoes", "Delicious")

output
-------
Decorator Function
('Mangoes', 'Delicious') {}
Main Function
Mangoes are Delicious
====================================
def decorator_fun(func): #decorator
  print("Inside decorator")
 
  def inner(*args, **kwargs):   #wrapper
    print("Inside inner function")
    print("Decorated the function")
     
    func()
     
  return inner
 
 
def func_to():
    print("Inside actual function")
 
# another way of using decorators
decorator_fun(func_to)()
========================================
def decodecorator(x,y):
    print(".....viswanathan......1")
    def decorator(fun):
        print(".....viswanathan......2")
        def viswa():
            print(".....viswanathan......3")
            return fun()
        return viswa
    return decorator
 
 

@decodecorator("hi","viswa")
def summation():
    print("viswanathan")
    return 10
    
output:
.....viswanathan......1
.....viswanathan......2
===============================================
def decorator(fun):
    print(".....viswanathan......2")
    def viswa():
        print(".....viswanathan......3")
        return fun()
    return viswa
 
 
@decorator
def summation():
    print("viswanathan")
    return 10
 
.....viswanathan......2
=============================================
def decodecorator(x,y):
    print(".....viswanathan......1")
    def decorator(fun):
        print(".....viswanathan......2")
        def viswa():
            print(".....viswanathan......3")
            return fun()
        return viswa
    return decorator
 
 

@decodecorator("hi","viswa")
def summation():
    print("viswanathan")
    return 10

 print("======================viswanathan")
print(summation())

output
.....viswanathan......1
.....viswanathan......2
===================viswanathan
.....viswanathan......3
viswanathan
10
================================================
# some function
def first(msg):
    print(msg)

# second function
def second(func, msg):
    func(msg)

# calling the second function with first as argument
second(first, "Hello!")
=============================================
# first decorator
def star(f):
    def wrapped():
        return '**' + f() + '**'
    return wrapped

# second decorator
def plus(f):
    def wrapped():
        return '++' + f() + '++'
    return wrapped

@star
@plus
def hello():
    return 'hello'

print(hello())
output:
**++hello++**
==========================
import time

def timing(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args,**kwargs)
        end = time.time()
        print(f.__name__ +" took " + str((end-start)*1000) + " mil sec") # how to get the function name
        return result
    return wrapper

@timing
def calcSquare(numbers):
    result = []
    for number in numbers:
        result.append(number*number) # [1, 4, 9, 16, ...
    return result

@timing
def calcCube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

# main method
if __name__ == '__main__':
    array = range(1,500)
    sq = calcSquare(array)
    cube = calcCube(array)
 ----
 calcSquare took 0.07653236389160156 mil sec
calcCube took 0.10728836059570312 mil sec
======
def my_decorator(func):
    def my_wrapper(argument1, argument2):
        print("The arguments are: {0}, {1}".format(argument1, argument2))
        print("The arguments are: {}".format(argument1, argument2))
        print("The arguments are: {} and {}".format(argument1, argument2))
        func(argument1, argument2)
    return my_wrapper #When you write function name without brackets, it acts as a function object and it does not call function. 
    #The function gets called only when there is a function name (object) followed by brackets “()”


@my_decorator
def names(firstName, secondName):
    print("Your first and second names are {0} and {1} respectively".format(firstName, secondName))

print(names("Nicholas", "Samuel"))
------
output
The arguments are: Nicholas, Samuel
The arguments are: Nicholas
The arguments are: Nicholas and Samuel
Your first and second names are Nicholas and Samuel respectively
None
==============================================
def my_decorator(func):
    def my_wrapper(*args, **kwargs):
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        func(*args)
    return my_wrapper

@my_decorator
def function_without_arguments():
    print("No arguments")

function_without_arguments()

Positional arguments: ()
Keyword arguments: {}
No arguments
=================================================
def my_decorator(func):
    def my_wrapper(*args,**kwargs):
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        print('Keyword arguments:', kwargs["child1"]) #hemashree
        func(*args)
    return my_wrapper

#@my_decorator
#def function_without_arguments(text1,text2): 
#    print(text2 + " and " + text2) #viswa and Vimala

@my_decorator
def function_without_arguments(*args): 
    print(args[0] + " and " + args[1]) #viswa and Vimala

function_without_arguments("viswa","vimala",child1="hemashree", child2="rithick")

-----
Positional arguments: ('viswa', 'vimala')
Keyword arguments: {'child1': 'hemashree', 'child2': 'rithick'}
Keyword arguments: hemashree
viswa and vimala
=============================================
def my_decorator(func):
    def my_wrapper(*args,**kwargs):
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
       # print('Keyword arguments:', kwargs["child1"])
        func(*args, **kwargs)
    return my_wrapper

#@my_decorator
#def function_without_arguments(text1,text2): 
#    print(text2 + " and " + text2) #viswa and Vimala

@my_decorator
def function_without_arguments(*args):  
    print("args ") #empty

@my_decorator
def function_without_arguments(*args, **kwargs):  
    print("args1 ") #empty
    
function_without_arguments()
function_without_arguments("viswa","vimala", child1="hema")
=====
Positional arguments: ()
Keyword arguments: {}
args1 
Positional arguments: ('viswa', 'vimala')
Keyword arguments: {'child1': 'hema'}
args1 
=======
def my_decorator(func):
    def my_wrapper(*args,**kwargs):
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
       # print('Keyword arguments:', kwargs["child1"])
        #func(*args) or
        # func(*args, **kwargs) 
        func()
    return my_wrapper

#@my_decorator
#def function_without_arguments(text1,text2): 
#    print(text2 + " and " + text2) #viswa and Vimala

@my_decorator
def function_without_arguments(*args, **kwargs):  
    print("args1 ") 
    
function_without_arguments() # call arg1
function_without_arguments("viswa","vimala", child1="hema") # call arg1 
# function_without_arguments("viswa","vimala", child1:"hema") error
--------
Positional arguments: ()
Keyword arguments: {}
args1 
Positional arguments: ('viswa', 'vimala')
Keyword arguments: {'child1': 'hema'}
args1 
========================
Passing printing the variable aruguments
def my_function(*args): # statr argument , stored in tuple 
    for arg in args:
        print(arg)

my_function(1, 2, 3, 4)

def my_function(**kwargs): #double star kwargs
    for key, value in kwargs.items():
        print(key, value)

my_function(name="Alice", age=30, city="New York")

=================================
print("viswa {1}".format(110,231)) #viswa 231
array = range(5) #[0,1,2,3,4] //list
=========================
# add 2 number using direct  function call
def addTwoNumbers(a, b):
    c=a+b
    return c

c=addTwoNumber(4, 5)
 
print("Addition of two numbers=", c)
-------------------
Addition of two numbers=9

# add 2 number using decorator function
def decorateFun(func): 
    def sumOfSquare(x, y): 
        return func(x, y) 
    return sumOfSquare 

@decorateFun
def addTwoNumbers(a, b): 
    c = a+b 
    return c 

c = addTwoNumbers 
print("Addition of two numbers=", c(4,5))
-------------------
Addition of two numbers=9
===============================================
# add 2 number using decorator function
def decorateFun(func): 
    def sumOfSquare(x, y): 
        return func(x, y) 
    return sumOfSquare 

def addTwoNumbers(a, b): 
    c = a+b 
    return c 

obj=decorateFun(addTwoNumbers)  #
c=obj(4,5) 
print("Addition of square of two numbers=", c)

obj=decorateFun(addTwoNumbers)(4,5)  
print("Addition of square of two numbers=", obj)
-------------------------------------
Addition of square of two numbers= 9
Addition of square of two numbers= 9
===============================================
When to Use Python Decorators?
Suppose you are working on a project. You are asked to make the changes in a certain complex function.

If you are making changes in already tested and robust functions, you can not deny the possibility of
 breaking functionality.

A better way is to use Python decorators.

You don’t need to make changes in the already tested function.
You don’t need to make any changes to the function call. This will be very useful if there are 
multiple function calls in your project source code.
You can also pass the arguments to the decorators. You can modify these arguments inside the 
decorators before passing them to the original function.
=================================================
if a > 10:
    print("a is greater than a")
else:
    print("a is smaller") 
    
 # a is not defined
=================================================
a = "viswa1"
b = "viswa"

if (b > a):
  print("b is greater than a")
else:
   print("a is greater than b")
-----
a is greater than b
=================================================
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass
------------
 output:
 no output
 ==================================================
a=12
if a > 10:print("a is greater than a") // space after : is not must
else:print("a is smaller")
===>
a=12
if a > 10:
   print("a is greater than a")
else:
   print("a is smaller")
 ====================================================
a = 200
b = 33
c = 500
if a > b and c > a: # and or == equalto != not equalto
  print("Both conditions are True")

-----------------------------------------------------
#no : here 
a = 20
b = 3

print("A") if a > b else print("B")
this is same as 
if (a>b) :
  print("A")
else:
  print("B")

==================================================
#no : here 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #!= (not equal to) == (equalto)
output:
=
#elif (a >b): ==> else if statement in python
==================================
if 5 > 2:
   print("Five is greater than two!")
==> 
if 5 > 2: print("Five is greater than two!")
=================================

if 5 > 2:
  print("Yes")
else:
  print("No")
 ===>
  
print("Yes") if 5 > 2 else print("No")
=====================================
#and and or operator?

There is no && and || operator in python: 

python has if a==5 and b>0: or or
=====================================
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
print("viswa")

1
2
3
viswa
=============================
i = 1
while i < 10:
  if i == 3:
    i += 2
    continue
  print(i)
  i += 1
  
print("viswa")

1
2
5
6
7
8
9
viswa
======================
print("Hello", "World!") Hello World
print("Hello , World!")  Hello, World
====================================
#get the humber for the user and print whether it is positive or negative?
Nested if statement:
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print(num,"Zero")
    else:
        print(num,"Positive number")
else:
    print(num,"Negative number")
 
 ---------------------------
 Enter a number: -32.123445644
-32.123445644 Negative number
 
Enter a number: 34.0
34.0 Positive number 
=======================
#while for else continue and vreak
i = 1
while i < 10:
  if i == 3:
    i += 2
    continue
  elif (i==9):
  	break
  print(i)
  i += 1
else:
  print("viswa1")
  
  
print("viswa")
------
1
2
5
6
7
8
viswa
====================
#if else elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
==========================

i = 1
while i < 10:
  if i == 3:
    i += 2
    continue
  print(i)
  i += 1 # or i=i+1
else:
  print("viswa1")
  
  
print("viswa")
-----------------
1
2
5
6
7
8
9
viswa1
viswa
=============================
for x in "banana":
  print(x)
b
a
n
a
n
a
===============================
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
//////////
apple
banana
==================================
for x in range(6): # 0 to 5 not including 6
  print(x)
print(x)
0
1
2
3
4
5
5
==================================
for x in range(2, 6):
  print(x) # 2 to 5
 
 ==================================
 for x in range(2, 15, 3):
  print(x) # 2 to 14 increment by 3, 2 5 8 11 14
  
==================================
for x in range(6): # loop through 6 times
  print(x)
else:
  print("Finally finished!")
  0 1 2 3 4 5 Finally finished
=================================
for x in [0, 1, 2]:
  print (x)
  
 ==0 1 2
 ===============================
 for x in [0, 1, 2]:
  pass #empty for loop 
  ====================
#{} => needs.format()
#%s =>%()
#add the dict one by one element 
 # Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
    if (i == "geeks"):
    	i = "Viswa" #here we are not changing the l, we are changing only i

for i in l:
    print(i) # no change in l content
    
print (l[1]) # for

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
      
# Iterating over a String
print("\nString Iteration")   
s = "Geeks"
for i in s :
    print(i)
      
# Iterating over dictionary
print("\nDictionary Iteration")  
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i])) or print(i, d[i])
     
#Iterating over a set
print("\nSet Iteration")
set1 = {1,2,3,4,5,6}
for i in set1:
    print(i)

map1={"xyz":"viswa","abc":"hi"}
print(map1["xyz"]) // viswa

map1={1:"viswa",2:"hi"}
print(map1[2]) //hi

===
ist Iteration
geeks
for
geeks
geeks
for
geeks
for

Tuple Iteration
geeks
for
geeks

String Iteration
G
e
e
k
s

Dictionary Iteration
xyz  123
abc  345

Set Iteration
1
2
3
4
5
6
viswa
hi
========================================
#without for for loop how to iterate over the lements of the list?
#While True:

fruits = ["apple", "orange", "kiwi"]
 
# Creating an iterator object
# from that iterable i.e fruits
iter_obj = iter(fruits)
 
# Infinite while loop
while True:
  try:
    # getting the next item
    fruit = next(iter_obj)
    print(fruit)
  except StopIteration:
 
    # if StopIteration is raised,
    # break from loop
    break
  
apple
orange
kiwi  
 ==============
 
 # Creating a Dictionary
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
  
# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
print(Dict[1])
print(Dict[1][3])
-----------------------------
# disctionary one key and one value#dic one key and multiple values
Dictionary with the use of Integer Keys: 
{1: 'Geeks', 2: 'For', 3: 'Geeks'}

Dictionary with the use of Mixed Keys: 
{'Name': 'Geeks', 1: [1, 2, 3, 4]}
[1, 2, 3, 4]
4
===========================
 # Declaring a list
L = [1, "a" , "string" , 1+2]
print L
#Adding an element in the list
L.append(6)    
print L
#Deleting last element from a list
L.pop() # if not index is passed then the last element will be removed.
print L
#Displaying Second element of the list
print L[1]
-------------------
[1, 'a', 'string', 3]
[1, 'a', 'string', 3, 6]
[1, 'a', 'string', 3]
a
=======================================
# list and tuple can contain different data types:
tup = (1, "a", "string", 1+2)

=========================================
#index , pop and append is there for array and list:
#print the total element in the list
nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
 
pos = nameList.index("Pratik") 
print(pos)
print(len(nameList))
1
4

pos = nameList.index("Pratik1")  # will not run since there is Pratik1 is not in the list and the next line will not be executed.
print(len(nameList))
==============================================
#print emumerate range
for x in enumerate(range(2)): 
  print(x)
-------
(0,0)
(1,1)
===========================================
#create dict from the enumerate(range)
D = dict() 
for x in enumerate(range(2)): 
    D[x[0]] = x[1] 
    D[x[1]+7] = x[0] 
print(D)
-------
{0: 0, 7: 0, 1: 1, 8: 1}
==============================================
#create the dictionary by using for loop:

a = {i: i * i for i in range(6)} 
print (a) 
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
============================================
#create the set by using for loop:
a = { i * i for i in range(6)} 
print (a)
=====
{0, 1, 4, 9, 16, 25}
=========================================
# array slicing in different ways and assigning to another variable?
# array index?
# aaray pop , remove and edit the content based on the index?
array(data_type, value_list)

# Python program to demonstrate
# slicing of elements in a Array

# importing array module
import array as arr

# creating a list
l = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

a = arr.array('i', l) #i for int, f float , d for double, I unsigned int
print("Initial Array: ")
for i in (a):
	print(i, end =" ")

# Print elements of a range
# using Slice operation
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array) #array('i', [14, 15, 16, 17, 18])

# Print elements from a
# pre-defined point to end
Sliced_array = a[5:]
print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_array) #array('i', [16, 17, 18, 19, 20])

# Printing elements from
# beginning till end
Sliced_array = a # or Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array) #array('i', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
Sliced_array.append(20) # add 20 in the last
print(Sliced_array) #array('i', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20])
print(Sliced_array.index(20)) #9
print(Sliced_array.index(20)) #9
Sliced_array.insert(0,1)
Sliced_array.insert(0,2)
print(Sliced_array) #array('i', [2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20])
print(Sliced_array.pop(0)) #delete the index 0 element, 2
print(Sliced_array) #array('i', [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20])
Sliced_array.remove(20) #remove the first occurance of 20
print(Sliced_array) #array('i', [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
Sliced_array[0] =101
print(Sliced_array) #array('i', [101, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
=========================================
#what are the different rray types possible?
#what is the difference between array insert and append?
#array loop from -3 to 5?
# add the dilimiter in the print?

# importing "array" for array creations
import array as arr
 
# array with int type
a = arr.array('i', [1, 2, 3])
 
 
print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
 
# inserting array using
# insert() function
a.insert(1, 4)
 
print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()
 
# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
 
print ("Array before insertion : ", end =" ")
for i in range (0, 3): # 0 to 2 
    print (b[i], end =" ")
print()
#for i in range(-3,5): -3 to 4 loops
# adding an element using append()
b.append(4.4)

i int, f float, d double, l long, q long long
 
print ("Array after insertion : ", end =" ")
for i in (b):
    print (i, end =" ")
print()
=========================
Array before insertion : 1 2 3 
Array after insertion :  1 4 2 3 
Array before insertion : 2.5 3.2 3.3 
Array after insertion :  2.5 3.2 3.3 4.4 
========================================
# Python program to demonstrate
# Adding Elements to a Array
# declaring the array# printing all the elements of the array in different ways
#inserting the element into the array?
 
# importing "array" for array creations
import array as arr
 
# array with int type
a = arr.array('i', [1, 2, 3])
 
 
print ("Array before insertion : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
 
# inserting array using
# insert() function
a.insert(1, 4)
 
print ("Array after insertion : ", end =" ")
for i in (a):
    print (i, end =" ")
print()
----------------------
Array before insertion :  1 2 3 
Array after insertion :  1 4 2 3 
======================================
#convert the number to string, int and float?

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x , y, z,) 3 3 3.0
===================================
#get the type of the variable?

x=5 # space  x = 5 is not must
y = "John"
print(type(x))
print(type(y))

<class,int>
<class, str>
==================================
a = 4
A = "Sally"
#A will not overwrite a
Remember that variable names are case-sensitive

#ileegeal variable names
2myvar = "John"
my-var = "John"
my var = "John"

=====================
many values to multiple variable
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

Orange
Banana
Cherry
======================
# one to multiple variable
x = y = z = "Orange"
=======================
#unpacking the content from list?

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
--------
apple
banana
cherry
===============================
# printing all the vraiable string content in one line
x = "Python "
y = "is "
z = "awesome"
print(x + y + z) # python is awessome

x = "Python" #no space
y = "is"
z = "awesome"
print(x,y,z) #python is awessome
======================
# you cannot the add the number and string directly?

x = 5
y = "John"
print(x + y)
we cannot add int and string

x = 5
y = "John"
print(str(x)+y) 5John
print(x,y) 5 John
==========================
#global variable can be accessed by all function
#if the global and the local vraible name are the same the local vriable is the preference and both the variables are different.
x = "awesome"

def myfunc():
  x = "fantastic" # local variable
  print("Python is " + x)

myfunc()

print("Python is " + x) # global variable
-----------------------------
Python is fantastic
Python is awesome
==========================================
#how to modify the content of the global variable? 
x = "awesome"

def myfunc():
  x = "fantastic"

myfunc()

print("Python is " + x) # python is awessome

def myfunc1():
  global x
  x = "fantastic"

myfunc1()
print("Python is " + x) # python is fantastic
============================================
#accessing the global variable inside the function 
x = "awesome"

def myfunc():
  print("Python is " + x) # python is awessome

myfunc()
============================================
print(5+10) #15
================================
"""
Points to be noted:
python packages consists of module , module has class and function
python has vast libraries and frameworh

Error:
StopIterator
ValueError
IndexError

pop, pop(index), remove(key), del key or index depend on the data type
dict: popiems, uodate, get clear
.index: return the index
insert and append

dict.keys()
dict_keys([])

dict.values()
dict_values([])

relation operator: and or """
