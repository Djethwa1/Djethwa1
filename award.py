'''This program requests user input of times taken to complete each traithlon event
The program then calculates the total time taken to complete the triathlon
Finally the program will determine the award the contestant will get
based on the time taken to complete the event'''
run_time=int(input("Please enter time in minutes taken to complete running event:"))
cycle_time=int(input("Please enter time in minutes taken to complete cycling event:"))
swim_time=int(input("Please enter time in minutes taken to complete swimming event:"))
total_time=run_time + cycle_time + swim_time
print("Total time taken to complete triathlon:" ,total_time , "minutes")
if total_time <=100:
    print("Awarded Provincial colours")
elif total_time >=101 and total_time <=105:
    print("Awarded Provincial Half colours")
elif total_time >=106 and total_time <=110:
    print("Awarded Provincial scroll")
else:
    print("No award")