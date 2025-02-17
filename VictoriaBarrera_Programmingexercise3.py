# Victoria Barrera Exercise 3.
# Import reduce from functools for calculating total expenses.
from functools import reduce

def main():
    # Create an empty list to store expenses.
    expenses = []
    # Start an infinite loop to collect user input asking for expense names and amount.
    while True:
        name = input("Enter expense name (Type 'done' to finish): ").strip()
        # Check if the user wants to stop giving input.
        if name.lower() == "done":
            # Exit the loop if 'done' is entered
            break

        try:
            # Convert expense to float.
            amount = float(input("Enter amount: "))
            expenses.append((name, amount))
            # If user gives invalid input.
        except ValueError:
            print("Invalid input.")
            # If no expenses were entered.
    if not expenses:
        print("No expenses entered.")
        return

    # Use reduce to calculate the total expense though the sum of the amounts.
    total = reduce(lambda acc, x: acc + x[1], expenses, 0)

    # Find the highest expense using max().
    highest = max(expenses, key=lambda x: x[1])

    # Find the lowest expense using min().
    lowest = min(expenses, key=lambda x: x[1])

    # Print the results
    print(f"\nTotal Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

if __name__ == "__main__":
    # Call the main function
    main()