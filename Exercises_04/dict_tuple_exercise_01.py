"""
Script: dict_tuple_exercise_01.py
By:Richard Vaughan
Purpose: Script to iterate through dictionary items and output a (key,value) tuple pair.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 30SEP22
Notes:

"""

# Create the dictionary can populated with values.
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for a, b in scan.items():
    # Outputs Key and Value correctly.
    print(f"IP address {a} Port {b}")
