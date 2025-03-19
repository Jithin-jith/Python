#In dataclasses we can define default values

from dataclasses import dataclass

@dataclass
class Person:
    name: str =  "No Name"
    age: int = 1
    city: float = "New Delhi"
    
p = Person()
print(p)

#Let's remove one default value from the class defiition

@dataclass
class Person:
    age: int  #Non default attributes must be defined before the default attributes
    name: str =  "No Name"
    city: float = "New Delhi"
    
try:    
    p = Person() #This will raise a type error as we have not passed any arguments for non default attribute
except TypeError as ex:
    print("non-default argument must be defined!")
    
p = Person(age=10)
print(p)

#Another way of using default values is by using the field function
#Lets first import the field function

from dataclasses import field
@dataclass
class Person:
    age: int = 10  #Non default attributes must be defined before the default attributes
    name: str =  field(default="No name")
    city: float = "New Delhi"
    
p = Person()
print(p)

#lets create a function that returns a random number as age between 1 and 70
import random
def age_func():
    return random.randint(1,70)

#Now we can pass this function as an argument to the field function. Let's see
@dataclass
class Person:
    age: int = field(default_factory=age_func) 
    name: str =  field(default="No name")
    city: float = "New Delhi"
    
p = Person()
print(p)

#we can also pass list of values as an argument since we have list() function
@dataclass
class Person:
    age: int = field(default_factory=age_func) 
    name: str =  field(default="No name")
    city: float = field(default_factory=list) #This will create an empty list
    
p = Person()
print(p)

#let's pass some values to overrite the default values
@dataclass
class Person:
    age: int = field(default_factory=age_func) 
    name: str =  field(default="No name")
    city: float = field(default_factory=list) #This will create an empty list
    
p1 = Person(age=10,name='Ken',city='Mumbai')
print(p1)
p2 = Person(age=10,name='Ken',city=['Mumbai','New Delhi'])
print(p2)