#  Sets are unordered collections of unique elements.
# Let's see some built-in methods to manipulate sets

# Let's create a set
a = set(('a','b',1,2,'a'))
print(a)

a = {'a','b',1,2,'a'}
print(a)

#1. add()
"""Adds an element to the set. If the element already exists, it does nothing."""
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

#2. update()
"""Adds multiple elements from another set, list, tuple, or string."""
s = {1, 2, 3}
s.update([4, 5, 6])
print(s)  # Output: {1, 2, 3, 4, 5, 6}

#3. remove()
"""Removes a specific element from the set. Raises a KeyError if the element is not found."""
s = {1, 2, 3}
s.remove(2)
print(s)  # Output: {1, 3}

#4. discard()
"""Removes a specific element from the set without raising an error if it is not found."""
s = {1, 2, 3}
s.discard(2)
print(s)  # Output: {1, 3}

s.discard(5)  # No error even though 5 is not in the set

#5. pop()
"""Removes and returns a random element from the set."""
s = {1, 2, 3}
element = s.pop()
print(element)  # Output: (Randomly removed element)
print(s)  # Output: Remaining elements

#6. clear()
"""Removes all elements from the set."""
s = {1, 2, 3}
s.clear()
print(s)  # Output: set()

#7. union()
"""Returns a new set containing all elements from both sets."""
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.union(s2)
print(result)  # Output: {1, 2, 3, 4, 5}

#OR using | operator:
result = s1 | s2
print(result)  # Output: {1, 2, 3, 4, 5}

#8. intersection()
"""Returns a new set containing only the common elements."""
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.intersection(s2)
print(result)  # Output: {3}

#OR using & operator:
result = s1 & s2
print(result)  # Output: {3}

#9. difference()
"""Returns a new set containing elements that are in the first set but not in the second."""
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.difference(s2)
print(result)  # Output: {1, 2}

#OR using - operator:
result = s1 - s2
print(result)  # Output: {1, 2}

#10. symmetric_difference()
"""Returns a new set containing elements that are in either set but not in both."""
s1 = {1, 2, 3}
s2 = {3, 4, 5}
result = s1.symmetric_difference(s2)
print(result)  # Output: {1, 2, 4, 5}

#OR using ^ operator:
result = s1 ^ s2
print(result)  # Output: {1, 2, 4, 5}

#11. issubset()
"""Returns True if all elements of the first set are in the second set."""
s1 = {1, 2}
s2 = {1, 2, 3, 4}
print(s1.issubset(s2))  # Output: True

#12. issuperset()
"""Returns True if all elements of the second set are in the first set."""
s1 = {1, 2, 3, 4}
s2 = {1, 2}
print(s1.issuperset(s2))  # Output: True

#13. isdisjoint()
"""Returns True if both sets have no elements in common."""
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))  # Output: True

#14. copy()
"""Creates a shallow copy of the set."""
s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)  # Output: {1, 2, 3}