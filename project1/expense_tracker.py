print("Enter what you want to do from the option menu")

expenses = []

while True:

    option = input("\n1. Add Expense\n2. View Expenses\n3. Calculate Total Expenses\n4. Exit\nChoose an option: ")

    if option == "1":

        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added successfully.")

    elif option == "2":

        print("\nExpenses:")

        for expense in expenses:
            print(
                f"Category: {expense['category']} | "
                f"Amount: {expense['amount']}"
            )

    elif option == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total Expenses: {total}")

    elif option == "4":
        print("Thank you for using Expense Tracker.")
        break

    else:
        print("Invalid option.")


