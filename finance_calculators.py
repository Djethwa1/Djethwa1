'''This code asks user to choose an option to calculate the interest
(compound or simple) obtained from an investent or the amount of repayment from a loan.
The code will automatically convert the user's chosen option to lowercase.
The user will ask for user input of some values that will be used in the calculations
and then output either the interest or repayment amount rounded to two decimal places
based on the user's chosen option'''

import math

choosen_option =  '''
   Investment - to calculate the amount of interest you'll earn on your investment\n

   Bond - to calculate the amount you will have to pay on a home loan\n

    Please select either Investment or Bond from the menu above:
'''
    
selection=input(choosen_option)
selection=selection.lower()

if selection == "investment":
       
    investment_amount=int(input("Please enter amount of money you are depositing:"))
    print("Amount deposited:" ,investment_amount)

    interest_rate=float(input("Please enter the investment rate of interest:"))
    print("Interest rate:" ,interest_rate)

    invest_time=int(input("How many years do you want to invest for:"))
    print("Investment duration in years:",invest_time)

    interest_type=input("What type of interest do you want, simple or compound:")

    interest_type=interest_type.lower()

    print("Type of investment:" ,interest_type)

  
    if interest_type == "compound":

                total_amount=investment_amount * math.pow((1 + interest_rate/100), invest_time)

                compound_interest=total_amount - investment_amount

                print(f"Compound interest is: £ {compound_interest:.2f}")
    
    elif interest_type == "simple":
            
                simple_interest=simple_interest=(investment_amount * invest_time * interest_rate) / 100

                print(f"Simple interest is: £ {simple_interest:.2f}")

    else:
            print("Invalid option selected, please enter a valid option")

            

elif selection == "bond":
    

            house_value=int(input("Please enter value of the house:"))

            print("Value of house is", house_value)

            loan_interest_rate=int(input("Please enter the loan interest rate:"))

            monthly_loan_interest_rate = (loan_interest_rate/100)/12

            print("Monthly repayment interest is:", monthly_loan_interest_rate)

            repayment_time=int(input("In how many months do you plan to repay the loan:"))

            print("Time in months to repay loan:", repayment_time)

            repayment_amount= (monthly_loan_interest_rate * house_value)/(1 - (1 + monthly_loan_interest_rate)**(-repayment_time))

            print(f"Amount to repay per month is: £ {repayment_amount:.2f}")

else:
     print("Invalid option selected, please enter a valid option")