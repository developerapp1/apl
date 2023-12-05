# Create a dictionary
dictionary = {
    "name": "Alice",
    "age": 32,
    "city": "New York"
}

# 1. Accessing elements
print(dictionary["name"])  # Output: Alice
print(dictionary["age"])  # Output: 32
print(dictionary["city"])  # Output: New York

# 2. Adding elements
dictionary["occupation"] = "Software Engineer"
print(dictionary)  # Output: {'name': 'Alice', 'age': 32, 'city': 'New York', 'occupation': 'Software Engineer'}

# 3. Removing elements
del dictionary["occupation"]
print(dictionary)  # Output: {'name': 'Alice', 'age': 32, 'city': 'New York'}

# 4. Checking for keys
print("name" in dictionary)  # Output: True
print("occupation" in dictionary)  # Output: False

# 5. Iterating over key-value pairs
for key, value in dictionary.items():
    print(f"{key}: {value}")