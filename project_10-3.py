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
        loan_amount = input("Enter loan amount:\t ")
        loan_amount = loan_amount.removeprefix("$")
        loan_amount = loan_amount.replace(",", "")
        loan_convert = loan_amount.find("K")
        if loan_convert == 3:
                loan_amount = loan_amount.replace("K", "")
                loan_amount = float(loan_amount)
                new_loan_amount = loan_amount * 1000
                loan_amount = new_loan_amount
        elif loan_convert < 3:
                loan_amount = float(loan_amount)
        else:
                print("You must enter a valid number.")
                continue
        if loan_amount < 0: #loop until user input is a positive value
                print("You must enter a positive number. Please try again.")
                continue
        else:
                interest_rate = input("Enter interest rate:\t ")
                interest_rate = interest_rate.removeprefix("%")
                interest_rate = interest_rate.removesuffix("%")
                interest_rate = interest_rate.replace(",", "")
                interest_rate = float(interest_rate)
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