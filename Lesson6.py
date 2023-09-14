"""
	Lesson 6: Sample program for the python.
	Source Code Location: https://github.com/ViswanathanRamasamy/PythonSamplePgm.git
	Author Name: Viswanathan Ramasamy
	Email id: rviswawt@gmail.com
"""
===================================================
======================================

try:
 1/0
except Exception as e: #class name Exception , e is instance of Exception

    print(type(e)) # <class 'ZeroDivisionError'>
==============================================
try:
 1/0
except Exception : #it is not necessary to instantiate
    print("exception occures") 
    
=======================================
try:
 1/0

except TypeError:
    print("type error")
except ZeroDivisionError:
    print("zero division error")
except Exception as e: #class name Exception , e is instance of Exception. 
#This should be always after the last of all the exception
    print("caughtall error")
===============
zero division error
=====================
try:
 1/0
 
except Exception as e: #class name Exception , e is instance of Exception. 
#This should be always after the last of all the exception
    print("caughtall error")
except TypeError:
    print("type error")
except ZeroDivisionError:
    print("zero division error")

===================
caughtall error
====================
=================
#same decorador function to handle all error in the different function
#ie centralized error handling mechanism
def decorador(func):
    def mywrapper():
        try:
            func()
        except ZeroDivisionError:
            print("zero division error")
        else:
            print("dsfd") # will print when ther is no exception
        finally:
            print("finall")
    return mywrapper
    
@decorador
def causeError():
   1/0
   
causeError() 
=============================
zero division error
finall
===========================
#raise my own exception
#same decorador function to handle all error in the different function
#ie centralized error handling mechanism
def decorador(func):
    def mywrapper(*args):
        try:
            func(*args)
        except ZeroDivisionError:
            print("zero division error")
        except Exception:
            print("some sort error")
        finally:
            print("finally")
    return mywrapper
    
@decorador
def causeError(n):
    if (n == 0):
      raise Exception()
    print(n)
   
causeError(0) 
print("viswa")
============================================
some sort error
finall
viswa
=========================
#same decorador function to handle all error in the different function
#ie centralized error handling mechanism
def decorador(func):
    def mywrapper(*args):
        try:
            func(*args)
        except ZeroDivisionError:
            print("zero division error")
        except Exception:
            print("some sort error")
        finally:
            print("finally")
    return mywrapper
    
@decorador
def causeError(n):
    if (n == 0):
      raise Exception()
    print(n)
   
causeError(1) 
print("viswa")
=======================================
1
finally
viswa
=========================================
#handle the pass exception
class CustonException(Exception):
  pass
  
===========================
#custom exception
class HttpException(Exception):
    StatusCode = None
    message = None
    x =10
    def __init__(self):
        super().__init__(f"Error Code {self.StatusCode} {self.message}")
        #print (x) #we cannot access the instance method to directly access the class 
        #attribute. print (self.x) is allowed.

class ServerNotFound(HttpException):
    StatusCode = 500
    message = "Server Error " 

class NotFound(HttpException):
    StatusCode = 404
    message = "Resource not found"

def raiseServerError():
    raise ServerNotFound()

raiseServerError() #__main__.ServerNotFound: Error Code 500 Server Error
====================================================================
try:
    1/0 #this will divisionby zero exception or arithamatic exception. 
    #which ever comes first
except ArithmeticError:
    print('ArithmeticError') #arithamatic error
except Exception:
    print('Exception')
except DivisionByZeroError:
    print('DivisionByZero')
except ZeroDivisionError:
    print ("division by zero")
=================================
try:
    1/0 #this will divisionby zero exception or arithamatic exception. 
    #which ever comes first
except ZeroDivisionError:
    print ("division by zero") #division by zero
except ArithmeticError:
    print('ArithmeticError') 
except Exception:
    print('Exception')
except DivisionByZeroError:
    print('DivisionByZero')
=================================
try:
    1/0 #this will divisionby zero exception or arithamatic exception. 
    #which ever comes first
except DivisionByZeroError: #no such exception
    print('DivisionByZero')
except ZeroDivisionError:
    print ("division by zero") #division by zero
except ArithmeticError:
    print('ArithmeticError') 
except Exception:
    print('Exception')
====================================================
datetimepackage
===============
from datetime import datetime

print(datetime.now())
print(datetime.now().second)
while_time =datetime.now().second+2 # be carefull 59+2 will return 61 but the second cannot be greater than 60
while True:
    if (datetime.now().second >= while_time):
        break
    
    
print("End of the pgm")
============
2022-09-12 01:14:13.594976
13
End of the pgm
=========================================================
#get the time

import time

start = time.time()
time.sleep(1)
print(f"time difference {time.time()-start}") #1.001
====================================================
#sort the list
mylist=[100,29,3,-4,5]
print(sorted(mylist))
=========================
#array of function
list = [function1,function2,function3]
for x in list1:
  x("viswa")
  ==================================
  def function(varA):
  print("Hello World")
  return 7
 
print(function.__code__.co_varnames) #('varA',)
print(function.__code__.co_code)# b't\x00d\x01\x83\x01\x01\x00d\x02S\x00'

list1 = ['.','-',':']
text = "Viswan.athan.ramasamy-123:west"
#print(text.replace(list1," ").lower()) not allowed

text=text.lower()
for char in list1:
    text=text.replace(char," ")
print(text) #viswan athan ramasamy 123 west

print(([x for x in text.split() if (len(x)<7) ]))#['viswan', 'athan', '123', 'west'] join will join the list with keywords inbetween
print( "-hi-".join([x for x in text.split() if (len(x)<7) ])) #viswan-hi-athan-hi-123-hi-west

#print(([x for x in text.split() if (len(x)<7) ]).join("-hi-")) not allowed
=============================================
x =10
varA=10
varZ=20
def outer_function(varA,VarB):
    print(locals()) #{'VarB': 2, 'varA': 1}
    print(varZ) #20
    def inner_function(varC,VarB):
       print(locals()) #{'varC': 123, 'VarB': 122, 'varA': 1}
       print(varA) #1 
       print(varZ) #20
    inner_function(123,122)

outer_function(1,2)
#inner_function(1,2) #inner function cannot be called from outside
===============================
x =10
varA=10
varZ=20
def outer_function(varA,VarB):
    zx = 12
    print(locals()) #{'VarB': 2, 'varA': 1}
    print(varZ) #20
    def inner_function(varC,VarB):
       print(globals()) # will list all the x, varA, VarZ, file name, function name no zx
       print(locals()) #{'varC': 123, 'VarB': 122, 'varA': 1}
       print(varA) # 1
       print(varZ)  # 2
    inner_function(123,122) #no call to inner function no zx
    print(globals()) # will list all the x, varA, VarZ, file name, function name
    
outer_function(1,2)
=====================
#named parameter ie passing the default value
def perform_operation(*args):
    print(args) #postional argument (2,3,4,5)
        
(perform_operation(2,3,3,4,5)) 
#(perform_operation(2,3,3,4,5,operation="sum")) not allowed
def perform_operation1(*args,**kwargs):
    print(args) #positional argument (2,3,4,5)
    print(kwargs) #{'operation': 'sum'}
        
perform_operation1(2,3,3,4,5, operation="sum") #keyword argument
====================================
import math
def perform_operation(*args,operation="sum"):
    if operation=="sum":
        return sum(args)
    if operation=="multiply":
        return math.prod(args)
        
print(perform_operation(2,3,3,4,5, operation="sum")) #17
print(perform_operation(2,3,3,4,5, operation="multiply")) # 360
==========================
def perform_operation(a,b,operation="sum", message="default message"):
    print(locals()) # print only the local variable with value in the dict
    
perform_operation(1,2,"multiply") #{'a': 1, 'b': 2, 'operation': 'multiply', 'message': 'default message'}
==========================
print(globals()) => will print all the global variable available in the python and not only in your program
========
python check the local scope of the variable first and then the global variable.ie if the local and global variable has the same name in the function,
then the function will access the local vraible 
==============
dict1={
    'a':["apple", "pineapple"],
    'b':{"ball"},
    'c':"cat",
    'd':"dog"}
dict1['a'].append("viswa")
dict1['b'].add("banana")
dict1['d'] =[1,2,3,4]
if 'o' not in dict1: # will s_earch for o in key only and not in value
  dict1['o']=[]
  dict1['o'].append("OXford")
print(dict1)
=================================
{'a': ['apple', 'pineapple', 'viswa'], 'b': {'banana', 'ball'}, 'c': 'cat', 'd': [1, 2, 3, 4], 'o': ['OXford']}
===================
=================================================
print(list(range(101))[::-5])
[100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0]

single line if statement
#iternary operator: take one value evaluate true or false and return one value
n=3
print("pass" if (n%2) else n )
n=2
q= ("pass" if (n%2) else n)
print(q)
#list containment
print([("pass" if (n%2) else n) for n in range(1,10)])
===
pass
2
['pass', 2, 'pass', 4, 'pass', 6, 'pass', 8, 'pass']
=====================================
=============================================
import json
jsonstring='{ "a":"apple", "b":"ball", "c":"cat"}' # not ' at the begining and end.
#"" inside
#convert json string to python object
j=json.loads(jsonstring) #loads not loads
print(j)
=============
{'a': 'apple', 'b': 'ball', 'c': 'cat'}
===================
import json
from json import JSONDecodeError

try:
    jsonstring='{ "a":"apple", "b":"ball", "c":"cat",}' 
    #convert json string to python object
    j=json.loads(jsonstring) #loads not load
    print(j)
#exception error caught during the parsing.
#exception is different from syntax error.in the json string, if we replace the ' to " it
#is syntax error
except JSONDecodeError: # not like exception(JSONDecodeError)
    print("JSONDecodeError")
=====================================
#convert from the python object to json
import json
python_object = { "a" : "apple", "b":"ball"}
#or python_object = { "a" : "apple", "b":"ball",}

jsonstr= json.dumps(python_object)
print(jsonstr)
==========
{"a": "apple", "b": "ball"}
=====================
from json import JSONEncoder, JSONDecodeError, dumps # note Json is in capital

class Animal():
    def __init__(self,name):
        self.name=name

class AnimalEncoder(JSONEncoder):
    def default(self,o):
        if (type(o) == Animal):
            return (o.name)
        return super().default(o)
pythonobj={ "a":Animal("apple"), "b":Animal("ball"), "c":Animal("cat")}
    #convert json string to python object
j=dumps(pythonobj,cls=AnimalEncoder) #dump dont understand the python class
print(j)
======
{"a": "apple", "b": "ball", "c": "cat"}
=====================================
j= "viswa
print(type(j).__name__) # str
print(type(j)) <class ,str>
========================
Reading JSON from a File and Parsing:
import json

# Open a JSON file for reading
with open('data.json', 'r') as file:
    data = json.load(file)

# Access and print JSON data
print(data)

==============================
Writing JSON to a File:
import json

# Create a Python dictionary
data = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}

# Write the dictionary to a JSON file
with open('output.json', 'w') as file:
    json.dump(data, file)
=================
Working with Nested JSON:
import json

# JSON data with nested structure
data = {
    "name": "John",
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}

# Accessing nested data
street = data["address"]["street"]
print("Street:", street)

===================================
Handling JSON Arrays:
import json

# JSON array
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Accessing elements in the array
for person in data:
    print("Name:", person["name"], "Age:", person["age"])

==============================================
Converting JSON to Python Objects:
import json

# JSON-formatted string
json_string = '{"name": "David", "age": 28, "city": "Chicago"}'

# Convert JSON string to a Python dictionary
data = json.loads(json_string)

# Access and print data
print(data)

====================================
Parsing JSON with Nested Structures:
import json

# JSON data with nested structure
json_string = '{"person": {"name": "Bob", "age": 30}}'

# Parse JSON data
data = json.loads(json_string)

# Access nested values
print(data["person"]["name"])  # Output: Bob
print(data["person"]["age"])   # Output: 30
===============================
try:
    # Attempt to divide by zero, which will raise a ZeroDivisionError
    x = 10 / 0
except ZeroDivisionError as zd_error:
    # Handle ZeroDivisionError
    print(f"ZeroDivisionError: {zd_error}")
except ArithmeticError as arith_error:
    # Handle ArithmeticError
    print(f"ArithmeticError: {arith_error}")
except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {e}")
else:
    # This block is executed if no exception is raised
    result = x + 5
    print(f"Result: {result}")
finally:
    # This block is always executed, regardless of whether an exception occurred
    print("Execution complete")

# Code continues here...
ZeroDivisionError: division by zero
Execution complete
=========================================
try:
    # Attempt to open a file that doesn't exist
    file = open("nonexistent_file.txt", "r")
except FileNotFoundError as e:
    # Handle the FileNotFoundError exception
    print(f"An error occurred: {e}")
else:
    # This block is executed if no exception is raised
    content = file.read()
    file.close()
    print(f"File contents: {content}")
finally:
    # This block is always executed, regardless of whether an exception occurred
    print("Execution complete")

# Code continues here...
An error occurred: [Errno 2] No such file or directory: 'nonexistent_file.txt'
Execution complete
======================================
===================================================
File handling in python:
=========================
f = open("viswa.txt","w")
print(f)
f.write("line1 \n") #if there is no \n it will write all the content in one line
f.write("line2 \n")
f.close() # in python only after f close the content from the bbuffer will write 
#data into the filter
f = open("viswa.txt","a")
print(f)
f.write("line1 \n") #if there is no \n it will write all the content in one line
f.write("line2 \n")
f.close() # in python only after f close the content from the bbuffer will write 
#data into the filter
with open("viswa.txt","a") as f:
    f.write("line11 \n") #if there is no \n it will write all the content in one line
    f.write("line22 \n") # with statement will close the file after the block
    
print(f)
#f.write("line212 \n") file is already closed
=============================
<_io.TextIOWrapper name='viswa.txt' mode='w' encoding='UTF-8'>
<_io.TextIOWrapper name='viswa.txt' mode='a' encoding='UTF-8'>
<_io.TextIOWrapper name='viswa.txt' mode='a' encoding='UTF-8'>
---------------------
line1 
line2 
line1 
line2 
line11 
line22 

==================================
f.write("line1 \"\\n\" \n") ==> line1 \n
====================================
to open the file for reading

f = open("viswa.txt","r")
print(f.readline()) ==> read the first line
print(f.readline()) ==> read the second line
print(f.readlines()) ==> 3 line to last line

for line in f.readlines():
   print(line.strip()) // will remove the /n character from the line is present in the file and print it 
   
==================================================
with open('example.txt', 'r') as file:
    data1 = file.read(10)  # Read the first 10 characters
    data2 = file.read()    # Read the rest of the file

print(data1)
print(data2)
=====================
with open('example.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()

print(line1)  # Contents of the first line
print(line2)  # Contents of the second line
=================================
//readlines
//[() condition]