#!/usr/bin/env python3

#This is the title of the console
print("Tip Calculator")
print()

#Get price of meal data
meal_cost = float(input("Cost of Meal: "))
print()

#Tip amount calc
tip_amnt_a = round(meal_cost * .15, 2)
tip_amnt_b = round(meal_cost * .20, 2)
tip_amnt_c = round(meal_cost * .25, 2)

#Total Amount


#Display data
print("15%")
print("Tip Amount: ", tip_amnt_a)
print("Total Amount: ", round(tip_amnt_a + meal_cost, 2))
print()

print("20%")
print("Tip Amount: ", tip_amnt_b)
print("Total Amount: ", round(tip_amnt_b + meal_cost, 2))
print()

print("25%")
print("Tip Amount: ", tip_amnt_c)
print("Total Amount: ", round(tip_amnt_c + meal_cost, 2))
print()
