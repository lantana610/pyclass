print("enter what you want to from the option menu")
chioce = []
while True:

    option = input("option:\n 1. Add Expense\n 2. View Epenses\n 3. calculate Total Expenses\n 4. Exit\n")

    if option == "1":
        add = float(input("Enter your expense amount:"))
        chioce.append(add)
        print("expense added successfully.")
    elif option == "2":
         print("chioce:")
         for add in chioce:
            print(chioce)

    elif option == "3":
        total = 0
        for expense in chioce:
            total += expense
        print(f"Total Epenses: {total}")
    elif option == "4":
        print("Thank ypou for using expense Tracker.")
        break
else:
    print("Invalid option.")