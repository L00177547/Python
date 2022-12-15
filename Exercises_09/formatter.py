"""
Script: formatter.py
By:Richard Vaughan
Purpose: Code written for the purpose of testing using unittest.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 16OCT22
Notes:
"""


def convert_upper(my_text):
    return my_text.upper()


def convert_lower(my_text):
    return my_text.lower()


def convert_capital(my_text):
    return my_text.capitalize()


print(convert_lower("John ORaw"))
print(convert_upper("John ORaw"))
print(convert_capital("dUBLIN"))
