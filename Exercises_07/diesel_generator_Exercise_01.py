"""
Script: diesel_generator_exercise_01.py
By:Richard Vaughan
Purpose: call user_input_validation function from module diesel_generator_exercise_first_attempt.py
to calculate the endurance of a diesel generator.
Prerequisites: None.
Tested: On python 3.10 on Windows 11.

Revision history:
Alpha Version: 08OCT22
Notes:

"""
# import module diesel_generator_exercise.
import diesel_generator_exercise_first_attempt

if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")
# Call diesel_generator_exercise.user_input_validation
diesel_generator_exercise_first_attempt.user_input_validation()
