"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

'''
modules are files that contain python code. they are used to organize code and
make it easier to reuse. modules can be imported into other modules or into the
interactive interpreter. modules can also be imported from the standard library
or from other people's code. modules can be imported using the import keyword.
'''

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
import os
import sys
print("SYS ARGV: ", sys.argv)
for item in sys.argv:
    print(item)

# Print out the OS platform you're using:
# YOUR CODE HERE
print("OS Platform: ", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python Version: ", sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Current Process ID: ", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current Working Directory: ", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("Machine Login Name: ", os.getlogin())
