# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #IndentationError: indentaion in not ment to be there and 
#SyntaxError: Missing parentheses

print ("\n") #IndentationError: indentaion in not ment to be there and 
#SyntaxError: Missing parentheses

# Variables declaring the user's age, casting the str to an int, and printing the result

age_Str = "24 years old" #SyntaxError: indentaion in wrong place and 
#NameError: a runtime error - name 'age_Str' is not defined

age = int(age_Str[0:2]) #SyntaxError: indentaion in wrong place and 
#ValueError- a runtime error - indexing used to extract integer part of string

print("I'm" + " " + str(age) + " " + "years old.") #Syntax error - indentation in wrong place and 
#TypeError - a Runtime error- string and integer cannot be concatenated so age converted to string

# Variables declaring additional years and printing the total years of age

years_from_now = 3 #Syntax error: indentaion in wrong place,
#interger not ment to be within speach marks

total_years = age + years_from_now # Syntax error: indentaion in not ment to be there

print ("The total number of years:" + " " + str(total_years)) #SyntaxError: Missing parentheses and 
#incorrect variable answer_years used instead of total_years and 
#Type error - a runtime error - total_years converted to string

# Variable to calculate the total amount of months from the total amount of years and 
#printing the result

total_months = total_years * 12 + 6 #NameError: syntax error
#The variable name 'total' is an incorrect variable to use - should be 'total_years' and
#6 months has not been included in the total calculation

print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") 
#Syntax Error: Missing parentheses and 
#Type error: a Runtime Error - string and integer cannot be concatenated convert total_months to string
