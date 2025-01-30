#A higher-order function (HOF) is a function that takes another function as an argument or returns a function as a result.
from random import choice

def make_laugh(): #This is the outer function
    def get_laugh(): #This is the inner function
        laugh = choice(("HAHAHA","hehehhe","hohohohohoho")) #randomly select a value
        return laugh # return the randomnly selected value
    return get_laugh #return the inner function 

laughing = make_laugh()  #create an variable from the outer function
print(laughing()) #calling the inner function from the variable

#Now let's create a function that can accecpt an argument

def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(("HAHAHA","hehehhe","hohohohohoho"))
        return f"{laugh} : {person}"  #return the randomly selected laugh variable and the person name passed into the main function
    return get_laugh
laugh_at = make_laugh_at_func("Tyson")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())

#Now let's create a function that can accept a function as a argument
def square(x): #create a function to return the sqaured value
    return x*x

def num(numbers,func): #create a function that will accept a list of numbers and the function
    for num in numbers:
        squared_value = func(num)
        yield squared_value #it will save the value and maintain state without terminating the function        
numb = num([1,2,3,4,5],func=square) #The variable numb will be an iterator.
print(f"The squared values are : ")
for num in numb:
    print(num)