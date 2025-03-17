# Abstraction is the process of hiding implementation details and only exposing the essential features of an object.
"""Python provides abstraction using abstract classes and abstract methods, 
which are defined using the ABC (Abstract Base Class) module."""

"""Methods which has only declaration and not definitions are called as 'Abstract Methods'.
Classes which has atleast one abstract method is called as Abstract class"""

# Let's see this with an example

# Lets create a base class called "Vehicle" that inherits from the ABC class

from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        """Abstract method to start the vehicle"""
        pass
    
    @abstractmethod
    def stop(self):
        """Abstract method to stop the vehicle"""
        pass
try:
    v1 = Vehicle() #Abstract class cannot be initialised
except TypeError as ex:
    print("Can't instantiate abstract class Vehicle without an implementation for abstract methods 'start', 'stop'")
    
#So lets create a subclass and implement these methods - "start" and "stop".

# Concrete Class (Subclass) implementing the abstract methods
class Car(Vehicle):
    def start(self):
        print("Car is starting with a key ignition.")
    
    def stop(self):
        print("Car is stopping with a brake.")

car = Car()
car.start()  # Output: Car is starting with a key ignition.
car.stop()   # Output: Car is stopping with a brake.

#Let's see another example

# Concrete Class (Subclass) implementing the abstract methods
class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a self-start button.")
    
    def stop(self):
        print("Bike is stopping with a hand brake.")
        
bike = Bike()
bike.start() # Output: Bike is starting with a self-start button.
bike.stop()  # Output: Bike is stopping with a hand brake.

#KEY POINTS
# -- These methods "start" and "stop" do not have any implementation and must be implemented in any subclass.
# -- Each subclass provides its own unique implementation of these methods.
# -- Since Vehicle is an abstract class, it cannot be instantiated directly.
# -- Instead, we create objects of Car and Bike, which have their own implementations.