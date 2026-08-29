# Simple Expense Tracker - by Elvis Walker
# A clean CLI app for tracking daily expenses in Ksh

import json
import os
from datetime import datetime

FILE = "expenses.json"

def load_expenses():
    """Load expenses from json file, return empty list if file missing"""
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_expenses(expenses):
    """Save expenses list to json file"""
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense():
    """Add a new expense entry"""
    try:
        amount = float(input("Amount (Ksh): ").strip())
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    category = input("Category (food, fare, rent etc): ").strip().lower()
    note = input("Note: ").strip()

    if not category:
        category = "general"

    expenses = load_expenses()
    expenses.append({
        "amount": amount,
        "category": category,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_expenses(expenses)
    print(f"\nSaved! Ksh {amount} for {category}")

def view_expenses():
    """View all expenses and total"""
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses yet. Add one first!")
        return

    print("\n--- Your Expenses ---")
    total = 0
    for e in expenses:
        print(f"{e['date']} | {e['category']}: Ksh {e['amount']} ({e['note']})")
        total += e['amount']
    
    print("-" * 30)
    print(f"TOTAL SPENT: Ksh {total}")
    print("-" * 30)

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose (1-3): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Bye! Keep tracking.")
            break
        else:
            print("Invalid choice, try 1, 2 or 3")

if __name__ == "__main__":
    main()
