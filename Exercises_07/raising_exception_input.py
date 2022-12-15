"""
Script: raising_exception_input.py
By:Richard Vaughan
Purpose: demonstrate raising an exception to incorrect input.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 08OCT22
Notes:

"""
# Take an input number as a string and convert it to an integer
my_value = int(input("Enter an integer greater than 0 :"))
if my_value <= 0:
    raise Exception("Values must be > 0")
else:
    print("Validation checks passed")
