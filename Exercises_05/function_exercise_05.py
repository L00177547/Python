"""
Script: function_exercise_05.py
By:Richard Vaughan
Purpose: Script to create a function that will interrogate a list for even integer numbers
and return a boolean value of True if it exists and False if it Does not.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 30SEP22
Notes:

"""


# Create the function called find_num that will expect a list passed to the function.
def find_num(number_list: list):
    # For every number in the list.
    for iterate_number in number_list:
        iterate_number_2 = (iterate_number % 2 == 0)
        # If the number in the list is an even number output message true and return boolean True.
        if iterate_number_2 is True:
            print(f"It is True the Number {iterate_number} from the list is even")
            return True
        # else boolean value is False and output message false.
        else:
            print(f"It is False the Number {iterate_number} from the list is even")
    # If no numbers are even return False.
    return False


# list of numbers for function.
find_num([1, 6, 3, 8, 5, 12, 7, 16, 9, 20])
