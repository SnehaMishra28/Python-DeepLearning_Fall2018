# Set Work

# A set is created by placing all the items (elements) inside curly braces {}, separated by comma or by using the
# built-in function set().
#
# It can have any number of items and they may be of different types (integer, float, tuple, string etc.).
# But a set cannot have a mutable element, like list, set or dictionary, as its element.

# Symmetric Difference
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#Print out the input set
print("The 1st set is: ")
print(A)
print("The 2nd set is: ")
print(B)
# use ^ operator for the symmetric differences
# Output: {1, 2, 3, 6, 7, 8}
print("The symmetric differences between set A & B is: ")
print(A ^ B)
