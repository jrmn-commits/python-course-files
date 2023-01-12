#!/usr/bin/env python3

#diplay message
print("Price Comparison")
print()

#get price of oz from user
price_of_a = float(input("Price of 64 oz size: "))
price_of_b = float(input("Price of 32 oz size: "))
print()

#calculate price per oz
price_per_a = round(price_of_a / 64 , 2)
price_per_b = round(price_of_b / 32 , 2)

#display result
print("Price per oz (64 oz):" , price_per_a)
print("Price per oz (32 oz):" , price_per_b)
