#let's make a dataclass immutable

from dataclasses import dataclass

@dataclass(frozen=True) #Setting froxen=True makes the class immutable to later changes
class Person:
    name : str
    age : int
    city : str
    
p1 = Person(name="Ted",age=10,city="New york")
print(p1)

#Now let's try to change the attributes
# p1.name = "Jack" -- This will raise error