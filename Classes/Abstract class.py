# An abstract class in Python is a class that cannot be instantiated and serves as a blueprint for other classes. 
# It is used to define common behavior and enforce that derived classes implement specific methods.
# Abstract classes in Python are defined using the ABC (Abstract Base Class) module from the abc package.

#Let's see with an example

from abc import ABC, abstractmethod

# Defining an Abstract Class
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        """Abstract method that must be implemented in subclasses"""
        pass

    def sleep(self):
        """Concrete method that can be used directly"""
        print("Sleeping...")

# Subclass Implementing the Abstract Class
class Dog(Animal):
    
    def make_sound(self):
        return "Bark"

# Creating an instance of Dog
dog = Dog()
print(dog.make_sound())  # Output: Bark
dog.sleep()  # Output: Sleeping...

# Trying to instantiate the abstract class will raise an error
try :
    animal = Animal() # TypeError: Can't instantiate abstract class Animal
except TypeError as ex:
    print("Can't instantiate abstract class Animal")

# KEY POINTS
# -- Cannot Instantiate Abstract Classes: Animal() would raise a TypeError.
# -- Forces Implementation: If Dog did not implement make_sound(), it would raise an error.
# -- Can Have Concrete Methods: Abstract classes can have both abstract and concrete (regular) methods.