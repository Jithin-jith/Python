# Dataclasses

#Let's create a normal class
print("Normal class : ")
class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

p = Person("Alice",30,"New York")
p2 = Person("Alice",30,"New York")
print(f'The __repr__ method : {p}') #This will call the __repr__ method as __str__ is not defined.
print(f'The __eq__method : {p == p2}') #This will return FALSE

"""Now let's check the same for a dataclass. Dataclass will implement __init__,__repr__ and __eq__ methods
by default"""
print("\n")
print("Data class : ")
#Let's see how we can define a data class
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

p = Person("Alice", 30, "New York")
p2 = Person("Alice",30,"New York")
print(f'The __repr__ method : {p}') #This will call the defined __repr__ method
print(f'The __eq__method : {p == p2}') #This will return TRUE