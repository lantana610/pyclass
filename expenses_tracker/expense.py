expenses = []
def add_expenses(expenses):
    category = input("enter category: ")
    amount = input(float("Enter amount: "))

    expense = {
        "category": category
        "amount": amount
    }
    
    expenses.append(expense)

    print("Expense added.")

def view_expenses(expenses):
    for expense in expenses:
        print(f"{expense['catergory']} - {expense['amount']}")

def calculate_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense['amount']

        print(f"Total: {total}")