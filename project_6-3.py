#!/usr/bin/env python3

def display_title():
    print("Contact Manager")
    
def command_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    
def list_contact():
    contact_name = ["Guido van Rossum", "Eric Idle"]
    for i in range(len(contact_name)):
        name = contact_name[i]
        print(f"{i + 1}. {name}")

def command_input():
    input = input("Command: ")
    return        

def main():
    display_title()
    print()
    command_menu()
    print()
    command_input()
    
# if started as the main module, call the main function
if __name__ == "__main__":
    main()