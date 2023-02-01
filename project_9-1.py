#! /usr/bin/env python3

import locale as lc

lc.setlocale(lc.LC_ALL, "en_us")

#display message
print("Interest Calculator")
print()

#init vars
continue_var = "y"

#y/n var controller
while continue_var == "y":

    
#get user data
        loan_amount = float(input("Enter loan amount:\t "))
        if loan_amount < 0: #loop until user input is a positive value
            print("You must enter a positive number. Please try again.")
            continue
        else:
            interest_rate = float(input("Enter interest rate:\t "))
        if interest_rate < 0: #loop until user input is a positive value
            print("You must enter a positive number. Please try again.")
            continue
        else:
            interest_amount = loan_amount * (interest_rate / 100)       #interest amount calc
            loan_amount = lc.currency(loan_amount, grouping=True)
            interest_amount = lc.currency(interest_amount, grouping=True)       #interest amount calc 
            print()
            print(f"{'Loan amount:':24}  {loan_amount:>10}")
            print(f"{'Interest rate:':24} {interest_rate:10,.3f}%")
            print(f"{'Interest amount:':24}  {interest_amount:>10}")
            print()

        continue_var = input("Continue? (y/n): ") #loop check
        print()
        
        if continue_var == "y": #if y then begin loop / if n then stop and print
            continue
        else:
            print("Bye!")
