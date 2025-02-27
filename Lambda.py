#A lambda function is an anonymous function (i.e., a function without a name) defined using the lambda keyword.
#Syntax : 
"""lambda arguments: expression"""

#Let's create an add function using lambda
add = lambda x, y: x + y
print('result from a basic add function: ',add(5, 3))  # Output: 8

#Lambda functions support default, variable-length, and keyword arguments also.
#Default argument
multiply = lambda x, y=2: x * y
print('result from a default argument function: ',multiply(5))   # Output: 10 (uses default y=2)

#Variable-Length Arguments (*args and **kwargs):
#*args
sum_args = lambda *args: sum(args)
print('result from a variable length args: ',sum_args(1, 2, 3, 4))  # Output: 10
#**kwargs
concat_strings = lambda **kwargs: " ".join(kwargs.values())
print('result from a variable length kwargs: ',concat_strings(a="Hello", b="World,",c="Nice to meet you!"))  # Output: 'Hello World'

#Use Cases of Lambda Functions
#Lambda functions are often used in functional programming, especially with map(), filter(), and reduce()
#Using map() with Lambda
#map() applies a function to every item in an iterable.
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(f'squared values of the elements in the list {nums} : {squared}')  # Output: [1, 4, 9, 16]

#Using filter() with Lambda
#filter() selects elements based on a condition.
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(f'even numbers from the elements in the list {nums} : {even_nums}')  # Output: [2, 4, 6]

#Using reduce() with Lambda
#reduce() applies a function cumulatively to elements.
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(f'cumulative product of numbers in {nums} : {product}')  # Output: 24

#Lambda in Sorting & Key Functions
#Sorting with sorted()
words = ["apple", "Jackfruit", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(f'words in the list {words} sorter based on number of caracters : {sorted_words}')  # Output: ['apple', 'cherry', 'Jackfruit']

#Sorting a List of Dictionaries
#let's arrange students based on the scores they obtained in ascending order
students = [{"name": "Alice", "score": 90},
            {"name": "Bob", "score": 85},
            {"name": "Charlie", "score": 92}]

sorted_students = sorted(students, key=lambda x: x["score"])
sorted_students_names = [name["name"] for name in sorted_students]
print(f"students sorted based on the scores obtained : {sorted_students_names}")

#Lambda with List Comprehensions
nums = [1, 2, 3, 4, 5]
squared = [(lambda x: x**2)(x) for x in nums]
print(squared)  # Output: [1, 4, 9, 16, 25]



