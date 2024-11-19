# Step-by-step implementation as described

# Create an empty list
my_list = []

# Append the elements 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

# Insert the value 15 at the second position
my_list.insert(1, 15)

# Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find the index of the value 30
index_of_30 = my_list.index(30)

# Print the index of the value 30
print(my_list, 'The index value of 30 in this list is:', index_of_30)
