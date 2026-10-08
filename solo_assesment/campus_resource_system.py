import json
import os
from datetime import datetime

resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3},
]

fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}

borrow_records = []

borrow_log = []

DATA_FILE = "data.json"


def find_resource(resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None


def valid_fellow(fellow_id):
    return fellow_id in fellows


def find_borrow_record(fellow_id, resource_id):
    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            return record
    return None


def read_positive_int(prompt):
    text = input(prompt).strip()
    try:
        value = int(text)
    except ValueError:
        print("Error: quantity must be a whole number (e.g. 2).")
        return None
    if value <= 0:
        print("Error: quantity must be a positive number.")
        return None
    return value


def print_resource(resource):
    print(f'{resource["id"]} | {resource["name"]} | {resource["category"]} | '
          f'available {resource["available"]} of {resource["total"]}')


def save_data():
    data = {
        "resources": resources,
        "borrow_records": borrow_records,
        "borrow_log": borrow_log,
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def load_data():
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE) as f:
            data = json.load(f)
        resources[:] = data["resources"]
        borrow_records[:] = data["borrow_records"]
        borrow_log[:] = data["borrow_log"]
        print("Saved data loaded.")
    except (json.JSONDecodeError, KeyError, OSError):
        print("Could not read saved data. Using starting data.")


def add_resource():
    resource_id = input("Resource ID: ").strip().upper()
    if resource_id == "":
        print("Error: ID cannot be empty.")
        return
    if find_resource(resource_id) is not None:
        print("Error: that resource ID already exists. Nothing was added.")
        return

    name = input("Name: ").strip()
    category = input("Category: ").strip()
    if name == "" or category == "":
        print("Error: name and category cannot be empty.")
        return

    total = read_positive_int("Total units: ")
    if total is None:
        return

    resources.append({"id": resource_id, "name": name, "category": category,
                      "total": total, "available": total})
    save_data()
    print("Resource added.")


def list_resources():
    if not resources:
        print("No resources in inventory.")
        return
    for resource in resources:
        print_resource(resource)


def borrow_resource():
    fellow_id = input("Enter fellow ID: ").strip().upper()
    if not valid_fellow(fellow_id):
        print("Error: invalid fellow ID.")
        return

    resource_id = input("Enter resource ID: ").strip().upper()
    resource = find_resource(resource_id)
    if resource is None:
        print("Error: resource not found.")
        return

    quantity = read_positive_int("Enter quantity: ")
    if quantity is None:
        return
    if quantity > resource["available"]:
        print(f'Error: not enough stock. Only {resource["available"]} available.')
        return

    resource["available"] -= quantity

    record = find_borrow_record(fellow_id, resource_id)
    if record:
        record["quantity"] += quantity
    else:
        borrow_records.append({"fellow_id": fellow_id,
                               "resource_id": resource_id,
                               "quantity": quantity})

    borrow_log.append({"fellow_id": fellow_id,
                       "resource_id": resource_id,
                       "quantity": quantity,
                       "time": datetime.now().isoformat(timespec="seconds")})
    save_data()
    print(f'Borrowing successful. {resource["name"]} available: {resource["available"]}')


def return_resource():
    fellow_id = input("Enter fellow ID: ").strip().upper()
    if not valid_fellow(fellow_id):
        print("Error: invalid fellow ID.")
        return

    resource_id = input("Enter resource ID: ").strip().upper()
    resource = find_resource(resource_id)
    if resource is None:
        print("Error: resource not found.")
        return

    record = find_borrow_record(fellow_id, resource_id)
    if record is None:
        print("Error: this fellow has no loan for that resource.")
        return

    quantity = read_positive_int("Enter quantity to return: ")
    if quantity is None:
        return
    if quantity > record["quantity"]:
        print(f'Error: cannot return more than borrowed. On loan: {record["quantity"]}.')
        return

    resource["available"] += quantity
    record["quantity"] -= quantity
    if record["quantity"] == 0:
        borrow_records.remove(record)
    save_data()
    print(f'Return successful. {resource["name"]} available: {resource["available"]}')


def search_resource():
    search = input("Enter resource name: ").strip().lower()
    if search == "":
        print("Error: search text cannot be empty.")
        return
    found = False
    for resource in resources:
        if search in resource["name"].lower():
            print_resource(resource)
            found = True
    if not found:
        print("No matching resource found.")


def filter_by_category():
    category = input("Enter category: ").strip().lower()
    found = False
    for resource in resources:
        if resource["category"].lower() == category:
            print_resource(resource)
            found = True
    if not found:
        print("No resources found in that category.")


def generate_report():
    total_units = sum(r["total"] for r in resources)
    available_units = sum(r["available"] for r in resources)
    borrowed_units = sum(r["quantity"] for r in borrow_records)

    print("\n=== REPORT ===")
    print("Total units:", total_units)
    print("Available units:", available_units)
    print("Borrowed units:", borrowed_units)

    print("\nLow stock resources (fewer than 3 available):")
    low_found = False
    for resource in resources:
        if resource["available"] < 3:
            print(f'{resource["name"]} ({resource["available"]})')
            low_found = True
    if not low_found:
        print("None")

    borrowed_by_resource = {}
    for record in borrow_records:
        rid = record["resource_id"]
        borrowed_by_resource[rid] = borrowed_by_resource.get(rid, 0) + record["quantity"]

    print("\nMost borrowed resource(s):")
    if not borrowed_by_resource:
        print("Nothing is currently borrowed.")
        return
    max_borrowed = max(borrowed_by_resource.values())
    for rid, qty in borrowed_by_resource.items():
        if qty == max_borrowed:
            print(f'{find_resource(rid)["name"]} ({qty})')


def show_menu():
    print("\n===== Learn2Earn Resource Manager =====")
    print("1. Add resource")
    print("2. List resources")
    print("3. Borrow resource")
    print("4. Return resource")
    print("5. Search by name")
    print("6. Filter by category")
    print("7. Generate report")
    print("8. Exit")


def main():
    load_data()
    actions = {
        "1": add_resource,
        "2": list_resources,
        "3": borrow_resource,
        "4": return_resource,
        "5": search_resource,
        "6": filter_by_category,
        "7": generate_report,
    }
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()
        if choice == "8":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
