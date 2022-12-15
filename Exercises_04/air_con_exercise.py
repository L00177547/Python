"""
Script: air_con_exercise.py
By:Richard Vaughan
Purpose:An American air conditioner system is returning temperatures in
Kelvin. From a list of 10 values in degrees Kelvin calculate and print these values in
Celsius and Fahrenheit.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 30SEP22
Notes:

"""
# List of temperatures in Kelvin from AC
list_of_temps_in_kelvin = ["295.50", "300.25", "280.75", "294.66", "275.33", "295.00", "290.00", "285.75", "290.66",
                           "275.33"]
# For Loop
for temp_value in list_of_temps_in_kelvin:
    # Calculate degrees celsius.
    temp_celsius = round(float(temp_value) - 273.15, 2)
    # Calculate degrees fahrenheit.
    temp_fahrenheit = round((float(temp_celsius) * 9 / 5) + 32, 2)
    # Output list of kelvin temps in celsius and fahrenheit.
    print(f"{temp_value} Kelvin is Equal to {temp_celsius} Celsius which is equal to {temp_fahrenheit} Fahrenheit")
