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
    pass

def calculate_expenses(expenses):
    pass