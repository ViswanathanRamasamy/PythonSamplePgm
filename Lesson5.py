"""
	Lesson 5: Sample program for the python.
	Source Code Location: https://github.com/ViswanathanRamasamy/PythonSamplePgm.git
	Author Name: Viswanathan Ramasamy
	Email id: rviswawt@gmail.com
"""
===================================================
#to print the warning message

import warnings

# Define a deprecated function
def deprecated_function():
    warnings.warn("This function is deprecated and should not be used.", DeprecationWarning)
    # Rest of the function's code

# Call the deprecated function
deprecated_function()

================================================
#default argumenet should always the last parameters

def greet_with_message(name="User", message="Hello"):
    """Greets a person with a custom message."""
    print(f"{message}, {name}!")

# Call the function with and without providing values for 'name' and 'message'
greet_with_message()                    # Uses default values 'User' and 'Hello'
greet_with_message("Alice")             # Uses 'Alice' with the default message 'Hello'
greet_with_message("Bob", "Good day")   # Uses both provided values 'Bob' and 'Good day'

=====================================
lista = [1, 2, 3, 4, 5]
mask = [True, False, True, False, True]

result = [x for x, m in zip(lista, mask) if m]
print(result)

[1 3 5]
=======================================
# Create two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Use zip to combine the lists element-wise into tuples
combined = list(zip(names, scores))

print (combined)
# Print the result
for name, score in combined:
    print(f"{name}: {score}")

[('Alice', 85), ('Bob', 92), ('Charlie', 78)]
Alice: 85
Bob: 92
Charlie: 78
===================================
# Create two lists
names = ["Alice", "Bob", "Charlie"]
names1 = []
# Print the result
if names:
    print(f"viswa")

if names1:
    print(f"viswa2")
 
 Viswa
====================================
result = (256).bit_length() => 9
===============================
# To change the ckass level attribute
class MyClass:
    class_variable = 0  # A class-level variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    def display_variables(self):
        print(f"Instance variable: {self.instance_variable}")
        print(f"Class variable: {MyClass.class_variable}")

# Create instances of MyClass
obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")

# Call the class method to increment the class variable
MyClass.increment_class_variable()

# Display instance and class variables for obj1 and obj2
obj1.display_variables()
obj2.display_variables()
=====
Instance variable: Instance 1
Class variable: 1
Instance variable: Instance 2
Class variable: 1
===================================
Static Method:

A static method is defined using the @staticmethod decorator.
It does not receive the instance (self) or the class (cls) as its first parameter by default. Instead, it behaves like a regular function.
Static methods are primarily used when a method does not need access to instance-specific data or class-level data. They are self-contained 
and don't depend on the class or its instances.
class MyClass:
    @staticmethod #It is not must to have the @static
    def static_method():
        print("This is a static method")

MyClass.static_method()
obj = MyClass()
obj.static_method()
===========================
static method called by the class method?

class MyClass:
    class_variable = 0

    @staticmethod #not strictly necessary
    def static_method():
        print("This is a static method")

    @classmethod #not strictly necessary
    def class_method(cls):
        print("This is a class method")
        # Call the static method using the class name
        MyClass.static_method() #cls.static_method()

# Call the class method
MyClass.class_method()

=========================
#when the class attribute is modified by the Instance metheod it will be local to the object.
class MyClass:
    class_attribute = 0

    @staticmethod
    def static_method():
        MyClass.class_attribute += 1

    def instance_method(self):
        self.class_attribute += 1
        
     @classmethod
    def class_method(cls):
        cls.class_attribute += 1
        
 
 MyClass.class_method() #1 
print(MyClass.class_attribute)  # Output: 1

obj = MyClass()
obj.instance_method() #2
print(obj.class_attribute) 

MyClass.static_method() #2
print(MyClass.class_attribute)  # Output: 1
====================================================
#static method will return the static property
class Dog:
    _ear = 2 #static attribute , _is preferred
    
    def __init__(self,name): #instance method
        self.name=name #instance attribute
        self.leg=4 #instance attribute
        
    def getLeg(self): #instance method
        return (self.leg)
    
    def get_ear(): #static method
        return (_ear)
    
	def getDog(self):
	  self.getanimal()
	  
	  
    def getDog(self):
        self.getanimal() #instance method
        Dog.getanimal2() #static method // you can also call like self.getanimal2()
		self.getanimal3() # instance method can call other instance method
	
    def getanimal(self):
	    print("hi inside getanimal")
	     
    def getanimal2():
	     print("hi inside getanimal2",Dog.ear) #static method can access only the static attribute
	
    @staticmethod	#below function is static method #This is required when we are going to call the function name using the object
	def getanimal3():
	     print("hi inside getanimal3",Dog.ear) #static method can access only the static attribute

myDog = Dog("Rover")
print(myDog.name) #rover    
print(myDog.leg) #4 
print(myDog._ear) #2 
myDog.leg=5 #class attribute can be changed outside the class
print(myDog.leg)  #5
#print(Dog.leg) #only static attribute can be accessed using class
Dog._ear =3 
print(myDog._ear) #3
print(myDog.ear) #100
print(Dog.ear) #3
myDog.getDog()#hi inside getanimal
hi inside getanimal2
hi inside getanimal3 3
=====================
#printing the static variable in the static and instance method
class Dog:
    _ear = 2 #static attribute , _is preferred
    
    def __init__(self,name): #instance method
        self.name=name #instance attribute
        self.leg=4 #instance attribute
        
    def getIear(self): #instance method
        print(self._ear)
    
    @staticmethod #This is required when we are going to call the function name using the object
    def get_ear(): #static method
        return (Dog._ear)
    

myDog = Dog("Rover")
#myDog.get_ear(); cannot access the static attribute if there us no @staticmethod 
myDog._ear =100
myDog.getIear(); #100
print(myDog.get_ear()) #2
=====================================
//calling the instance method directly without the functon
class Dog:
    def __init__(self,name):
        self.name=name #instance attribute
        self.leg=4 #instance attribute
        
    def get_bark(self):
        print("bark bark")
    
#inheritance
class SDog(Dog):
    def get_bark(self):
        print("mysmall bark bark",self.name,self.leg) #mysmall bark bark rover2 40

mySDog = SDog("rover2")

#error Dog.get_bark("")
Dog.get_bark("") #bark bark 
Dog.get_bark(SDog) #bark bark 
mySDog.get_bark() #mysmall bark bark rover2 4
SDog.get_bark(mySDog) #mysmall bark bark rover2 4
===========================================
# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived class (child class) inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another derived class (child class) inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on instances
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
===================================================
cooperative multiple inheritance:
class A:
    def action(self):
        print("A's action")

class B(A):
    def action(self):
        super().action()
        print("B's action")

class C(A):
    def action(self):
        super().action()
        print("C's action")

class D(B, C):
    def action(self):
        super().action()
        print("D's action")

d = D()
d.action()  # Calls actions from A, C, B, and D
============================================
multiple inheritance:
class Parent1:
    def some_method(self):
        print("Method from Parent1")

class Parent2:
    def some_method(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def some_method(self):
    #note super().some_method() will call only the parent1 calss method and not parent2
        super(Parent1, self).some_method()  # Call Parent1's method explicitly
        super(Parent2, self).some_method()  # Call Parent2's method explicitly

c = Child()
c.some_method()  # Calls methods from both Parent1 and Parent2

===========================================
#method overriding
class Parent:
    def some_method(self):
        print("Parent's method")

class Child(Parent):
    def some_method(self):
        super().some_method()  # Call the parent class's method
        print("Child's method")

c = Child()
c.some_method()  # Calls both Parent's and Child's methods
=====================================
#constructor inheriatance
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the parent class's constructor
        self.age = age

c = Child("Alice", 25)

=================================
#super() will not have the self keyword in the function call.
#but it can have self keyword and class if it argument of super.
class Parent1:
    def __init__(self, arg1):
        self.arg1 = arg1

    def method1(self):
        print(f"Parent1 method with arg1: {self.arg1}")

class Parent2:
    def __init__(self, arg2):
        self.arg2 = arg2

    def method2(self):
        print(f"Parent2 method with arg2: {self.arg2}")

class Child(Parent1, Parent2):
    def __init__(self, arg1, arg2, arg3):
        super().__init__(arg1)  # Call Parent1's constructor with arg1
        Parent2.__init__(self, arg2)  # Call Parent2's constructor with arg2
        self.arg3 = arg3

    def method3(self):
        print(f"Child method with arg3: {self.arg3}")

# Create an instance of Child with all required arguments
child = Child("Value1", "Value2", "Value3")

# Access methods and attributes from Parent1, Parent2, and Child
child.method1()  # Output: Parent1 method with arg1: Value1
child.method2()  # Output: Parent2 method with arg2: Value2
child.method3()  # Output: Child method with arg3: Value3
============================
# if the child object calls a function and the function is not there in the derived class then the method in the base class will be called
#overriding of the methof of the parent with derived class function with argument:
class Parent:
    def greet(self, name):
        print(f"Hello, {name}!")

class Child(Parent):
    def greet(self, name):
        # Call the parent class's greet method using super()
        super().greet(name)
        print("How are you doing today?")

# Create an instance of the Child class
child = Child()

# Call the overridden greet method
child.greet("Alice")
===
Hello, Alice!
How are you doing today?
===============================================
====================================
Class extended from LIst base class:
=====================
class UniqueList(list):
    x = 3 #this has nothing to do with the list content
    def append(self, number):
        if number in self:
            return
        else:
            super().append(number)
            #self.append(number) Will call the append in the Uniquelist class and lead to recursive loop
    

myUniqueList = UniqueList()
myUniqueList.append(1)
myUniqueList.append(2)
myUniqueList.append(4)
myUniqueList.append(1)

print(myUniqueList) #[1,2,4]
==============================================
dict1 = {
    "a": {"apple1","appl2",},
    "b": {"ball1","ball2",},
    "c": {"cat",},
    "d": {"dog","dog2",},
}

for x in dict1:
    print(x) #print only the keys


for x,y in dict1.items():
    print(y) #print all the valuses
print()

for x,y in dict1.items():
    if(len(y) <= 1):
      print(y) #cat
=====================
a
b
c
d
{'apple1', 'appl2'}
{'ball1', 'ball2'}
{'cat'}
{'dog', 'dog2'}

{'cat'}
================================
#to print the prime number
for x in range(2, 101):
    is_prime = True  # Assume x is prime initially
    for y in range(2, int(x**0.5) + 1):  # Include the square root value
        if x % y == 0:
            is_prime = False  # Found a factor, so x is not prime
            break

    if is_prime:
        print(x, end=" ")

[print(y) for y in range(2,-1)] # nothing it will print since the starting is in 2nd  and ending is -1        
[print(y) for y in range(2,5)] #2 3 4 
print ([print(y) for y in range(2,5)]) # 1 2 3 [None none None]
print("pgm end")
 ===============
 #no output:  for else
for number in range(1, 100):
    if number % 10 == 0:
        break ; # because of break it will not print the else part , it it is continue it will print the else part
else:
    print('Let\'s print something out!') 
======
for number in range(1, 100):
    if number % 10 == 0:
        continue
else: #else block is associated with the for loop
    print('Let\'s print something out!', number) #99
print (number) #99
=======
#named parameter ie passing the default value. name parameter(keyword argument) should be after the positional argument. 
positional  argument we cannot change the order.

def perform_operation(a,b,operation="sum", message="default message"):
    print(message)
    if operation=="sum":
        return(a+b)
    if operation=="multiply":
        return(a*b)
        
print(perform_operation(2,3,"sum")) #default message 5
print(perform_operation(2,3,)) # default message 5 , after 3 is not must
print(perform_operation(2,3,"multiply")) #default message 6
print(perform_operation(2,3,operation="multiply")) #default message 6
print(perform_operation(2,3,operation="multiply", message="welcome")) #welcome 6
print(perform_operation(2,3, message="welcome")) #welcome 5
print(perform_operation(2,3, message="welcome3",operation="multiply")) #welcome3 6
================================================
class Dog: #class name should always start in caps 
  
  def __init__(self):
    self.name = "rovera" #name and leg are caled attribut
    self.leg = 4
  
  def speak(self): #speak is called method or class function
    print("bark " + self.name)
    
my_dog = Dog() # class name should be send
my_dog.speak() # bark rovera
type(Dog()) #dog
type(my_dog) #dog
type(Dog) #error
===========================================