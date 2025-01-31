#Decorators are functions that wrap other functions and enhance its behaviour.
#They are examples of Higher order functions
#They have their own syntax, using "@".

#Let's create a wrapper function to wrap another function
def be_polite(func): # The main wrapper function
    def wrapper(): 
        print("Hello. Nice to meet you!")
        print(func())
        print("See you! Take care")
    return wrapper # Returns the sub function
    
def greet(): #the function to be wrapped
    return "How are you?"

polite = be_polite(func=greet) #save the returuned function into a variable
polite() #run the function

#Now let's create the Decorator using the synta "@"

@be_polite # The syntax used to mention the wrapper function
def scold(): #The function that needs to be wrapped
    return "I HATE YOU"  #The return value

scold()  #Run th function. No need to save the return and then execute the function

#STANDARD DECORATOR FUNCTION

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name,place):
    return f"Hi I am {name}, and I am from {place}"

print(greet(name="John",place="Berlin"))

#The above standard decorator function have a problem. 
#It cannot return us the function name,documentation etc
#Lets check that

def shout(fn):
    """This is a wrapper function."""
    def wrapper(*args, **kwargs):
        """This is a wrapper function."""
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name,place):
    """This is a function to greet a person by introducing yourself"""
    return f"Hi I am {name}, and I am from {place}"

print(greet.__name__) # It will print the name of the wrapper function
print(greet.__doc__) # It will print the docs of the wrapper function
print(greet(name="John",place="Berlin"))

#TO RESOLVE IT PYTHON USES WRAP MODULE FROM FUNCTOOLS
from functools import wraps

def shout(fn):
    """This is a wrapper function."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """This is a wrapper function."""
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name,place):
    """This is a function to greet a person by introducing yourself"""
    return f"Hi I am {name}, and I am from {place}"

print(greet.__name__) # It will print the name of the wrapper function
print(greet.__doc__) # It will print the docs of the wrapper function
print(greet(name="John",place="Berlin"))