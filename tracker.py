import json
from datetime import datetime
import os

# ---------- File Handling ----------

FILE_NAME = 'expenses.json'

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, 'w') as file:
        json.dump(expenses, file, indent=4)

# ---------- Core Features ----------

def add_expense(expenses):
    try:
        amount = float(input("Enter amount: ₹ "))
        category = input("Enter category (e.g., Food, Transport): ").capitalize()
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        date = date_input if date_input else datetime.today().strftime('%Y-%m-%d')

        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("✅ Expense added!\n")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.\n")

def view_summary(expenses):
    if not expenses:
        print("📭 No expenses to show.\n")
        return
    
    total = 0
    category_totals = {}

    for exp in expenses:
        total += exp["amount"]
        category = exp["category"]
        category_totals[category] = category_totals.get(category, 0) + exp["amount"]

    print("\n📊 Summary by Category:")
    for cat, amt in category_totals.items():
        print(f"  {cat}: ₹{amt:.2f}")
    
    print(f"\n💰 Total Expenses: ₹{total:.2f}\n")

# ---------- Main Menu ----------

def main():
    expenses = load_expenses()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("💾 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# ✅ Don't forget this line
if __name__ == "__main__":
    main()
