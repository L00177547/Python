"""
Script: class_template.py
By:Richard Vaughan
Purpose: Class Template for reuse - Name Slasses using Camelcase.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 08OCT22
Notes:
"""


# Create a class called ClassTemplate.
class ClassTemplate():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, template):
        # Print Class Template
        print("Class Template")
        # Create attributes and set initial values
        self.template = template

    # Class Method Template
    def my_method_template(self):
        a = 1
        b = 2
        c = a + b
        print(c)
        print(self.template)


# Create an instance of the Class
my_class_template = ClassTemplate("Template")
# Call the method of the class.
my_class_template.my_method_template()
# print the instance type
print(type(my_class_template))
# Further testing
print("test")

if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")

else:
    print(f"This module is called {__name__} and is being called by another script")
