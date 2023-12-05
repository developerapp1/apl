# Create a string
string = "Hello, World!"

# 1. Accessing characters
print(string[0])  # Output: H
print(string[5])  # Output: o
print(string[-1])  # Output: !

# 2. Slicing
print(string[1:5])  # Output: ello
print(string[6:])  # Output: World!

# 3. Concatenating strings
print("Hello" + " " + "World!")  # Output: Hello World!

# 4. Checking for characters
print("o" in string)  # Output: True
print("z" in string)  # Output: False

# 5. Iterating over characters
for character in string:
    print(character)
