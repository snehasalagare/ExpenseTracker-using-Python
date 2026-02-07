import csv

FILE_NAME = "expenses.csv"

# Initialize CSV file
def initialize_file():
    try:
        with open(FILE_NAME, "r"):
            pass
    except FileNotFoundError:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Month", "Amount", "Category", "Description"])

# Add a new expense
def add_expense():
    month = input("Enter month (e.g., Jan, Feb): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([month, amount, category, description])

    print("Expense added successfully\n")

# View all expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        print("\nMonth | Amount | Category | Description")
        print("-" * 45)
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    print()

# Total expense analysis
def total_expenses():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[1])

    print("Total expenses:", total, "\n")

# Monthly summary
def monthly_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            month = row[0]
            amount = float(row[1])
            summary[month] = summary.get(month, 0) + amount

    print("\nMonthly expense summary:")
    for month in summary:
        print(month, ":", summary[month])
    print()

# Category-wise summary
def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[2]
            amount = float(row[1])
            summary[category] = summary.get(category, 0) + amount

    print("\nCategory-wise expense summary:")
    for category in summary:
        print(category, ":", summary[category])
    print()

# Main menu
def main():
    initialize_file()

    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Monthly Summary")
        print("5. Category Summary")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            category_summary()
        elif choice == "6":
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
