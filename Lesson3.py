"""
	Sample program for the python. Lesson 2.
	Source Code Location: https://github.com/ViswanathanRamasamy/PythonSamplePgm.git
	Author Name: Viswanathan Ramasamy
	Email id: rviswawt@gmail.com
"""
/////////
build in data types: list, tuple, set. array, dictorary
/////////
Enummeration

# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1) #or obj1 = enumerate(l1, 0) # index start from 0
obj2 = enumerate(s1,5) #index starts from 5
  
print ("Return type:", type(obj1)) # return the type 
print (list(enumerate(l1)))
  
# changing start index to 2 from 0
print (enumerate(s1, 2)) #print the address of the enumarate object
print (list(enumerate(s1, 2)))

for f,e in obj2:
  print(f,e)
  
for f,e in obj1:
  print(f,e)
  
=====
Return type: <class 'enumerate'>
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
<enumerate object at 0x1541215b15c0>
[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]
5 g
6 e
7 e
8 k
0 eat
1 sleep
2 repeat
==================
#python variables are case sensitive
L=[1,2,3,4,5]
print(*L) *L will unpack the elements of the list L into separate arguments for the print function.
1 2 3 4 5

print("hi") print("good") #  2 print line cannot be in the same line
print("viswa\n nathan")
viswa
nathan

=================
#count down program:
#T is in caps for True

import time
 
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush = True)
        time.sleep(1)
    else:
        print('Start')

3 >>> 2 >>> 1 >>> start.
if there is no flush (default flush = False) it will put in the buffer and print all the buffer in oneshot. if there is flush=True 
3 >>> (sleep1)
3 >>> 2 (sleep1)
3 >>> 2 >> 1 (sleep1)
3 >>>2 >>>1 >>start (sleep1)
==============================================
a=12
b=12
c=2022
print(a,b,c)
print(a,b,c,sep=":")
print(a,b,c,sep="")

12 12 2022
12:12:2022
12122022
======================================
number1 = 9
number2=5.333
print("Geeks : %2d, Portal : %5.2f" % (number1, number2))
print("Geeks : %02d, Portal : %05.2f" % (number1, number2))
#print("Geeks : %02d, Portal : %05.2f" %number1,%number2) Not allowed
print("Geeks : %02d" % number1)
print("Geeks : %04o" % number1)
#d for int, f float o octal e exponential
=======
Geeks :  9, Portal :  5.33
Geeks : 09, Portal : 05.33
Geeks : 09
Geeks : 0011
==================================
#dict or map will use only this { paramaeter not [
tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678, 'dude':12.5333}
tab1 = {'geeks': 24127, 'for': 24098, 'geek': 28637678, 'dude':212.5333}
# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
    'Geeks: {0[geek]:d}' ' {0[dude]:5.2f}'.format(tab, tab1))

print('Geeks: {1[geeks]:d}; For: {1[for]:d}; '
    'Geeks: {1[geek]:d}' ' {1[dude]:5.2f}'.format(tab, tab1))
    
print('Viswa Geeks: {geeks};'' For: {geek}; '.format(**tab)) #** operator is used for dictionary unpacking

print('Viswa1 Geeks: {0[for]};'.format(tab))

data = dict(fun ="GeeksForGeeks", adj ="Portal") #{'fun': 'GeeksForGeeks', 'adj': 'Portal'} #dict can also be taking =
 
# using format() in dictionary
print("I love {fun} computer {adj}".format(**data))

print(*data)
	 
====
Geeks: 4127; For: 4098; Geeks: 8637678 12.53
Geeks: 24127; For: 24098; Geeks: 28637678 212.53
Viswa Geeks: 4127; For: 8637678; 
Viswa1 Geeks: 4098;
I love GeeksForGeeks computer Portal
fun adj
================================================
data = {}
print (type(data)) #dict
data = dict()
print (type(data)) #dict
===============================================
data = dict(fun ="GeeksForGeeks", adj ="Portal")
print((*data)) #fun adj 
================================
cstr = "I love geeksforgeeks"
   
# Printing the center aligned 
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#')) # print (cstr.center(40, "#"))
 
# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))
 
# Printing the right aligned string
# with "-" padding 
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))
=====
Center aligned string with fillchr: 
##########I love geeksforgeeks##########
The left aligned string is : 
I love geeksforgeeks--------------------
The right aligned string is : 
--------------------I love geeksforgeeks
"""
%o octal
{0[geeks}d} => no %d
x,y for enumerate object
string.ljust .rjust
((*dict)) => print only keys