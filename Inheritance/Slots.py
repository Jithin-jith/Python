#SLOTS 
"""__slots__ is a special attribute that allows you to explicitly define the attributes (variables) an object can have.
It helps reduce memory usage and improves performance by preventing the creation of a dynamic dictionary (__dict__) for each instance."""

#Some advantages of slots are :

# -- Memory Optimization
# -- Performance Improvement
# -- Prevents Accidental Attribute Creation

#Let' see an example

class Car:
    __slots__ = ['brand', 'model', 'year']  # Define allowed attributes

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

# Creating an object
car1 = Car("Toyota", "Corolla", 2022)

print(car1.brand)  # Output: Toyota

try:
    car1.color = "Red"  # AttributeError: 'Car' object has no attribute 'color'
except AttributeError as ex:
    print(" AttributeError : Cannot assign atribute as it is not defined in slots")
    
try:
    print(car1.__dict__)
except AttributeError as ex:
    print("No attribute __dict__")

# When not to use slots
# -- If you need dynamic attributes that are not predefined.
# -- If the class inherits from a class without __slots__, as it won't prevent __dict__ creation in the parent class.
# -- If you need multiple inheritance, as __slots__ can cause conflicts.