#What is a Iterable?
"""It is an object/collection of objects that will return an Iterator when iter() is called on it.\n
   Examples of iterables: Lists, tuples, dictionaries, strings, sets, and any object that implements __iter__()."""

my_list = [1, 2, 3, 4]  # List is an iterable
my_string = "hello"  # String is also an iterable

#What is Iterator?
"""It is an object that can be iterated upon. It is an object that returns data, one element at a time when next() is called.\n
    To create an iterator from an iterable, we use the iter() function."""
    
my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)  # Convert list into an iterator

print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2

#We can use next() function to check whether a given object is a iterable or a iterator
#If we get error saying ___ is not a iterator then it is a iterable
#it can then be converted to a iterator by passing it into an iter() function.
try:
    print(next(my_string))
except:
    it = iter(my_string)
    print(f'firxt element of the iterator : {next(it)}')
    print(f'Second element of the iterator : {next(it)}')