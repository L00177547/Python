"""
Script: lists_exercise.py
By:Richard Vaughan
Purpose: Script to experiment with methods associated with lists.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 24SEP22
Notes:

"""


# Create List of Colours.
colours = ["red", "blue", "orange", "blue", "white", "black", "red", "blue"]
# Output the number of times red is used.
print(colours.count("red"))
# Output the position of the colour orange.
print(colours.index("orange"))
# Output the next position of the colour blue after position 4.
print(colours.index("blue", 4))
# Reverse the colours.
colours.reverse()
# Now output the reversed colours.
print(colours)
# Reverse the colours back to their original.
colours.reverse()
# Now output the reversed colours again.
print(colours)
# Append the colour purple to the list.
colours.append("purple")
# Now print the updated list.
print(colours)
# Sorted colour list.
colours.sort()
# Output colour list.
print(colours)
# Create a second list of colours.
colours_2 = ["pink", "green"]
# Extend list of colours with the colours_2 list.
colours.extend(colours_2)
# Output the extended colours list.
print(colours)
# Insert the colour yellow at position 1.
colours.insert(1, "yellow")
# Output new list containing yellow at position 1.
print(colours)
# Remove first red from the colours list.
colours.remove("red")
# Output list with first red removed.
print(colours)
# Remove the item at position 7 from the list.
colours.pop(7)
# Output the updated list with item 7 removed.
print(colours)
# Return a shallow copy of the colours list.
colours.copy()
# Output colours list.
print(colours)
# Clear the colours list.
colours.clear()
# Output cleared colours list.
print(colours)
