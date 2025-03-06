#Class Methods
"""When we define a function in a class , how we call it will alter its behavior"""
#let's create a class with a plain function defined in the class

class MyClass:
    def hello():
        return 'Hello'

print(MyClass.hello()) #This will return 'Hello'
#Let's create an instance of the class

my_class = MyClass() 
try:
    print(my_class.hello())
except TypeError as ex:
    print("Missing self argument in function definition")
    
#The function hello() cannot be called from the instance as self parameter is not defined.

#Let's create a function with some default value
class MyClass:
    def hello(arg = 'Name'):
        return f'Hello {arg}'
    
my_class = MyClass() 
try:
    print(my_class.hello()) # now this will return the 'Hello and the location of the function'
except TypeError as ex:
    print("Missing self argument in function definition")
    
#But if we pass an argument it will raise error

my_class = MyClass() 
try:
    print(my_class.hello('John')) # now this will return the 'Hello and the location of the function'
except TypeError as ex:
    print("Missing self argument in function definition")