# Even when we define a class that does not inherit from any class explicitly, Python makes the class
# inherit from the "object class" implicitly

#so basically
class Person:
    pass

#is same as 
class Person(object):
    pass

#Here object is a class similar to other classes like int,str
print(type(object),type(int),type(str))

#let's validate using the subclass function
print(issubclass(Person,object)) #True

print(issubclass(int,object)) #True

#Hence every class we create is a subclass of object class
#and every instance we create is an instance of object class

"""Therefore any class we create automatically inherits behaviours and attributes from the object class
for example"""
#__name__
#__new__
#__init__
#__repr__
#__eq__   -> uses the id() to check if two instances are same
#__hash__

"""Hence we can use all the default implementations that are defined in the object class"""

#Apart from clas which is a type, let's see what are the other types of type
import types
print(dir(types))

#All these types are a subclass of the object class
#for example

print(issubclass(types.AsyncGeneratorType,object)) #True

#HOW TO CHECK IF A METHOD/ATTRIBUTE IS OVERRIDDEN?
class Person:
    pass

#now there are some defaults methods like __init__. Let's check the id() of init in Person and object class
print(id(Person.__init__),id(object.__init__)) #id's will be same as it is inherited and not overridden

#now lets see a case where the __init__ method is overridden
class Person:
    def __init__(self):
        pass
    
print(id(Person.__init__),id(object.__init__)) #id's will be different as the init method is overridden