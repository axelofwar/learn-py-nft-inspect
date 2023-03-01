# For the exercise, look up the methods and functions that are available for use
# with Python lists.

# Lists are one of Python's most powerful data types. A list is a collection
# which is ordered and changeable. In Python lists are written with square
# brackets.

# Lists differ from arrays in that all the items belonging to a list can be of
# different data type.

# Lists differ from tuples in that the items of a list can be changed unlike
# tuples whose elements cannot be changed once assigned.

# Lists differ from dictionaries in that items in a list are ordered, and
# use numbers to access them, while items in a dictionary are unordered, and
# use keys to access them. A disctionary can contain multiple lists and
# dictionaries - a list cannot contain a dictionary.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for item in x:
    print(item * 1000)

# Print the max value of x
# YOUR CODE HERE
print(max(x))

# Print the min value of x
# YOUR CODE HERE
print(min(x))

# Print the average of x
# YOUR CODE HERE
print(sum(x) / len(x))

# Print the sum of x
# YOUR CODE HERE
print(sum(x))

# Print the product of all the numbers in x
# YOUR CODE HERE
product = 1
for item in x:
    product *= item

# Print all values but the first of x
# YOUR CODE HERE
print(x[1:])

# Print all values but the last of x
# YOUR CODE HERE
print(x[:-1])

# Print the middle two values of x
# YOUR CODE HERE
print(x[3:5])
