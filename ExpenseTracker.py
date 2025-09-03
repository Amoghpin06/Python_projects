from datetime import datetime

class Expense:
    def __init__(self, date, amount, description):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
        else:
            print("Expense List:")
            print(f"{'Index':<6} {'Date':<12} {'Description':<20} {'Amount':>10}")
            print("-" * 50)
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i:<6} {expense.date:<12} {expense.description:<20} {expense.amount:>10.2f}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses: {total:.2f}")

# Utility function for validating date format
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            if not validate_date(date):
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            description = input("Enter the description: ")
            try:
                amount = float(input("Enter the amount: "))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            expense = Expense(date, amount, description)
            tracker.add_expense(expense)
            print("Expense added successfully.")

        elif choice == "2":
            try:
                index = int(input("Enter the expense index to remove: ")) - 1
                tracker.remove_expense(index)
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        elif choice == "3":
            tracker.view_expenses()

        elif choice == "4":
            tracker.total_expenses()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
