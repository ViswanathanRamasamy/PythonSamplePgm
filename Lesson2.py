"""
	Lesson 2: Sample program for the python.
	Source Code Location: https://github.com/ViswanathanRamasamy/RockYourInterview-CPP/
	Author Name: Viswanathan Ramasamy
	Email id: rviswawt@gmail.com
"""
"""
python is used in google, facebook and spotify
in python there is no intermediate executable file or binary file. in python compiler convert the source file into bytecode and then interpretor 
run on it.
python is general purpose programming langauge  and cabaple of scripting as well.
python package has python modules. python module consists of class and function.python object takes heap memory and release by garbage collector
when it is not in use. python can be used as object oridented programming as well structural oridented programming.

some datastructures present in python:
list => mutable ie can be modified
tuple => immutable , cannot be modified
directory => map===> {"xyz":"viswa","xyz1":"viswa2"}
set => {"viswa","hi"}

Function can be passed as an argument to another function,
function can be return from the function
function can be assigned to a variable

Python Decorator:
==================
python decorator are used to change the behaviour of the class or the function. It is used to wrap the function inorder to increase the functionality.
function are objects in c"""

def greet(name):
    """This is a simple function that greets the user."""
    print(f"Hello, {name}!")
    
name can be string or numbers

print(f"Hello, {'hello'}!")
print(f"Hello, {"hello"}!")
========================================    
syntax for the decorator:
==========================
@decorator(params)
def func_name():
    ''' Function implementation'''
=========================
def func_name():
    ''' Function implementation''' #doc string

func_name = (decorator(params))(func_name)
=============================
# first method that return second method
def A(number):
	print("Inside the method A.", number)

returned_function = A(12) #return value 

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

# call second method by first method return value which is none
returned_function
output
Inside the method A.
==============================================
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
    def wrapper(): #defulut no agrument
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
=============================
# Python code to illustrate
# Decorators with parameters in Python
 
def decorator_fun(func):
  print("Inside decorator")
 
  def inner(*args, **kwargs):
    print("Inside inner function")
    print("Decorated the function")
     
    func()
     
  return inner
 
 
def func_to():
    print("Inside actual function")
 
# another way of using decorators
decorator_fun(func_to)()
0r
func_to()
///
output:
-------
Inside inner function
Decorated the function
Inside actual function
===================================
# Python code to illustrate
# Decorators with parameters in Python

def decorator_func(x, y):

	def Inner(func):

		def wrapper(*args, **kwargs):
			print("I like Geeksforgeeks")
			print("Summation of values - {}".format(x+y) )

			func(*args, **kwargs) # we pass the 2 argument but accept only the first argument
			
		return wrapper
	return Inner


# Not using decorator
def my_fun(*args): 
	for ele in args:
		print(ele)

# another way of using decorators
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')
or
# another way of using decorators
obj=decorator_func(12, 15)(my_fun)
obj('Geeks', 'for', 'Geeks')
///output
viswanathan23
abc
cat
lion
=======================================================
#overridding the decorator values?

def decorator(x,y):
    def inner(funct):
        def mywrapper(*args,**kwargs):
            print("viswanathan{}".format(x+y))
            funct(*args)
        return mywrapper
    return inner

@decorator(1,2)
def myfunction(*args):
    for e in args:
        print(e)

(decorator(11,12))(myfunction)('abc','cat','lion')

viswanathan23
viswanathan3
abc
cat
lion
=================================================
#type check for the each argument 
#if for the type check of the all the lements?

def decorator(mtype, message1, message2):
    print(message1)
    def myinner(function):
        def mywrapper(*args,**kwargs):
            print(message2)
            if ([(type(e) == mtype) and print(e) for e in args ]): #in any of the input is str then the function will be called
            # here it check all the args of type, if it matches then it will call the function
                return function(*args,**kwargs)
            return ("ivvalid")
        return mywrapper
    return myinner
    

@decorator(str,"hi", "viswa")
def string_to_json(*args):
    str1 = "" # str1= ''
    for e in args:
        str1 += str(e)
    return str1
    
print(string_to_json(1, "Good", "morning"))

output
hi
viswa
Good
morning
1Goodmorning
==========================================================
#passing the dict to the decorator as the parameter?
#executing without the actual call ie just from the decorator assignment:
def decorator(*args, **kwargs):
	print("Inside decorator")
	
	def inner(func):
		
		# code functionality here
		print("Inside inner function", args)
		print("I like", kwargs['like']) #kwargs["like"]
		
		func(*args)
		
	# returning inner function
	return inner

@decorator(like = "geeksforgeeks")
def my_func():
	print("Inside actual function")

Inside decorator
Inside inner function ()
I like geeksforgeeks
Inside actual function
==============================================
