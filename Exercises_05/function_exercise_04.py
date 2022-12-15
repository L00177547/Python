"""
Script: function_exercise_04.py
By:Richard Vaughan
Purpose: Script to create a function that will interrogate a list for a particular integer number
and return a boolean value of True if it exists and False if it Does not.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 30SEP22
Notes:

"""


# Create the function called find_num that will expect a list of integer numbers passed
# and will return a boolean value.
def find_num(number_list: list, number: int) -> bool:
    # For every number in the list.
    for iterate_number in number_list:
        # If the number exists in the list then return boolean true.
        if iterate_number == number:
            return True
    # Else Return False
    else:
        return False


result = find_num([1, 2, 3, 4, 5, 6, 7, 8, ], 9)
print(result)
