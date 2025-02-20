import os

#1. Writing to a File

with open("example.txt", "w") as file:
    file.write("Hello, this is an example file.\n")
    file.write("This is the second line.\n")
print("File written successfully!")

#2. Reading from a File
#Let's reads and prints the content of "example.txt".

with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

#3. Appending to a File
# Let's adds new content to the existing "example.txt".

with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")
print("Text appended successfully!")

#4. Reading a File Line by Line
# Let's reads "example.txt" line by line.

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes extra newlines
    file.close()

#5. Using seek() to Read from a Specific Position.
#Let's reads the first 10 characters from "example.txt".

with open("example.txt", "r") as file:
    file.seek(0)  # Move to the beginning of the file
    print("First 10 characters:", file.read(11))
    file.close()

#6. Checking if a File Exists Before Reading

if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        print("File exists. Reading content:")
        print(file.read())
else:
    print("File does not exist!")
    
#7. Deleting a File

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted successfully!")
else:
    print("File not found!")

