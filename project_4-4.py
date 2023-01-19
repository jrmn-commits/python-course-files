# /usr/bin/python3

#display message
print("Sales Tax Calculator")
print()
print("ENTER ITEMS (ENTER 0 TO END)")

#init vars
continue_var = "y"
total_cost = 0


#y/n var controller
while continue_var == "y":
    
#get cost of items
    costs_items_input = float(input("Cost of items ordered:\t "))
    if costs_items_input != 0: #loop until user input is a value greater than 0
        total_cost += costs_items_input
        continue
    else:    
        sales_tax_total = round(total_cost * .06, 2)        #sales tax calc
        print("Total cost:\t\t" , round(total_cost, 2))
        print("Sales tax:\t\t" , round(sales_tax_total, 2))
        print("Total after tax:\t" , round(total_cost + sales_tax_total, 2))
        print()
        
    continue_var = input("Again? (y/n): ") #loop check
    print()
    
    if continue_var == "y": #if y then begin loop / if n then stop and print
        total_cost = 0 # reset var
        print("ENTER ITEMS (ENTER 0 TO END)")
        continue
    else:
        print("Thanks, bye!")    