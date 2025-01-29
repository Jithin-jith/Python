# A generator function is a special type of function that returns an iterator object.
"""Instead of using return to send back a single value, generator functions use yield to produce a series of results over time. \n
This allows the function to generate values and pause its execution after each yield, maintaining its state between iterations."""

def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)

for n in ctr:
    print(n)
    
#YIELD VS RETURN
#YIELD
"""yield is used in generator functions to provide a sequence of values over time. When yield is executed, \n
it pauses the function, returns the current value and retains the state of the function. This allows the function to continue \n
from the same point when called again, making it ideal for generating large or complex sequences efficiently."""

#RETURN
"""return, on the other hand, is used to exit a function and return a final value. Once return is executed, the function \n
is terminated immediately, and no state is retained. This is suitable for cases where a single result is needed from a function."""

#example of return function
def fun():
    return 12345

fn = fun()
print(fn)

#PYTHON GENERATOR EXPRESSION
"""Generator expressions are a concise way to create generators. They are similar to list comprehensions but use \n
parentheses instead of square brackets and are more memory efficient."""

sq = (x*x for x in range(1, 6))
print(f'type of sq variabel is : {type(sq)}')
# now let's iterate and print out the values
for value in sq:
    print(value)
   
def stateful_generator():
    value = yield 'Starting Generator' # Receive a value from outside
    while True:
        value = yield value * 2

gen = stateful_generator()
print(next(gen))          # Start the generator
print(gen.send(10))  # Outputs: 20
