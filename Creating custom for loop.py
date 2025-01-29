#Let's build a custom for loop for iterables with iter function

def my_func(iterable):
    it = iter(iterable) #converts the iterable into an iterator
    
    while True:
        try:
            print(next(it)) # print elements of the iterator object untill it is exhausted    
        except StopIteration: # Handle the StopIteration error that will occur after reaching the last element of the iterator
            break

my_func(iterable=[1,2,3,4,5])

#Lets add a custom function to perfrom on the iterables 

#Let's create a custom function to get square of numbers
def square(x):
    return x*x

#Let's include that function into the custom for loop function
def my_func2(iterable,func):
    it = iter(iterable)
    while True:
        try:
            element = next(it)
            print(func(element))
        except StopIteration:
            break
        
my_func2(iterable=[1,2,3,4,5,6,7,8,9,10],func=square)