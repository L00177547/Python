"""
Script: oo1.py
By:Richard Vaughan
Purpose: Simple Class by Richard Vaughan
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 08OCT22
Notes:

"""
"""
Simple Class by Richard Vaughan
"""


# Create a class
class RichardVaughanClass:

    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for RichardVaughanClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(f"Well {self.message}")


my_class1 = RichardVaughanClass("Good Morning Richard")
my_class1.my_method()
print("Object is of type:")
print(type(my_class1))
print(id(my_class1))

my_class2 = RichardVaughanClass("Good Morning JOR")
my_class2.my_method()
print("Object is of type:")
print(type(my_class2))
print(id(my_class2))
