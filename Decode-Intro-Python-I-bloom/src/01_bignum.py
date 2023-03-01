# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
print(2**65536)

# OTHER MATHEMATICAL OPERATIONS
print(2+2)
print(2-2)
print(2*2)
print(2/2)
print(2 % 2)
print(2**2)
print(2//2)
# q: what is the difference between // and /?
# a: // is floor division, / is regular division
# q: what is the difference between % and **?
# a: % is modulus, ** is exponentiation
# q: what is modulus?
# a: modulus is the remainder of a division operation
'''
Lesson 2: Numbers
Numbers are the most basic data type in Python. They can be integers, floats, or complex numbers. They are defined as int, float, and complex class in Python.
You can define an integer, a floating point number and a complex number as follows −
var1 = 1
var2 = 10.5
var3 = 1+2j
To verify the type of any object in Python, use the type() function. This function will also tell you the class a variable or a value belongs to. The isinstance() function is used to check if an object belongs to a particular class.
>>> a = 5
>>> print(type(a))
<class 'int'>
>>> b = 2.0
>>> print(type(b))
<class 'float'>
>>> c = 1 + 2j
>>> print(type(c))
<class 'complex'>
>>> print(isinstance(a, int))
True
>>> print(isinstance(b, float))
True
>>> print(isinstance(c, complex))
True

We can also do some cool math without needing to use numpy:
>>> a = 21
>>> b = 10
>>> c = 0
>>> c = a + b
>>> print("Line 1 - Value of c is ", c)
Line 1 - Value of c is  31
>>> c = a - b
>>> print("Line 2 - Value of c is ", c)
Line 2 - Value of c is  11
>>> c = a * b
>>> print("Line 3 - Value of c is ", c)
Line 3 - Value of c is  210

>>> c = a / b
>>> print("Line 4 - Value of c is ", c)
Line 4 - Value of c is  2.1
>>> c = a % b
>>> print("Line 5 - Value of c is ", c)
Line 5 - Value of c is  1
>>> a = 2
>>> b = 3
>>> c = a**b
>>> print("Line 6 - Value of c is ", c)
Line 6 - Value of c is  8
>>> a = 10
>>> b = 5
>>> c = a//b
>>> print("Line 7 - Value of c is ", c)
Line 7 - Value of c is  2

'''
