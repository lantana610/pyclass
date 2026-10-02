print("enter what you want to from the option menu")
choice = []
while True:

    option = input("option:\n 1. Add Expense\n 2. View Epenses\n 3. calculate Total Expenses\n 4. Exit\n")

    if option == "1":
        add = float(input("Enter your expense amount:"))
        choice.append(add)
        print("expense added successfully.")
    elif option == "2":
         print("choice:")
         for add in choice:
            print(add)

    elif option == "3":
        total = 0
        for expense in choice:
            total += expense
        print(f"Total Epenses: {total}")
    elif option == "4":
        print("Thank ypou for using expense Tracker.")
        break
    else:
        print("Invalid option.")