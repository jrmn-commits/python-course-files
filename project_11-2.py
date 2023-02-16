#! /usr/bin/env python3
#Project 11-2

from datetime import date, time, datetime, timedelta

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
        time_traveled = float(miles / miles_per_hr) * 3600
        

        #calc arrival datetime
        arrival_datetime = dep_datetime + timedelta(seconds = time_traveled)
        date_format = "%Y-%m-%d"
        time_format = "%I:%M %p"
        travel_span = (arrival_datetime - dep_datetime).seconds
        arrival_timespan = travel_span // 60
        arrival_hr = arrival_timespan // 60
        arrival_mins = arrival_timespan % 60

        #print results
        print("Estimated travel time")
        print("Hours:\t\t", arrival_hr)
        print("Minutes:\t", arrival_mins)
        print(f"Estimated date of arrival:\t {arrival_datetime:{date_format}}")
        print(f"Estimated date of arrival:\t {arrival_datetime:{time_format}}")
        
        continue_var = input("Continue? (y/n): ") #loop check
        print()
        if continue_var == "y": #if y then begin loop / if n then stop and print
            continue
        else:
            print("Bye!")