#! /usr/bin/env python3

#display message
print("===============================================================")
print("Shipping Calculator")
print("===============================================================")

#init vars
continue_var = "y"

#y/n var controller
while continue_var == "y":

    
#get user data
        costs_items_ordered = float(input("Cost of items ordered:\t "))
        if costs_items_ordered < 0: #loop until user input is a positive value
            print("You must enter a positive number. Please try again.")
            continue
        elif costs_items_ordered <= 30.00:     #shipping cost vars
            (shipping_cost :=  5.95) and print("Shipping cost:\t\t" , shipping_cost)
        elif costs_items_ordered >= 30.00 and costs_items_ordered <= 49.99:
            (shipping_cost :=  7.95) and print("Shipping cost:\t\t" , shipping_cost)
        elif costs_items_ordered >= 50.00 and costs_items_ordered <= 74.99:
            (shipping_cost :=  9.95) and print("Shipping cost:\t\t" , shipping_cost)
        else:
            print("Shipping cost:\t\t FREE")
        if costs_items_ordered <= 74.99:    #total cost calc
            print("Total cost:\t\t" , round(costs_items_ordered + shipping_cost, 2))
            print()
        else:
            print("Total cost:\t\t" , (costs_items_ordered))    #total cost w/ free shipping applied
            print()
        continue_var = input("Continue? (y/n): ") #loop check
        print("===============================================================")
        if continue_var == "y": #if y then begin loop / if n then stop and print
            continue
        else:
            print("Bye!")

