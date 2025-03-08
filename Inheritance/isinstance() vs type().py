#isinstance vs type function 
"""In Object-Oriented Programming (OOP) in Python, both isinstance() and type() are used to check the type
of an object, but they have key differences in how they work and when to use them."""

#1. type() Function
# -- Returns the exact type of an object.
# -- Does not consider inheritance.
# -- Used when you need an exact match.

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print("\n")
print("Using type() function : ")
print(type(dog) == Dog)    # True
print(type(dog) == Animal) # False (even though Dog is a subclass of Animal)
# It does not recognize that Dog is a subclass of Animal

#2. isinstance() Function
# -- Checks if an object is an instance of a class or its subclass.
# -- Considers inheritance, making it more flexible for OOP.
print("\n")
print("Using isinstance() function : ")
print(isinstance(dog, Dog))    # True
print(isinstance(dog, Animal)) # True (Dog is a subclass of Animal)