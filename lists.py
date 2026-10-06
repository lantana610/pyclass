languages = ["python", "Go", "JavaScript"]

languages.append("Rust")
languages.remove("Go")
print(len(languages))

for language in languages:
    print(language)

# list containing multiple items
expenses = [
    {"category": "food", "amount": 500},
    {"category": "Transport", "amount": 200},
    {"category": "Internet", "amount": 100}
]
for expense in expenses:
    print(expense["category"])
# print amounts

amounts = [money["amount"] for money in expenses]
print(amounts)

# calculate total

total = 0
for expense in expenses:
    total += expense["amount"]

print(f"Total expenses: {total}")