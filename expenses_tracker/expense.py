
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

    expenses =[
        {"category": "Food", "amount": 500},
        {"category": "Transport", "amount": 200},
        {"category": "Food", "amount": 300}
    ]

def delete_expense(expenses):
    category_to_delete = input("Enter  what you want to delete: ").lower()

    for expense in expenses:
        if expense['category'].lower() == category_to_delete:

            expenses.remove(expense)
            print("expense deleted successfully")
            return

    return "category not found"

expenses = []

add_expense(expenses)

view_expenses(expenses)

calculate_expenses(expenses)
count_expenses(expenses)
find_food_expenses(expenses)
delete_expense(expenses)