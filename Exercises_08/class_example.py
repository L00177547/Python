"""
Script: class_example.py
By:Richard Vaughan
Purpose: Simple Class - by convention, use camel case to name classes
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 08OCT22
Notes:
"""


# Create a class
class RVzClass():

    # Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting):
        print("Running constructor for RVzClass")
        # Create attributes and set initial values
        self.message = my_greeting

    def my_method(self):
        print(self.message)


my_class1 = RVzClass("Morning Richard")
my_class1.my_method()
print("test")
print(type(my_class1))

if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")

else:
    print(f"This module is called {__name__} and is being called by another script")
