# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
 
name = "Tim"
# indenting error
    # surname = " Jones"
surname = " Jones"
age = 21

# 'is' is used as an operation, not string
# cannot concatenate strings and integers 
# full_message = name + surname +  is  + age + " years old"
full_message = (name + surname +  " is "  + str(age) + " years old")
# spacing error between 'is' and age
print (full_message)