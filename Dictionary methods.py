# Creating a sample dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 1️⃣ get() - Get value for a key, return default if key is missing
print(my_dict.get("age"))  # Output: 25
print(my_dict.get("gender", "Not Specified"))  # Output: Not Specified

# 2️⃣ keys() - Get all keys
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# 3️⃣ values() - Get all values
print(my_dict.values())  # Output: dict_values(['Alice', 25, 'New York'])

# 4️⃣ items() - Get all key-value pairs
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# 5️⃣ pop() - Remove and return a value by key
print(my_dict.pop("age"))  # Output: 25
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}

# 6️⃣ popitem() - Remove and return the last key-value pair
print(my_dict.popitem())  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'Alice'}

# 7️⃣ update() - Update dictionary with another dictionary
my_dict.update({"age": 30, "city": "San Francisco"})
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'San Francisco'}

# 8️⃣ clear() - Remove all elements
my_dict.clear()
print(my_dict)  # Output: {}

# 9️⃣ copy() - Create a shallow copy
original_dict = {"a": 1, "b": 2}
copy_dict = original_dict.copy()
print(copy_dict)  # Output: {'a': 1, 'b': 2}

# 🔟 setdefault() - Get value if key exists, otherwise set a default value
copy_dict.setdefault("c", 3)
print(copy_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 1️⃣1️⃣ fromkeys() - Create dictionary from a list of keys with default value
keys = ["x", "y", "z"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'x': 0, 'y': 0, 'z': 0}
