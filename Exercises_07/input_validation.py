"""
Script: input_validation.py
By:Richard Vaughan
Purpose: Code for validating user Input.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 08OCT22
Notes:

"""


# Function to validate user input is an integer.
def validate_integer():
    # Loop forever
    while True:
        try:
            int(input("Enter an integer value: "))
        except:
            # Bad value,
            print(f"Error")
            continue
        else:
            print("Valid input")
            # Good value, exit the loop
            break
        # Finally will always run whether there is an error or not.
        finally:
            # Only runs after the except, continue
            print("Try again - enter an integer value only!")


validate_integer()
