"""
Script: oo2.py
By:Richard Vaughan
Purpose: Class Template
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 08OCT22
Notes:
"""


class MyTemplate:
    class_object_attribute1 = 12345
    class_object_attribute2 = 678910

    # semi_major_axis = 6378137
    # semi_minor_axis = 6356752

    # Constructor, called whenever an instance of the class is created.
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        # Take in an argument and assign it to a meaningful attribute name
        self.attr1 = attribute1
        self.attr2 = attribute2

    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")

    def my_method2(self, my_name: str):
        # self.attr2  = False
        print(self.attr2)
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")


# Instantiate the class( Manual testing)
my_object = MyTemplate("Richard", True)
# print(my_object.semi_major_axis, my_object.semi_minor_axis)
print(my_object.class_object_attribute1, my_object.class_object_attribute2)

# Check the object and type
print(type(my_object))
# The following lines print(type()) are for learning purposes
print("Check object attr1 type")
print(type(my_object.attr1))
print("Check object class_object_attribute1 type")
print(type(my_object.class_object_attribute1))
print("Check object attr1 type")
print(type(my_object.attr2))
print("Check object class_object_attribute1 type")
print(type(my_object.class_object_attribute1))
my_object.my_method1()
my_object.my_method2("Giovanni")
