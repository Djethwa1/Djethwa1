# Code to calculate the total stock value in a cafe using Lists and dictionaries

menu_items = ["Chips" , "Sandwich" , "Burger" , "Pies"] #items stocked in cafe

stock_value = {"Chips" : 20 , "Sandwich" : 20 , "Burger" : 35 , "Pies" : 25} #stock value of goods

price_of_goods = {"Chips" : 1.10 , "Sandwich" : 1.95 , "Burger" : 2.24 , "Pies" : 2.50}

total_value = 0  # initial count of goods

for item in menu_items:
    total_value = total_value + stock_value[item] * price_of_goods[item]
    
print("The total stock value of items in cafe is:" , f"{total_value:.2f}") #total with 2 decimal places
