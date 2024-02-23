# This program continuously asks user to enter a number until they type -1
#The inputed numbers are stored in an array called user-inputs
# the program will then calculates the average of the inputed numbers excluding the -1

number=0
user_inputs=[]

while True:
    number = int(input("Please enter a number:"))
    if number == -1:
        break
    else:
        user_inputs.append(number)

print (sum(user_inputs) / len(user_inputs))