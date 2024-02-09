'''This code will request user input of 3 integers to perform some calculations
the user input is converted to interger format before performing any calculations'''
x= input ("Please enter a number:")
y= input ("Please enter a second number:")
z= input ("Please enter a third number:")
a=int(x)
b=int(y)
c=int(z)
sum_of_integers= a + b + c
subtraction= a - b
multiply= c * a
print("The sum of integers is:" , sum_of_integers)
print("First number minus Second number:" , subtraction)
print("Multiplication of third number with first number is: " , multiply)
print("Sum of integers divided by third integer is:" , sum_of_integers/c)