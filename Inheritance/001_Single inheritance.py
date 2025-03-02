# Single Inheritance
# Let's define classes that inherit from another class
# For now let's not implement any functionality or state for these classes.

class Shape:
    pass

class Ellipse(Shape):
    pass

class Circle(Ellipse):
    pass

class Polygon(Shape):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Triangle(Polygon):
    pass

# The **classes** are subclasses of each other -
# "subclass" contains the word "class" - so it defines a relationship between classes, not instances:

print(issubclass(Ellipse, Shape))

s = Shape()
e = Ellipse()
try:
    issubclass(e, s)
except TypeError as ex:
    print(ex)
    
print(isinstance(e, Ellipse))

#When we deal with instances of classes, we can instead use the `isinstance()` function:
print(isinstance(e, Ellipse))

# But, not only is 'e' an instance of an 'Ellipse', since 'Ellipse' IS-A 'Shape', i.e. 
# 'Ellipse' is a "subclass" of 'Shape', it tunrs out thet 'e' is also considered an instance of 'Shape':

print(isinstance(e, Shape))

# Subclasses behave similarly in that a class may be a subclass of another class without being 
# a "direct subclass".
"""In our example here, every class we defined is a subclass of `Shape` because the inheritance 
chains all go back up to the `Shape` class"""

print(issubclass(Square, Shape))

# And of course, the same works for instances when we look at `isinstance`
sq = Square()
print(isinstance(sq, Square))


