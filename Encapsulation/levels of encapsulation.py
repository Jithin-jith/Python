#Python provides three levels of encapsulation

#1. Public Members
"""
-- These can be accessed from anywhere inside or outside the class.
-- Defined without any leading underscores.
"""
class Person:
    def __init__(self, name):
        self.name = name  # Public attribute

p = Person("Alice")
print(p.name)  # Accessible from outside

#2. Protected Members
"""
-- Indicated by a single underscore (_), suggesting they should be accessed only within the class and its subclasses.
-- Still accessible from outside but considered a convention to avoid direct access.
"""
class Person:
    def __init__(self, name):
        self._name = name  # Protected attribute

p = Person("Jack")
print(p._name)  # Technically accessible, but discouraged

#3. Private Members
"""
-- Indicated by a double underscore (__), making them name-mangled (internally renamed as _ClassName__attribute).
-- Prevents direct access from outside the class.
"""
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name  # Public method to access private data

p = Person("Anna")

try:
    print(p.__name)
except AttributeError as ex:
    print("Cannot access private variable")
print(p.get_name())  



