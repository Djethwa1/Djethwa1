# Program to calculate a users total holiday cost

# The total holiday includes cost of the flight, car rental and hotel stay

# The user will select the city they want to travel to from an options menu

def options():      # function to define user options
    print("\n")
    print("City Options:")
    print("\n")
    print("1 = LONDON")
    print("2 = TOKYO")
    print("3 = SYDNEY")
    print("4 = JOHANNESBURG")
    print("5 = NEW YORK")
   
options()      # function called and waiting for user selection
print("\n")

# users input of chosen city is converted to uppercase to reflect the options available in the menu

city_flight = input("Please choose the city you would like to travel to: ").upper()

print("\n")

# user inputs number of nights they want to stay in a hotel

num_nights = int(input("Please enter the number of nights you will be staying at a hotel: "))

print("\n")

print("Number of nights in hotel:" , num_nights , "nights")

print("\n")

# user inputs the number of days they want to rent a car for

rental_days = int(input("Please enter the number of days you will be hiring a car: "))

print("\n")

print("Number of days you will be renting a car: " , rental_days , "days")

print("\n")

# Functions to calculate holiday cost 

def plane_cost(city_flight):    # ticket cost depending on which city the user wants to fly to


        if city_flight == "1":
            return 390

        elif city_flight == "2":
            return 785
    
        
        elif city_flight == "3":
            return 660
    

        elif city_flight == "4":
            return 455

        else:
            city_flight == "5"
            return 495
             

def hotel_cost(num_nights):    # Calculates the hotel cost per night that user stays at hotel
    
    price_per_night=150
    return num_nights * price_per_night

def car_rental(rental_days):    # calculates the car rental cost per day that the user hires a car for
    rental_cost_per_day= 60
    return rental_days * rental_cost_per_day


def holiday_cost(num_nights , rental_days , city_flight):   # calculates the total cost of the holiday
   
    hotel = hotel_cost(num_nights)      # cost of hotel stay
    print("Cost of hotel stay is:" , hotel)
    print("\n")
    
    ticket = plane_cost(city_flight)      # cost of flight ticket
    print("Cost of your flight ticket is:" , ticket)
    print("\n")
    
    car = car_rental(rental_days)        # cost of car rental
    print("Cost of your car rental is:" , car)
    print("\n")
    
    total_holiday_cost = hotel + car + ticket # total cost of holiday
    print("\n")
    print("The total cost of your holiday is:" " " "$", total_holiday_cost)

holiday_cost(num_nights, rental_days, city_flight) # funtion called to return total holiday cost