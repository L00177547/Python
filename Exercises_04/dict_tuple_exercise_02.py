"""
Script: dict_tuple_exercise_02.py
By:Richard Vaughan
Purpose: Sample Script to iterate through items in a dictionary and output (key,value) tuple pair.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 30SEP22
Notes:

"""
# Create the dictionary scan and populate with values.
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
    # Outputs Key and Value correctly.
    print(f"Found a service on {ipv4} at {port}")
