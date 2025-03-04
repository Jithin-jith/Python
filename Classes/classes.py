#A class is like a template used to create objects
#They are also called type

#Let's create a class
class Person:
    """A persoon class"""
    pass

#Let's create a object p. Objects created from a class are called 'Instances'
p = Person()
print(type(p)) #The type of the instance/object will be the person class

print(type(Person))#  But the type of the class Person will be 'type'

#ie; the type of an instance will be the class and the type of the class will be 'type'
# This applies to even inhertied classes. Let's see an example

class Student(Person):
    """A Student class inherited from the persoon class"""
    pass

s = Student()
print(type(s)) #The type of this instance/object will be the Student class

print(type(Student)) #However the type of Student class will be 'type' itself.

#CLASSES ARE THEMSELVES OBJECTS
# -- They have name
# -- They have behaviours. They can create instances of the class

#IF A CLASS IS AN OBJECT AND OBJECTS ARE CREATED FROM CLASSES, THEN HOW ARE CLASSES CREATED ???
"""In python classes are created from the type "metaclass" """

#When python goes through the following class code. It creates an object
#It then automatically provides some attributes and methods

class Student(Person):
    """A Student class inherited from the persoon class"""
    pass
s = Student()
print(Student.__name__)
print(Student.__dict__)
print(isinstance(s,Student))
type(Student)