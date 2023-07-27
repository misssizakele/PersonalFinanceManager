import csv
from datetime import datetime
import matplotlib.pyplot as plt



# Function to input financial transactions
def input_transaction():
    amount = float(input("Enter the transaction amount: "))
    category = input("Enter the transaction category: ")
    date = input("Enter the transaction date (YYYY-MM-DD): ")
    return amount, category, date

# Function to calculate total income and expenses
def calculate_total(transactions):
    total_income = 0
    total_expenses = 0
    for transaction in transactions:
        if transaction[0] >= 0:
            total_income += transaction[0]
        else:
            total_expenses += transaction[0]
    return total_income, total_expenses

# Function to categorize expenses
def categorize_expenses(transactions):
    categories = {}
    for transaction in transactions:
        amount, category, _ = transaction
        if amount < 0:
            if category in categories:
                categories[category] += abs(amount)
            else:
                categories[category] = abs(amount)
    return categories

# Function to set monthly budgets
def set_budgets():
    budgets = {}
    num_categories = int(input("Enter the number of expense categories: "))
    for _ in range(num_categories):
        category = input("Enter the expense category: ")
        budget = float(input("Enter the monthly budget for this category: "))
        budgets[category] = budget
    return budgets

# Function to track spending habits
def track_spending(transactions):
    dates = [datetime.strptime(transaction[2], "%Y-%m-%d") for transaction in transactions]
    amounts = [transaction[0] for transaction in transactions]
    plt.plot(dates, amounts)
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Spending Habits Over Time")
    plt.show()

# Function to export financial data as a CSV file
def export_data(transactions):
    filename = input("Enter the filename for exporting data: ")
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Date"])
        writer.writerows(transactions)
    print("Data exported successfully!")

# Main function
def main():
    transactions = []
    while True:
        print("\nPERSONAL FINANCE MANAGER")
        print("1. Add a Transaction")
        print("2. Calculate Total Income and Expenses")
        print("3. Categorize Expenses")
        print("4. Set Monthly Budgets")
        print("5. Track Spending Habits")
        print("6. Export Financial Data")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            transaction = input_transaction()
            transactions.append(transaction)
            print("Transaction added successfully!")
        elif choice == 2:
            total_income, total_expenses = calculate_total(transactions)
            print(f"Total Income: {total_income}")
            print(f"Total Expenses: {total_expenses}")
            print(f"Savings: {total_income + total_expenses}")
        elif choice == 3:
            categories = categorize_expenses(transactions)
            for category, amount in categories.items():
                print(f"{category}: {amount}")
        elif choice == 4:
            budgets = set_budgets()
            for category, budget in budgets.items():
                print(f"Budget for {category}: {budget}")
        elif choice == 5:
            track_spending(transactions)
        elif choice == 6:
            export_data(transactions)
        elif choice == 7:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()