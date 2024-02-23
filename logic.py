""" This code asks the customer for their log in details
the customer needs to enter their username and a 10 digit password to excess their account
details. The bank is also offering any customer over the age of 65 a change to win a prize.
If they win, they will get douuble interest rate on their savings"""

username = input("Please enter your username:")
password = int(input("Please enter your 10 digit password:"))

if password == 10:
  print(" ")
  print(f"Hello {username}" , "Welcome to ABC Bank")
  
else:
    print("Invalid password, Try again")
print(" ") 
print("TODAY'S PRIZE DRAW - Double interest rate on your savings if your 65 years and over")
print(" ")
print("Please submit your name and age for a chance to win")

print(" ")
name= input("Please enter your full name:")
age= int(input("Please enter your age for a chance to :"))

if age > 65:
  print(" ")
  print("You have been entered into the draw - Good luck and hope you win")
  
else:
  print("Sorry - you do not qualify, Goodbye")