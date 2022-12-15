"""
Script: tuple_exercise.py
By:Richard Vaughan
Purpose: Script to demonstrate that tuples are immutable
and unlike lists can't be modified using their index.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 24SEP22
Notes:

**** This File Will Run With an Error ****
As Tuples are Immutable you can not change the value like a list.
Line 23 demonstrates this."""

my_list = ["one", "two", "three"]
my_tuple = ("one", "two", "three")
print(type(my_list))
print(type(my_tuple))
# You can comment out line 23 to fix the problem
# Tuples are immutable...
my_tuple[2] = "Four"
