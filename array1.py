import numpy as np

# Create an array
array = np.array([1, 2, 3, 4, 5])

# 1. Accessing elements
print(array[0])  # Output: 1
print(array[2])  # Output: 3

# 2. Slicing
print(array[1:4])  # Output: [2 3 4]

# 3. Modifying elements
array[2] = 10
print(array)  # Output: [1 2 10 4 5]

# 4. Iterating over elements
for element in array:
    print(element)

# 5. Performing operations on elements
print(np.sum(array))  # Output: 25
print(np.min(array))  # Output: 25
print(np.max(array))  # Output: 25
print(np.mean(array))  # Output: 5