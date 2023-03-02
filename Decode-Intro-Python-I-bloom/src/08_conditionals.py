'''
Python has a number of conditional statements that allow your code to
execute under different conditions. Research how to use the `if`,
`elif`, and `else` statements in Python. 

Using if and else, and its variations, we can tell our code to do different things
depending on the value of a variable, the state of a program or user input, etc.

There are also try and except statements that allow us to handle specific use cases
and errors associated with them in our code. Use try and except statements when we
want our code to attempt to execute a block of code, but we want to handle a specific
error if it occurrs or do something else in the case that the block can't be executed.
'''

# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(2))  # True
print(is_even(3))  # False

# We can also take input in python code from a user in the terminal in the form of a string.
# Then that input can be used to do something in our code. For example, we can ask a user
# for a number and then print out whether that number is even or odd.

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the inputted number is even. Otherwise print "Odd"
print("Even!" if is_even(num) else "Odd")  # in-line if-else statement

# Write a function that tries to tell if an inpur is even or odd
# and returns a string that says "Even!" or "Odd!" depending on the input.
# Or returns "Invalid input" if the input is not a number.

# YOUR CODE HERE


def is_even_or_odd(num):
    try:
        if is_even(num):
            return "Even!"
        else:
            return "Odd!"
    except ValueError:
        return "Invalid input"
    except:
        return "Input must be a number"


is_even_or_odd(num)

# We can pass a specific error type to the except statement to handle a specific error.
# For example, we can handle a ValueError if the user inputs a string that can't be
# converted to an integer. Or we can pass a generic error type to the except statement
# to handle any error that occurs in the try block.
