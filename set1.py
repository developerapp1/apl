# Create a set
set1 = {1, 2, 3, 4, 5}

# 1. Checking for membership
print(2 in set1)  # Output: True
print(6 in set1)  # Output: False

# 2. Adding elements
set1.add(6)
print(set1)  # Output: {1, 2, 3, 4, 5, 6}

# 3. Removing elements
set1.remove(3)
print(set1)  # Output: {1, 2, 4, 5, 6}

# 4. Union of sets
set2 = {3, 4, 5, 6, 7}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5, 6, 7}

# 5. Intersection of sets
print(set1 & set2)  # Output: {4, 5, 6}
