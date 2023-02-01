#!/usr/bin/env python3

import csv

FILENAME = "contacts.csv"

def write_contacts(contacts):
    with open (FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def read_contacts():
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def display_title():
    print("Contact Manager")
    
def command_menu():
    print("COMMAND MENU")
    print("list - Display all contacts", "\nview - View a contact",
          "\nadd - Add a contact", "\ndel - Delete a contact",
          "\nexit - Exit program")

def list_contact(contacts):
    for i in range(len(contacts)):
        name = contacts[i] #Name var will look for Contact Name's index.
        i += 1
        print(f"{i}. {name[0]}")
    print()

def view_contact(contacts):
    num_input = int(input("Number: "))
    if num_input < 1 or num_input > len(contacts) + 1: #If user input is less than 1 or greater than the amount of indexed contacts, it will fail.
        print("Invalid contact number. Please try again. \n")
        print()
        return
    else:
        contact = contacts[num_input-1]
        
        print("Name: " , contact[0])
        print("Email: " , contact[1])
        print("Phone: " , contact[2])
        print()
    
def add(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)   #   #   # These add the contact list generated here to the main contact list.
    write_contacts(contacts)
    print(name +  " was added.")    
    print()

def delete(contacts):
    num_input = int(input("Number: "))
    if num_input < 1 or num_input > len(contacts): #If user input is less than 1 or greater than the amount of indexed contacts, it will fail.
        print("Invalid contact number. Please try again. \n")
        print()
    else:
        name = contacts.pop(num_input-1) #Deletes based off index listed.
        write_contacts(contacts)
        print(name[0] + " was deleted.")
        print()
        return contacts
        
        
def main():
    display_title()
    contacts =  read_contacts()
    print()
    command_menu()
    print()
    
    while main:
        com_input = input("Command: ")
        if com_input == "list":
            list_contact(contacts)
        elif com_input == "view":
            view_contact(contacts)
        elif com_input == "add":
            add(contacts)
        elif com_input == "del":
            delete(contacts)        
        elif com_input == "exit":
            print("Bye!")
            return
        else:
            print("Invalid command. Please try again. \n")
    
# if started as the main module, call the main function
if __name__ == "__main__":
    main()