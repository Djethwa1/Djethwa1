# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #NameError: name 'Lion' is not defined, speech marks missing 
#when  defining the string variable

animal_type = "cub"

number_of_teeth = 16

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth")
# variable was not formated, f-string used to format
# The variables number_of_teeth and animal_type are placed in incorrect part of statement,
# error fixed by interchanging them

print (full_spec) #SyntaxError: Missing parentheses