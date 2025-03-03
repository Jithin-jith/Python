#CHALLENGE
"""Shape Area Calculator:

1. Create a base class Shape with a method area().
2. Derive Rectangle and Circle classes, overriding the area() method to return respective areas."""

#1. Create a base class Shape with a method area().
class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        return f"The area of the {self.name} if ___."
    
shape1 = Shape('random_shape')
print(shape1.area())

#2. Derive Rectangle and Circle classes, overriding the area() method to return respective areas."""

class Rectangle(Shape):
    def __init__(self,name,length,breadth):
        super().__init__(name)
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return f"The area of the Rectangle is {self.length * self.breadth}"
    
rect1 = Rectangle(name="Rectangle",length=5,breadth=10)
print(rect1.area())

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return f"The area of the circle is {3.14*self.radius**2}"
    
circle1 = Circle(radius=10)
print(circle1.area())