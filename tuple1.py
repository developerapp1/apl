# Create a tuple
tuple1 = (1, 2, 3, 4, 5)

# 1. Accessing elements
print(tuple1[0])  # Output: 1
print(tuple1[2])  # Output: 3
print(tuple1[-1])  # Output: 5

# 2. Slicing
print(tuple1[1:4])  # Output: (2, 3, 4)
print(tuple1[3:])  # Output: (4, 5)

# 3. Concatenating tuples
print((1, 2, 3) + (4, 5))  # Output: (1, 2, 3, 4, 5)

# 4. Checking for membership
print(2 in tuple1)  # Output: True
print(6 in tuple1)  # Output: False

# 5. Iterating over elements
for element in tuple1:
    print(element)
