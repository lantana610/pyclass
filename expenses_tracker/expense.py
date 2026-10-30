def add_expense(expenses):
    category = input("enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }
    
    expenses.append(expense)

    print("Expense added.")

def view_expenses(expenses):
    for expense in expenses:
        print(f"{expense['category']} - {expense['amount']}")

def calculate_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense['amount']

    print(f"Total: {total}")

def count_expenses(expenses):
    print(f"number of expenses {len(expenses)}")


def find_food_expenses(expenses):

    for expense in expenses:
        if expense["category"] == "Food":
            print(f"{expense['category']} - {expense['amount']}")

   

def delete_expense(expenses):
    category_to_delete = input("Enter  what you want to delete: ").lower()

    for expense in expenses:
        if expense['category'].lower() == category_to_delete:

            expenses.remove(expense)
            print("expense deleted successfully")
            return

    print("category not found")

def update_expense(expenses):
    category = input("enter catergory to update: ")
    new_amount = float(input("enter new amount to update: "))

    for expense in expenses:
        if expense["category"] == category:
            expense['amount'] = new_amount

            print("expense updated successfully.")
            
            return

    print("expense not found.")


expenses = []

while True:

    option = input(
        "\n1. Add Expense"
        "\n2. View Expenses"
        "\n3. Calculate Total"
        "\n4. Count Expenses"
        "\n5. Find Food Expenses"
        "\n6. Update Expense"
        "\n7. Delete Expense"
        "\n8. Exit"
        "\nChoose an option: "
    )
    if option == "1":
        add_expense(expenses)

    elif option == "2":
        view_expenses(expenses)

    elif option == "3":
        calculate_expenses(expenses)

    elif option == "4":
        count_expenses(expenses)

    elif option == "5":
        find_food_expenses(expenses)

    elif option == "6":
        update_expense(expenses)

    elif option == "7":
        delete_expense(expenses)

    elif option == "8":
        print("Googbye!")
        break

    else:
        print("invalid option.")

with open("skills.txt", "w") as file:
    file.write("Python")
with open("skills.txt", "w") as file:
    file.write("Go")
with open("skills.txt", "w") as file:
    file.write("linux")
with open("skills.txt", "w") as file:
    file.write("Git")