# Tell the function calculate_circumference I'm
# Passing a float and expecting a float returned.
def calculate_circumference(radius: float) -> float:
    """
    Calculate the circumference of a circle based on its radius
    """
    return 2 * 3.142 * radius


# Get a radius value as a string
r = float(input("Provide a radius value: "))
# Call the function and create the variable for the return value
a = calculate_circumference(r)
print(a)
