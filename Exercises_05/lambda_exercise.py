"""
Script: lambda_exercise.py
By:Richard Vaughan
Purpose: Script to create a lambda function to calculate the volume of a cylinder
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 30SEP22
Notes:

"""
# lambda function to calculate the volume of a cylinder
volume_of_cylinder = lambda height, radius: 3.142 * (radius * radius) * height
# Input the Height as float.
height = float(input("Please enter the Height of the Cylinder :"))
# Input the Radius as float.
radius = float(input("Please enter the Radius of the Cylinder :"))
# Output result of function
print(f"The Volume of the Cylinder is {volume_of_cylinder(height, radius)}")
