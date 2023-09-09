"""
	Lesson 4: Sample program for the python.
	Source Code Location: https://github.com/ViswanathanRamasamy/PythonSamplePgm.git
	Author Name: Viswanathan Ramasamy
	Email id: rviswawt@gmail.com
"""
===================================================
# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.
 
print("I love {'Geeks'} for \"{'Geeks'}!\"")
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
print("I love {'Geeks'} for \"Geeks!\"")

# using format() method and referring
# a position of the object
print(f"{'Geeks'} and {'Portal'}")
-========
I love {'Geeks'} for "{'Geeks'}!"
I love Geeks for "Geeks!"
I love {'Geeks'} for "Geeks!"
Geeks and Portal

==================================
if __name__ == '__main__':
    array = range(1,5)

print(array)

=====
#output
range(1, 5)

=============
 Examples of Arithmetic Operator
a = 9
b = 4
  
# Addition of numbers
add = a + b
  
# Subtraction of numbers
sub = a - b
  
# Multiplication of number
mul = a * b
  
# Division(float) of number
div1 = a / b
  
# Division(floor) of number
div2 = a // b
  
# Modulo of both number
mod = a % b
  
# Power
p = a ** b
  
# print results
print(add)
print(sub)
print(mul)
print(div1) //2.25
print(div2) //2 
print(mod)  // 1
print(p) // power

========================
x = 24
y = 20
list = [10, 20, 30, 40, 50]
  
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
  
if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
	
####
x is NOT present in given list
y is present in given list
======================
[on_true] if [expression] else [on_false] 

# Program to demonstrate conditional operator
a, b = 10, 20
 
# Copy value of a in min if a < b else copy b
min = a if a < b else b
 
print(min)
======
10
---------------------------	

# Python program to demonstrate ternary operator
a, b = 10, 20
 
# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
print( (b, a) [a < b] )
 
# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# else if [a<b] is false then value of False key will print
print({True: a, False: b} [a < b])
print({True: b, False: a} [a < b])
======
10
10
20
=======================================

# Program to demonstrate conditional operator
a, b = 10, 20
 
# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b
 
print(min) #10
a= 0
min = a < b and a or b
 
print(min) #20

a= 100
min = a < b and a or b #20
 
print(min)

min = a < b and b or a #100
 
print(min)
=========================
# Python program to show use of
# + operator for different purposes.
print(1 + 2)
  
# concatenate two strings
print("Geeks"+"For") 
  
# Product two numbers
print(3 * 4)
  
# Repeat the String
print("Geeks"*4)

Output
3
GeeksFor
12
GeeksGeeksGeeksGeeks
===============================
any if one of the element is true
all if all of the element is true

# Since all are false, false is returned
print (any([False, False, False, False])) # False
  
# Here the method will short-circuit at the
# second item (True) and will return True.
print (any([False, True, False, False])) # True
  
# Here the method will short-circuit at the
# first (True) and will return True.
print (any([True, False, False, False])) #True
=======================================
To check whether any number is divisible by 5


# This code explains how can we 
# use 'any' function on list 
list1 = []
list2 = []
  
# Index ranges from 1 to 10 to multiply
for i in range(1,11):
    list1.append(4*i) 
  
# Index to access the list2 is from 0 to 9
for i in range(0,10):
    list2.append(list1[i]%5==0)
  
print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))
====================================
#Illustration of 'all' function in python 3
#all the numbers in the list are odd  
# Take two lists 
list1=[]
list2=[]
  
# All numbers in list1 are in form: 4*i-3
for i  in range(1,21):
    list1.append(4*i-3)
  
# list2 stores info of odd numbers in list1
for i in range(0,20):
    list2.append(list1[i]%2==1)
  
print('See whether all numbers in list1 are odd =>')
print(all(list2))
====================================
list1 = []

print(all(list1)) #True
print(any(list1)) # False
===================================
 #include <cstdlib>
 if we are going to use the system command in the cpp
 
===================
The __init__() function is called automatically every time the class is being used to create a new object.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
it can be changed to any of your convenient name.

class MyClass:
	x =5
	#init function will be always called when the class is initatiated
	def __init__(self, name, age): 
		self.name = name # name and age are the property of the object
		self.age = age

	def MyFunction(self): #name self can be changed based on your convenient naming.
		print(self.name, self.age) 

p1 = MyClass("Viswa",39);
p2 = MyClass("Viswa1",139);
p1.MyFunction()
del p1.age #delete the age property of the object p1
print(p1.name)
#print(p1.age)
print(p1.x) #5
p1.x=100
print(p1.x) #100
del p1.x
print(p1.x) #5
p2.MyFunction()
print(p2.x)
print(p2.name)
print(p2.age)
del p2 #delete the object
#print(p2.name) p2 is not defined

===================
Viswa 39
Viswa
5
100
Viswa1 139
5
Viswa1
139
==========================
class definitions cannot be empty, but if you for some reason have a class definition with no content, 
put in the pass statement to avoid getting an error.
class Person:
  pass

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
     # adding two objects 
    def __add__(self, other):
        return (self.a + other.a, self.b + other.b)
        
    def MyFunction(self):
    	return self.a , self.b
  
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob1 + Ob2)
print(Ob2)
print(Ob3)
#print(Ob3.MyFunction()) AttributeError: 'tuple' object has no attribute
print(Ob2.MyFunction())
print(type(Ob3))
----
(3, 5)
<__main__.complex object at 0x147d749b5fd0>
(3, 5)
(2, 3)
tuple
-------
class MyClass:
	x =5
	#init function will be always called when the class is initatiated
	def __init__(self, name, age): 
		self.name = name # name and age are the property of the object
		self.age = age

	def MyFunction(self): #name self can be changed based on your convenient naming.
		print(self.name, self.age) 
        
	def MyFunction1(self): #name self can be changed based on your convenient naming.
		return self.name, self.age

p1 = MyClass("Viswa",39);
p2 = MyClass("Viswa1",139);
p1.MyFunction()
del p1.age #delete the age property of the object p1
print(p1.name)
#print(p1.age)
print(p1.x)
p1.x=100
print(p1.x)
p2.MyFunction()
print(p2.x)
print(p2.name)
print(p2.age)
print(p2)
print(p2.MyFunction1())
del p2 #delete the object
#print(p2.name) p2 is not defined
===================
Viswa 39
Viswa
5
100
Viswa1 139
5
Viswa1
139
<__main__.MyClass object at 0x14cef4a93dc0>
('Viswa1', 139)
================================
some of the operator that can be overloaded are
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
.....
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)
========================
# Repeat the String
print("Geeks"*4)
GeeksGeeksGeeksGeeks
========================
Python has predefined functions for many mathematical, logical, relational, bitwise etc operations under the module “operator”.
# importing operator module 
import operator
  
# Initializing variables
a = 4
  
b = 3
  
# using add() to add two numbers
print ("The addition of numbers is :",end="");
print (operator.add(a, b))
  
# using sub() to subtract two numbers
print ("The difference of numbers is :",end="");
print (operator.sub(a, b))
  
# using mul() to multiply two numbers
print ("The product of numbers is :",end="");
print (operator.mul(a, b))
Output:

The addition of numbers is:7
The difference of numbers is :1
The product of numbers is:12
======================================
x = ["apple", "banana", "cherry"]	list
x = ("apple", "banana", "cherry")	tuple
x = range(6)						range
x = {"name" : "John", "age" : 36}	dict
x = {"apple", "banana", "cherry"}	set
	======================
z = 1+1j   # complex
print(z)
x = complex (12)
print(x)
print(type(z))
-------
(1+1j)
(12+0j)
<class 'complex'>
======
import random

print(random.randrange(1, 10)) # print the one random number between 1 to 10
===============
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
z = int("100",2) #4 binary
z = int("ff",16) #255 hexa decimal
=======================
i = 1
while True:
    if i % 3 == 0:
        break
    print(i)
    i + = 1 #syntax error space 
===========
mylist = ['geeks', 'forgeeks']
for i in mylist:
    i.upper()
    print(i)
    i=i.upper()
    print(i)
print(mylist)
===========
geeks
GEEKS
forgeeks
FORGEEKS
['geeks', 'forgeeks']
=============
mylist = ['geeks', 'forgeeks']
for i in mylist:
    mylist.append(i.upper())
print(mylist)
=====
no output, the loop will not terminate
=========================================
f the argument passed to the bool function does not amount to zero then the Boolean function returns true else it always returns false. 
In the above code, in first line ‘False’ is passed to the function which is not amount to 0.
 Therefore output is true. In the second line, an empty list is passed to the function bool. Hence the output is false.

True=False
print(bool("False") # if something is passed to bool , then it will print True
print(bool()) #if nothing is passed it will print False
print(bool("0")) #True
print(bool(0)) #False
print(bool(False)) #False
=======================
print(['love', 'python'][bool('gfg')]) #python

mylist =[0, 5, 2, 0, 'gfg', '', []]
print(list(filter(bool, mylist))) 
[5,2,'gfg']
======
mylist =[0, 5, 2, 0, 'gfg', '', ["hi"]]
print(list(filter(bool, mylist)))
====
[5, 2, 'gfg', ['hi']]

=============================
L = [2e-04, 'a', False, 87]
T = (6.22, 'boy', True, 554)
for i in range(len(L)):
    if L[i]:
        L[i] = L[i] + T[i]
    else:
        pass
        #T[i] = L[i] + T[i] # result in type error when we tryto change
        break
        
print(L)
2e-04=>0.0002
False+True = 1 not true
we cannot change the tuple, it will result in type error if we try to change the tuple
[6.222e-04, ‘aboy’, False, 641] 

===========================

T = (2e-04, True, False, 8, 1.001, True)
val = 0
for x in T:
    val += int(x) 
print(val)
===11
int(12.12) #12
int(False) #0
print(int('A')) # we cannot convert the character to the interger number
print(int(ord('A'))) #65
print(chr(int(ord('A'))+1)) #B

space ascii value is 32
* asccii value is 35
ord will covert the ascii to number
=======================
str1 = '{2}, {1} and {0}'.format('a', 'b', 'c')
str2 = '{0}{1}{0}'.format('abra', 'cad')
print(str1, str2)
#c, b and a abracadabra
==================
a = 2
b = '3.77'
c = -8
str1 = '{0:.4f} {0:3d} {2} {1}'.format(a, b, c)
print(str1)
========
2.0000 2 -8 3.77 
--------
line = "I'll come by then."
eline = ""
for i in line:
    eline += chr(ord(i)+3) 
print(eline) 
====================
line =  "What will have so will"
L = line.split()
print(L)
for i in L:
    print(i, end=' ')

print()
L = line.split('a') # diferrent element in the single list
print(L)
for i in L:
    print(i, end=' ')
=====================
['What', 'will', 'have', 'so', 'will']
What will have so will 
['Wh', 't will h', 've so will']
Wh t will h ve so will 
==============================
dict1 = {} #deirectory
dict[(1,2,4)] = 8 #using the tuple inside the directory
dict[(4,2,1)] = 10
dict[(1,2)] = 12
_sum = 0
for k in dict:
    _sum += dict[k]
print(len(dict) + _sum)
==============
33 
===================================
tuple = {}
tuple[(1,2,4)] = 8
tuple[(4,2,1)] = 10
tuple[(1,2)] = 12
_sum = 0
for k in tuple:
    _sum += k[0]
print(len(tuple) + _sum) #6+3 ie 1 4 1 3
===========================
tuple=("Check")*3
print(tuple) #checkcheckcheck
===============================
tuple = (1, 2, 3)
print(2 * tuple) # (1, 2, 3,1, 2, 3) 
==================
tuple1 = (1, 2, 4, 3)
tuple2 = (1, 2, 3, 4)
print(tuple1 < tuple2) #false each individual element is compared
=====================
class Acc:
    def __init__(self, id):
        self.id = id
        id = 555 # changing the local varibel and not the property value
 
acc = Acc(111)
print (acc.id) #here 111 
======================================
counter = {} #dict
 
def addToCounter(country):
    if country in  counter:
        counter[country] += 1
    else:
        counter[country] = 1
 
addToCounter('China')
addToCounter('Japan')
addToCounter('china')
addToCounter('china')
print(counter)
print (len(counter))
=====
{'China': 1, 'Japan': 1, 'china': 2} #case sensitive
3
============================
value = (1,2,3,1,2,3) #tuple
print(value)
value = {1,2,3,1,2,3} # set set will not have the dublicate element. the order of the element stored might change
print(value)
set1 = set()
String = 'GeeksForGeeks'
set1 = set(String)
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
========
(1, 2, 3, 1, 2, 3)
{1, 2, 3}
==================================
value = {"geeksforgeeks"} # set set will not have the dublicate element. the order of the element stored might change
print(value)
value = {"g","e","eksforgeeks"} # set set will not have the dublicate element. the order of the element stored might change
print(value)
=====
{'geeksforgeeks'}
{'g', 'eksforgeeks', 'e'}
====================
list = [1, 2, 3, None, (1, 2, 3, 4, 5), ['Geeks', 'for', 'Geeks']]
print len(list) #6
============================
list = ['python', 'l_earning', '@', 'Geeks', 'for', 'Geeks']
 
print list[::]         
print list[0:6:2]      
print list[ :6: ]      
print list[ :6:2]     
print list[ ::3]      
print list[ ::-2]    
# list[X:Y:Z] //x initial index y final index z step size
========
['python', 'l_earning', '@', 'Geeks', 'for', 'Geeks']
['python', '@', 'for']
['python', 'l_earning', '@', 'Geeks', 'for', 'Geeks']
['python', '@', 'for']
['python', 'Geeks']
['Geeks', 'Geeks', 'l_earning']
=============================================


v="viswanathan"
print(v[-1])
v=["geeks1","geeks2","geeks3","geeks4"]
print(v[-1])
print(v[::-2])
print(v[2::-2])
======
n
geeks4
['geeks4', 'geeks2']
['geeks3', 'geeks1'] 
=======================================

d1 = [10, 20, 30, 40, 50]
d2 = [1, 2, 3, 4, 5]
d1 = (d1 + d2) #append the 2 list [100, 20, 30, 40, 50, 1, 2, 3, 4, 5]
d1[0]=100
print (d1)
#d1 = (d1 - d2) - sign will not work
=============================
list = ['a', 'b', 'c']*-1 #- sign will not work
print (list)
======================
list = ['a', 'b', 'c']
print(list[10:])
#[]

"""
Note:
a,b = 10, 20 a will be assigend woth 10 and b with 20
a =range(10)

list => all, any
list(fileter(bool,List1)))
list can have None

tuple[{}], 
tuple1 < tuple2
set("geeks")
set will not allow the duplicate and order of the element in the set will be different while prirninting

import random
t=random.randgen(1,10)

obj3=obj1+obj2; def __add__(self,others)

import operator
operator.add(1,2)

empty class
class name
  pass
  

'a'
l=int(ord('a'))

"""

