#A namespace in a class is a mapping of names (attributes and methods) to objects (values/functions).
# Each class and instance has its own namespace.

#Let's create a class
class Person:
    pass

#The namespace can be accessed by '__dict__' attribute
print(f'Namespace of the class is : {Person.__dict__}')
print(f'Type of the namespace is : {type(Person.__dict__)}') #MappingProxy

#If we add a new attribute, then it will be reflected in the namespace
Person.name = 'John'
print(f'Namespace of the class after adding name attribute is : {Person.__dict__}')

#But MappingProxy is a read-only Namespace. We cannot add attributes indirectly
try :
    Person.__dict__['age'] = 25
    print("Added to namespace")
except:
    print("Could not add to namespace")
    
#Now lets look at an instance of this class

class Person:
    pass

p1 = Person()

print(f'Namespace of the instance is : {p1.__dict__}') #Empty dictionary
print(f'Type of the namespace is : {type(p1.__dict__)}') #MappingProxy

#If we add a new attribute, then it will be reflected in the namespace
p1.name = 'Leonard'
print(f'Namespace of the class after adding name attribute is : {p1.__dict__}')

#we can modify the instance dictionary
p1.__dict__['age'] = 25
#The age attribute will be reflected in the namespace
print(f'Namespace of the class after adding age attribute is : {p1.__dict__}')