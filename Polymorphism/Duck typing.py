#Duck typing is a way of implementing polymorphism
#Duck Typing emphasizes behavior over explicit type definitions.
""" Instead of checking an object's type, Python allows us to use an object as long as it supports 
    the expected methods and properties"""
# "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

"""This means that Python does not require explicit interface declarations like in statically typed languages 
(e.g., Java or C++). Instead, it focuses on whether an object behaves as expected."""

# Let's see an example

class Duck:
    def quack(self):
        return "Quack! Quack!"

class Dog:
    def quack(self):
        return "I'm a dog, but I can quack! Woof-Quack!"

def make_it_quack(animal):
    return animal.quack()  # No type checking, just assuming it has a quack() method

# Works because both have a quack() method
donald = Duck()
bruno = Dog()
print("\n")
print("Example 1:")
print(make_it_quack(donald))  # Output: Quack! Quack!
print(make_it_quack(bruno))   # Output: I'm a dog, but I can quack! Woof-Quack!

# Now, Why does this work?
# -- We didn't check if animal is an instance of Duck.
# -- As long as the object has a quack() method, it works!

#Let's see another example:
"""Imagine a function that calculates the area of a shape. Instead of forcing objects to belong to a Shape 
class, we simply expect them to have an area() method."""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

def calculate_area(shape):
    return shape.area()  # No need to check if it's a Circle or Square

circle1 = Circle(5)
square1 = Square(4)
print("\n")
print("Example 2:")

print(f"The are of the circle is : {calculate_area(circle1)} m^2")  # Output: 78.5
print(f"The are of the square is : {calculate_area(square1)} m^2")  # Output: 16