#!/usr/bin/env python3

def display_title():
    print("Contact Manager")
    
def command_menu():
    print("COMMAND MENU")
    print("list - Display all contacts", "\nview - View a contact",
          "\nadd - Add a contact", "\ndel - Delete a contact",
          "\nexit - Exit program")

def make_list(contact_name, contact_email, contact_phone): #Generates starting data list with two contacts.
    contact_name_a = 'Guido van Rossum'
    contact_email_a ='guido@vanrossum.com'
    contact_phone_a = '+22 34 5439 4422'
    contact_name_b = 'Eric Idle'
    contact_email_b = 'eric@ericidle.com'
    contact_phone_b = '+44 20 7946 0958'
    contact_a = []
    contact_b = []
    contact_a.append(contact_name_a)
    contact_a.append(contact_email_a)
    contact_a.append(contact_phone_a)
    contact_name.append(contact_a)
    contact_email.append(contact_a)
    contact_phone.append(contact_a)
    contact_b.append(contact_name_b)
    contact_b.append(contact_email_b)
    contact_b.append(contact_phone_b)
    contact_name.append(contact_b)
    contact_email.append(contact_b)
    contact_phone.append(contact_b)
    print()

def list_contact(contact_name):
    for i in range(len(contact_name)):
        name = contact_name[i] #Name var will look for Contact Name's index.
        i += 1
        print(f"{i}. {name[0]}")
    print()

def view_contact(contact_name, contact_email, contact_phone):
    num_input = int(input("Number: "))
    if num_input < 1 or num_input > len(contact_name) + 1: #If user input is less than 1 or greater than the amount of indexed contacts, it will fail.
        print("Invalid contact number. Please try again. \n")
        print()
        return
    else:
        name = contact_name[num_input-1]
        email = contact_email[num_input-1]
        phone = contact_phone[num_input-1]
        
        print("Name: " , name[0])
        print("Email: " , email[1])
        print("Phone: " , phone[2])
        print()
    
def add(contact_name, contact_email, contact_phone):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contact_name.append(contact)    #
    contact_email.append(contact)   #  #
    contact_phone.append(contact)   #   #   # These add the contact list generated here to the main contact list.
    print(name +  " was added.")    
    print()

def delete(contact_name):
    num_input = int(input("Number: "))
    if num_input < 1 or num_input > len(contact_name): #If user input is less than 1 or greater than the amount of indexed contacts, it will fail.
        print("Invalid contact number. Please try again. \n")
        print()
    else:
        name = contact_name.pop(num_input-1) #Deletes based off index listed.
        print(name[0] + " was deleted.")
        print()
        return contact_name
        
        
def main():
    contact_name = []
    contact_email = []
    contact_phone = []
    
    make_list(contact_name, contact_email, contact_phone)
    display_title()
    print()
    command_menu()
    print()
    
    while main:
        com_input = input("Command: ")
        if com_input == "list":
            list_contact(contact_name)
        elif com_input == "view":
            view_contact(contact_name, contact_email, contact_phone)
        elif com_input == "add":
            add(contact_name, contact_email, contact_phone)
        elif com_input == "del":
            delete(contact_name)        
        elif com_input == "exit":
            print("Bye!")
            return
        else:
            print("Invalid command. Please try again. \n")
    
# if started as the main module, call the main function
if __name__ == "__main__":
    main()