age=int(input("Please enter your age:"))
if age == 21:
    print("Congrats on your 21st!")
elif age >100:
    print("Sorry, you're dead")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill")
elif age <13:
    print("You qualify for kiddie discount")
else:
    print("Age is but a number")