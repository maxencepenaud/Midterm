# Example of string immutability
my_string = "My name is Maxence"
print("Original string:", my_string)

# Attempt to modify the string
try:
    my_string[1] = "a"  # This will raise an error
except TypeError as e:
    print("Error:", e)

# Correct way to "modify" a string by creating a new one
my_string = my_string.replace("e", "a")
print("New string:", my_string)



# Example of list mutability
my_list = [1, 2, 3]
print("Original list:", my_list)

# Modify an element
my_list[1] = 13
print("Modified list:", my_list)

# Add an element
my_list.append(4)
print("List after adding an element:", my_list)

# Remove an element
my_list.remove(13)
print("List after removing an element:", my_list)

