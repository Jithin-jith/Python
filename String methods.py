# Defining a sample string
text = "  Hello, World! Welcome to Python programming.  "

# String Methods Demonstration
print("Original String:", text)

# 1. strip() - Removes leading and trailing spaces
print("strip():", text.strip())

# 2. lower() - Converts to lowercase
print("lower():", text.lower())

# 3. upper() - Converts to uppercase
print("upper():", text.upper())

# 4. title() - Converts to title case
print("title():", text.title())

# 5. capitalize() - Capitalizes the first letter
print("capitalize():", text.capitalize())

# 6. swapcase() - Swaps uppercase to lowercase and vice versa
print("swapcase():", text.swapcase())

# 7. replace() - Replaces a substring
print("replace():", text.replace("World", "Universe"))

# 8. split() - Splits string into a list
print("split():", text.split())

# 9. join() - Joins elements of a list into a string
words = ["Python", "is", "fun"]
print("join():", "-".join(words))

# 10. find() - Finds the position of a substring
print("find():", text.find("Python"))

# 11. index() - Finds the position of a substring (raises error if not found)
print("index():", text.index("Python"))

# 12. count() - Counts occurrences of a substring
print("count():", text.count("o"))

# 13. startswith() - Checks if the string starts with a specific substring
print("startswith():", text.startswith("Hello"))

# 14. endswith() - Checks if the string ends with a specific substring
print("endswith():", text.endswith("programming."))

# 15. isalpha() - Checks if all characters are alphabets
print("isalpha():", "HelloWorld".isalpha())

# 16. isdigit() - Checks if all characters are digits
print("isdigit():", "12345".isdigit())

# 17. isalnum() - Checks if all characters are alphanumeric
print("isalnum():", "Hello123".isalnum())

# 18. isspace() - Checks if string contains only spaces
print("isspace():", "   ".isspace())

# 19. ljust() - Left aligns the string with padding
print("ljust():", text.ljust(50, '-'))

# 20. rjust() - Right aligns the string with padding
print("rjust():", text.rjust(50, '-'))

# 21. center() - Centers the string with padding
print("center():", text.center(50, '-'))