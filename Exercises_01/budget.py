# Calculations to show funds available this Semester.
weeks_in_year = 52
academic_semester_in_weeks = 18
net_household_annual_salary = 45000
annual_travel_and_subs_allow = 10000
# Calculate Annual Net Income.
annual_income = net_household_annual_salary + annual_travel_and_subs_allow
# Convert Net Annual Income to Semester Income.
semester_income = round((annual_income / weeks_in_year) * academic_semester_in_weeks, 2)
annual_mortgage_cost = 11000
annual_house_insurance = 700
annual_heating_costs = 4000
annual_energy_cost = 3000
annual_motor_tax = 200
annual_motor_insurance = 480
current_weekly_motor_fuel_cost = 80
# Convert Weekly Motor Fuel to Annual.
annual_motor_fuel_cost = current_weekly_motor_fuel_cost * weeks_in_year
annual_motor_maintenance = 400
current_weekly_grocery_shopping = 90
# Convert Weekly Shopping to Annual.
annual_grocery_shopping = current_weekly_grocery_shopping * weeks_in_year
annual_mortgage_life_insurance = 3000
annual_health_insurance = 2500
# Calculate Total Annual Expenditure.
total_annual_expenditure = annual_energy_cost \
                           + annual_grocery_shopping \
                           + annual_health_insurance \
                           + annual_heating_costs \
                           + annual_house_insurance \
                           + annual_mortgage_cost \
                           + annual_mortgage_life_insurance \
                           + annual_motor_fuel_cost \
                           + annual_motor_insurance \
                           + annual_motor_maintenance \
                           + annual_motor_tax
# Calculate Total Semester Expenditure.
semester_expenditure = round((total_annual_expenditure / weeks_in_year) * academic_semester_in_weeks, 2)
# Output Semester Income & Expenditure on Next 2 lines of code.
print(f"Your Semester Income will be approximately €{semester_income}")
print(f"Your Semester Expenditure will be approximately €{semester_expenditure}")
# Calculate Semester Funds Available.
funds_available_for_semester = round(semester_income - semester_expenditure, 2)
# Output Available Funds this Semester
print(f"Your available funds for this semester are approximately €{funds_available_for_semester}")
