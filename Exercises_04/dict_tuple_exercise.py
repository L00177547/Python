"""
Script: dict_tuple_exercise.py
By:Richard Vaughan
Purpose: Script to iterate through a dictionary.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 30SEP22
Notes:

"""
# Store data of the type dictionary in the variable scan.
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}

# for a+b in scan:  (Produces an error)
for a in scan: # only iterates the key
    # Only the Dictionary Key name is output Dictionary value is missing
    print(a)
