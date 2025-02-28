#assert keyword in python
"""
The assert statement in Python is used for debugging purposes. 
It tests whether a condition is True, and if not, it raises an AssertionError with an optional error message.
"""
#Syntax of assert
'''
assert condition, "Optional error message"
'''
# - If condition evaluates to True, the program continues execution
# - If condition is False, an AssertionError is raised.

#Use Cases of assert
#1.Debugging and Error Checking
x = 10
assert x > 0, "x should be positive"

#2.Input Validation
def divide(a, b):
    assert b != 0, "Denominator cannot be zero"
    return a / b
print(divide(5,3))

#3.Ensuring Invariants in Code
def get_square_root(n):
    assert n >= 0, "Cannot compute square root of a negative number"
    return n ** 0.5
print(get_square_root(33))

#Disabling Assertions
'''
Assertions can be globally disabled using the -O (optimize) flag while running the script.
Example - python -O Assert.py
'''
#In optimized mode, all assert statements are ignored, improving performance.

#When NOT to Use assert
'''
- Assertions should be used only for debugging, not for handling runtime errors because as explained it can be disabled by using -o flag.
- Use exceptions like ValueError for handling invalid user input:
'''
#Example :

def divide(a, b):
    if b ==0:
        raise ValueError("b cannot be zero")
    return a / b
print(divide(5,2))


