# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # syntax error - missing brackets
print("\n") # syntax error - unnecessary indent + missing brackets

    # Variables declaring the user's age, casting the str to an int, and printing the result
# syntax error - whole block indented
# syntax error - confusion between 'equal' and assign'; age_Str has not been assigned a value
age_Str = "24 years old" 
# syntax error - cannot format a string into an integer
age = 24
# not necessarily an error but don't need to use age variable, can just use age_Str
print("I'm " + age_Str)

    # Variables declaring additional years and printing the total years of age
# syntax error - whole block indented
years_from_now = "3"
# syntax error - cannot concatenate string and integer
total_years = age + int(years_from_now)
# syntax error - missing brackets
# syntax error - incorrect variable entered, in an incorrect manner
print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
# syntax error - appropiate variable not entered 
total_months = (total_years * 12) + 6
# syntax error - mising brackets
# syntax error - cannot concatenate string and integer
# logical error - 6 months not added to total months
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

#HINT, 330 months is the correct answer

