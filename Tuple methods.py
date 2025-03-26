# Python Tuple Methods and Functions with Examples

# Creating a tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (10, 20, 30, 40, 50)

# Accessing elements
element = tuple1[1]  # Accessing second element (indexing starts from 0)
print("Element at index 1:", element)

# Slicing a tuple
slice_tuple = tuple1[1:4]  # Returns (2, 3, 4)
print("Sliced tuple:", slice_tuple)

# Length of tuple
length = len(tuple1)
print("Length of tuple1:", length)

# Concatenation of tuples
concat_tuple = tuple1 + tuple2
print("Concatenated tuple:", concat_tuple)

# Repeating tuples
repeat_tuple = tuple2 * 3  # Repeats ('a', 'b', 'c') three times
print("Repeated tuple:", repeat_tuple)

# Checking element existence
is_present = 3 in tuple1  # Returns True
print("Is 3 in tuple1?", is_present)

# Counting occurrences of an element
count = tuple1.count(2)  # Returns number of times 2 appears in tuple1
print("Count of 2 in tuple1:", count)

# Finding index of an element
index = tuple3.index(30)  # Returns index of first occurrence of 30
print("Index of 30 in tuple3:", index)

# Iterating through a tuple
print("Iterating through tuple1:")
for item in tuple1:
    print(item)

# Tuple unpacking
a, b, c, d, e = tuple1
print("Unpacked values:", a, b, c, d, e)

# Using tuples in functions
def return_multiple():
    return ("Hello", 42, 3.14)

tuple_returned = return_multiple()
print("Returned tuple:", tuple_returned)

# Converting a list to a tuple
list1 = [1, 2, 3, 4]
tuple_from_list = tuple(list1)
print("Tuple from list:", tuple_from_list)

# Converting a string to a tuple
tuple_from_string = tuple("hello")
print("Tuple from string:", tuple_from_string)

# Finding the max and min values in a tuple
max_value = max(tuple3)  # Returns maximum value
min_value = min(tuple3)  # Returns minimum value
print("Max value in tuple3:", max_value)
print("Min value in tuple3:", min_value)

# Sum of tuple elements
sum_values = sum(tuple3)
print("Sum of tuple3:", sum_values)

# Sorting a tuple (returns a sorted list)
sorted_tuple = sorted(tuple3)
print("Sorted tuple (as list):", sorted_tuple)

# Using tuple with zip function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zip_tuple = tuple(zip(list1, list2))  # Returns ((1, 'a'), (2, 'b'), (3, 'c'))
print("Zipped tuple:", zip_tuple)

# Deleting a tuple
del tuple1  # Tuples are immutable, so we delete the reference
# print(tuple1)  # This will raise an error as tuple1 is deleted
