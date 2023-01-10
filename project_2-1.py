#!/usr/bin/env python3

#This is the title of the program
print("Registration Form")
print()

#Get user data
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth_year = input("Birth Year: ")
print()

#Display user data and password
print(f"Welcome {first_name} {last_name}!")
print("Your registration is complete.")
print(f"Your temporary password is: {first_name}*{birth_year}")