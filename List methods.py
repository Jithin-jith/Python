#Here is a comprehensive list of Python list methods

#1. append - Adds an item to the end of the list.
lst = [1, 2, 3]
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]

#2. extend - Extends the list by appending elements from the given iterable (e.g., another list, tuple, or string).
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # Output: [1, 2, 3, 4, 5]

#3. insert - Inserts an item at a given position index.
lst = [1, 2, 4]
lst.insert(2, 3)  # Inserts 3 at index 2
print(lst)  # Output: [1, 2, 3, 4]

#4. remove - Removes the first occurrence of a value.
lst = [1, 2, 3, 2, 4]
lst.remove(2)  # Removes the first occurrence of 2
print(lst)  # Output: [1, 3, 2, 4]

#5. pop - Removes and returns the item at the given index. If no index is specified, removes and returns the last item.
lst = [1, 2, 3, 4]
print(lst.pop(2))  # Output: 3
print(lst)  # Output: [1, 2, 4]

print(lst.pop())  # Removes and returns the last element (4)
print(lst)  # Output: [1, 2]

#6. clear - Removes all elements from the list
lst = [1, 2, 3]
lst.clear()
print(lst)  # Output: []

#7. index(x, [start, end]) - Returns the index of the first occurrence of x. Optional start and end arguments specify a search range.
lst = [1, 2, 3, 2, 4]
print(lst.index(2))  # Output: 1
print(lst.index(2, 2))  # Output: 3 (searching from index 2 onwards)

#8. count - Returns the number of occurrences of x in the list.
lst = [1, 2, 3, 2, 4, 2]
print(lst.count(2))  # Output: 3

#9. sort(key=None, reverse=False) - Sorts the list in ascending order by default. You can provide a key function for custom sorting and set reverse=True for descending order.
lst = [3, 1, 4, 2]
lst.sort()
print(lst)  # Output: [1, 2, 3, 4]

lst.sort(reverse=True)
print(lst)  # Output: [4, 3, 2, 1]

# Sorting with a key (sorting by absolute values)
lst = [-3, 1, -4, 2]
lst.sort(key=abs)
print(lst)  # Output: [1, 2, -3, -4]

#10. reverse() - Reverses the elements of the list in place.
lst = [1, 2, 3, 4]
lst.reverse()
print(lst)  # Output: [4, 3, 2, 1]

#11. copy() - Returns a shallow copy of the list.
lst = [1, 2, 3]
copy_lst = lst.copy()
print(copy_lst)  # Output: [1, 2, 3]