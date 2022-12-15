"""
Script: diesel_generator_exercise.py
By:Richard Vaughan
Purpose: Calculate the endurance in minutes and seconds of a diesel generator given fuel in litres
and fuel consumption in litres per minute.  endurance = fil /fcilpm
validate any input of values.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 08OCT22
Release 2: 15DEC222
Notes:

"""

# import module math.
import math
import logging

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

# create logging formatter
logFormatter = logging.Formatter(fmt=' %(name)s :: %(levelname)s :: %(message)s')
consoleHandler.setFormatter(logFormatter)

# Add console handler to logger
logger.addHandler(consoleHandler)


# Function to calculate the endurance of the Diesel Backup Generator.
def endurance(fuel_in_litres: float, fuel_consumption_rate: float):
    try:
        return fuel_in_litres / fuel_consumption_rate
    except ZeroDivisionError:
        logger.error('Zero division, setting endurance to zero')
        return 0


# Define a function for user input validation using try except else finally.
def user_input_validation():
    correct_input = False
    # Repeat input of fil and fcim until correct input format
    while not correct_input:
        try:
            # Input fuel remaining in litres and store in variable fil.
            fil = float(input("Please enter the total fuel remaining in litres : "))
        except ValueError:
            # If the input is not able to be converted to a float then print Error.
            logger.error("Error with fuel remaining input")
            correct_input = False
        else:
            # Repeat input of fcim until correct input format
            while not correct_input:
                try:
                    fcim = float(input("Please enter the Fuel consumption in litre per minute : "))
                except ValueError:
                    # If the input is not able to be converted to a float then print Error.
                    logger.error("Error with fuel consumption rate input")
                    correct_input = False
                else:
                    correct_input = True
                    mins_remaining = endurance(fil, fcim)
                    if mins_remaining == 0:
                        logger.info("The diesel backup generator is idling")

                    elif mins_remaining < 1:
                        # Calculate seconds
                        endurance_sec = round(mins_remaining * 60)
                        # Output the results in seconds
                        logger.info(f"The endurance of the generator is {endurance_sec} seconds")
                    else:
                        # Using math.modf to split endurance into a tuple with 2 values
                        # and calculate minutes and seconds
                        endurance_decimal_split = math.modf(mins_remaining)
                        seconds, minutes = endurance_decimal_split
                        endurance_sec_2 = round(seconds * 60)
                        endurance_min = round(minutes)
                        # Output result in minutes and seconds
                        logger.info(f"The endurance of the generator is {endurance_min} minutes and"
                              f" {endurance_sec_2} seconds")
                finally:
                    log.info("Calculation Completed")


if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")
    # call the function user_input_validation
    user_input_validation()
else:
    print(f"This module is called {__name__} and is being called by another script")
