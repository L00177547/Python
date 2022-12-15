"""
Script: diesel_generator_exercise_first_attempt.py
By:Richard Vaughan
Purpose: Calculate the endurance of a diesel generator given fuel in litres
and fuel consumption in litres per minute.  endurance = fil /fcilpm
validate any input of values.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 08OCT22
Notes:

"""

import math


# Function to calculate the endurance of the Diesel Backup Generator.
def endurance(fuel_in_litres: float, fuel_consumption_in_minutes: float):
    # If Fuel consumption is not equal to 0
    if fuel_consumption_in_minutes != 0:
        # calculate endurance and store in variable endurance.
        endurance1 = fuel_in_litres / fuel_consumption_in_minutes
        # If endurance is less than 1 then.
        if endurance1 < 1:
            # Calculate seconds
            endurance_sec = round(endurance1 * 60)
            # Output the results in seconds
            print(f"The endurance of the generator is {endurance_sec} seconds")
        else:
            # Using math.modf to split endurance into a tuple with 2 values
            # and calculate minutes and seconds
            endurance_decimal_split = math.modf(endurance1)
            seconds, minutes = endurance_decimal_split
            endurance_sec_2 = round(seconds * 60)
            endurance_min = round(minutes)
            # output result in minutes and seconds
            print(f"The endurance of the generator is {endurance_min} minutes and {endurance_sec_2} seconds")
    else:
        # If fuel consumption is = 0 then output
        # The generator is idling
        print(" The generator is idling")


# define a function for user input validation using try except else finally.
def user_input_validation():
    while True:
        try:
            # Input fuel remaining in litres and store in variable fil.
            fil = float(input("Please enter the total fuel remaining in litres : "))
        except ValueError:
            # If the input is not a float then print Error.
            print("Error")
            continue
        else:
            # If the input is a float then print Valid input.
            print("Valid input")
            try:
                # Input fuel consumption in litres per minute and store in variable fcim.
                fcim = float(input("Please enter the Fuel consumption in litre per minute : "))
            except ValueError:
                # If the input is not a float then print Error.
                print("Error")
                continue
            else:
                # If the input is a float then print Valid input.
                print("Valid input")

                # Define a function to Calculate Endurance of a diesel generator given
                # Fuel in litres and Fuel consumption in litres per minute.
                # All values input will be floats.

                endurance(fil, fcim)
                break
            finally:
                print("")
            break
        finally:
            print("")


if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")
    # call the function user_input_validation
    user_input_validation()
else:
    print(f"This module is called {__name__} and is being called by another script")
