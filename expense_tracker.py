import json
import matplotlib.pyplot as plt 

expenses = []

def add_expense (expense):
    category = input("Enter the category (e.g, Food, Transport): ")
    amount = float(input("Enter the amount: " ))
    date = input("Enter the date (YYYY-MM-DD): ")
    expenses.append({"category": category, "amount": amount, "date": date})
    print("Expense added succesfylly!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded")
    for expense in expenses:
        print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")


def delete_expenses(expenses):
    view_expenses(expenses)
    try:
        index = int(input("Enter the index of the expenses to delete"))
        if 0 <= index < len(expenses):
            expenses.pop(index)
            print("Expenses deleted successfuly!")

        else:
            print("Invalid Index.")

    except ValueError:
        print("Please enter a valid number.")      

def summarize_expenses(expenses):
    summary = {}
    for expense in expense:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\nSummary of Expenses:")
    for category, total in summary.items():
        print(f"Category; {category}, Total Spent {total}")

def visualize_expenses(expenses):
    summary = {}
    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"] 

    catgories = list(summary.keys())
    amounts = list(summary.values())

    plt.figure(figsize=(10, 5))
    plt.bar(catgories, amounts, color='skyblue')
    plt.xlabel("Category")
    plt.tittle("Expenses by Category")
    plt.show()     


def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "W") as file:
        json.dump(expenses, file)
        print("Expenses saved to file.")


def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def main():
    global expenses
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense ")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Summarize Expenses")
        print("5. Visualize Expenses")
        print("6. Save and Exit")

        choice = input("Choose an Option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expenses(expenses)
        elif choice == '4':
            summarize_expenses(expenses)
        elif choice == '5':
            view_expenses(expenses)
        elif choice == '6':
            save_expenses(expenses)
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()            




