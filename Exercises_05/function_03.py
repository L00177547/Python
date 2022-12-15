def calculate_circumference(radius=1):
    """
    Calculate the circumference of a circle based on its radius
    """
    return 2 * 3.142 * radius


# Missing radius value causes error.
a = calculate_circumference()
print(a)
