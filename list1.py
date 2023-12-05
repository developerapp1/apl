# Create a list
list1 = [1, 2, 30, 4, 5, 'omkar']

# 1. Accessing elements
print(list1[0])  # Output: 1
print(list1[2])  # Output: 3

# 2. Adding elements
list1.append(6)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# 3. Removing elements
list1.remove('omkar')
print(list1)  # Output: [1, 3, 4, 5, 6]

# 4. Reversing elements
list1.reverse()
print(list1)  # Output: [6, 5, 4, 3, 1]

# 5. Sorting elements
list1.sort()
print(list1)  # Output: [1, 3, 4, 5, 6]
