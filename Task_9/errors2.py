# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# syntax error - lion is a string hence must in ""
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# logical/synatx error - {} are used without f to produce f-string and variables used in wrong order
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

# syntax error - missing brackets
print(full_spec)

