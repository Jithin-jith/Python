# Encapsulation using property
"""we use the @property decorator to create controlled access to private attributes."""

class Person:
    def __init__(self, name, age):
        self._name = name  # Private attribute (_name)
        self._age = age    # Private attribute (_age)

    @property
    def age(self):
        """Getter method (controlled access to _age)"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter method with validation"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

# Usage
p = Person("Alice", 25)
print(p.age)  # 25 (Accesses _age through getter)

p.age = 30   # Allowed (Setter validates before changing)

try:
    p.age = -5
except ValueError as ex:
    print("Age cannot be negative")