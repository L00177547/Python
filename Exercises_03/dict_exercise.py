"""
Script: dict_exercise.py
By:Richard Vaughan
Purpose: Script to demonstrate the keys, values and items methods that can be used with dictionaries.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 24SEP22
Notes:

"""

my_dictionary = {"FName": "Richard", "SName": "Vaughan", "Occupation": "Student"}
print(my_dictionary)
my_dictionary["Salary"] = "Not Enough!"
print(my_dictionary)
# Output dictionary key names only using the .keys method.
print (my_dictionary.keys())
# Output dictionary values only using the .values method.
print (my_dictionary.values())
# Output dictionary items using the .items method.
print (my_dictionary.items())

