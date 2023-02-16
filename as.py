#! /usr/bin/env python3

from datetime import date, time, datetime

#display message
print("Arrival Time Estimator")
print()

#init vars
continue_var = "y"

#y/n var controller
while continue_var == "y":

    
#get user data
        dep_date_str = input("Estimated date of departure (YYYY-MM-DD):\t ")
        dep_time_str = input("Estimated time of departure (HH:MM AM/PM):\t ")
        miles = int(input(f"Enter miles:\t "))
        miles_per_hr = int(input("Enter miles per hour:\t "))
        print()
        
        dep_str= dep_date_str + " " + dep_time_str
        dep_datetime = datetime.strptime(dep_str, "%Y-%m-%d %I:%M %p")
        hours = round(miles / miles_per_hr, 1)
        
        print("Estimated travel time")
        print("Hours:\t", hours)
        
        continue_var = input("Continue? (y/n): ") #loop check
        print("===============================================================")
        if continue_var == "y": #if y then begin loop / if n then stop and print
            continue
        else:
            print("Bye!")