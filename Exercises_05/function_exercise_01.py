"""
Script: function_exercise_01.py
By:Richard Vaughan
Purpose: Script to create a function that will Calculate Modulus of 2 integers and return a boolean value
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 30SEP22
Notes:

"""


# Create the function called divisible
# where numerator and denominator are to expect integer values
# and the function returns a boolean value.
def divisible(numerator: int, denominator: int) -> bool:
    """Calculate Modulus of 2 integers and return a boolean value"""
    return numerator % denominator == 0


# Output a boolean Value (in this case it will be True)
print(divisible(30, 6))
