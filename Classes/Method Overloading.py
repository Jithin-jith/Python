#Method Overloading

"""
- Method overloading in Python refers to the ability to define multiple methods with the same name 
but different parameters.
- However, unlike some other languages like Java or C++, Python does not support traditional method
overloading directly.
- Instead, you can achieve similar behavior using default arguments, variable-length arguments, 
or by manually checking argument types/lengths inside a method.
"""

# Python only allows the latest definition of a method with the same name. Earlier ones are overridden.

# 1. Using Default Arguments
class Greet:
    def hello(self, name="Guest"):
        print(f"Hello, {name}!")

g = Greet()
g.hello()              # Output: Hello, Guest!
g.hello("Alice")       # Output: Hello, Alice!

# 2. Using Variable-Length Arguments (*args)
class Calculator:
    def add(self, *args):
        return sum(args)

c = Calculator()
print(c.add(2, 3))            # Output: 5
print(c.add(2, 3, 4, 5))      # Output: 14

# 3. Type Checking Inside a Method
class Multiply:
    def product(self, a, b=None):
        if b is None:
            return a * a
        else:
            return a * b

m = Multiply()
print(m.product(5))       # Output: 25 (square)
print(m.product(5, 3))    # Output: 15
