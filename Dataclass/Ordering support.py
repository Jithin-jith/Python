#Let's try to compare two instance created from a dataclass

from dataclasses import dataclass

@dataclass
class Person:
    name : str
    age : str
    
p1 = Person(name="erin",age=28)
p2 = Person(name="Ken",age=30)

try:
    print(p2>p1)
except TypeError as ex:
    print("cannot compare")
    
# Now let's compare the by setting an order = True

@dataclass(order=True)
class Person:
    age : str
    
p1 = Person(age=28)
p2 = Person(age=30)

print(p2>p1) #True