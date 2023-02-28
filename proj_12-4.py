#! /usr/bin.env python3
#Project 12-4


FILENAME = "monthly_sales.txt"

def write_months(months):
    with open (FILENAME, "w") as file:
        writer = file.write(file)
        writer.writerows(months)

def read_months_from_txt():   
    with open(FILENAME, "r") as file:
        monthly_sales = {}
        for line in file:
            line = line.replace("\n", "")
            row = line.split("\t")
            monthly_sales[row[0]] = int(row[1])          
    return monthly_sales

def display_title():
    print("Monthly Sales Program")
    print()

def command_menu():
    print("COMMAND MENU")
    print("\nview - View sales for specified month",
          "\nedit - Edit sales for specified month", "\ntotals - View sales summary for year",
          "\nexit - Exit program")

def edit_month(monthly_sales):
    month = input("Three-letter Month:\n")
    month = month.title()
    if month in monthly_sales.keys():
        amount = int(input("Sales Amount:\n"))
        monthly_sales[month] = amount
        print("Sales amount for {:s} is {:,.2f}.".format(month, amount))
        print()
    else:
        print(" Invalid three-letter month.")
        print()
        
def yearly_total(monthly_sales):       
        total = 0.0
        for month, amount in monthly_sales.items():
            totals += amount
            return total
def main():
    monthly_sales = {}
    display_title()
    print()
    command_menu()
    print()
    
    while main:
        com_input = input("Command: ")
        if com_input == "view":
            monthy_sales = read_months_from_txt()
            print(monthly_sales)
        elif com_input == "edit":
            monthly_sales = edit_month(monthly_sales)
        elif com_input == "totals":
            add(contacts)      
        elif com_input == "exit":
            print("Bye!")
            return
        else:
            print("Invalid command. Please try again. \n")
    
# if started as the main module, call the main function
if __name__ == "__main__":
    main()