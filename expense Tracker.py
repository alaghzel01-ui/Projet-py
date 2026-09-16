expense =  []
budget = None
import datetime
import os
print(os.getcwd())

while True:
    print("")
    print("1. Add expense")
    print("2. Show current date and time")
    print("3. Show all expenses")
    print("4. Show total expenses")
    print("5. Search expense")
    print("6. Delete expense")
    print("7. Exit")
    print("8. Show statistics")
    print("9. Budget system")
    print("10 Show budget status")
    print("11. Expenses by categories")
    print("12. highest spending category")
    print("13. date processing")
    print("14. expenses.json")
    print("15. json.load")
    choice = input("Choose an option (1-15): ")

    if choice == "1":
        type_of_expense = input("expense: ").strip().capitalize()
        amount = input("Enter amount: ").strip()
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue
        if amount < 50 :
            print("Invalid amount. Please enter an amount between 50 and 1000.")
        elif amount > 1000:
            print("expense is high, consider budgeting.")
        else:
            expense.append({"name": type_of_expense, "amount": amount, "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}) 
            print("Expense added!")  
            print("Expense:", type_of_expense, "| Amount:", amount, "| Date:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    elif choice == "2":
        now = datetime.datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print("Current date and time:", current_time)      


    elif choice == "3":
        if len(expense) == 0:
            print("No expenses yet")
        else:
            print("")
            print("All expenses:")
            for exp in expense:
                print("-", exp["name"], "|", exp["amount"], "|", exp["date"])

    elif choice == "4":
        total = sum(float(exp["amount"]) for exp in expense)
        print("Total expenses:", total)

    elif choice == "5":
        search_name = input("Enter expense to search: ").strip().capitalize()
        found = False
        for exp in expense:
            if exp["name"].lower() == search_name.lower():
                print("Found:", exp["name"], "|", exp["amount"], "|", exp["date"])
                found = True
        if not found:
            print("Expense not found")

    elif choice == "6":
        delete_name = input("Enter expense to delete: ").strip().capitalize()
        confirmation = input("Are you sure you want to delete this expense? (yes/no): ").strip().lower()
        if confirmation == "yes":
            print("Expense deletion.")
        elif confirmation == "no":
                print("delete cancelled.")
                continue
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        found = False
        for exp in expense:
            if exp["name"].lower() == delete_name.lower():
                new_list = [e for e in expense if e["name"].lower() != delete_name.lower()]
                expense = new_list
                print("Deleted expense:", exp["name"])    
                print("Expense deleted!")
                found = True
        if not found:
                print("Expense not found")

    elif choice == "7":
        print("Exiting...")
        break

    elif choice == "8":
        if len(expense) == 0:
            print("No expenses yet")
        else:
            total = sum(float(exp["amount"]) for exp in expense)
            print("Total expenses:", total)
            average = total / len(expense)
            print("Average expense:", average)
            highest = max(float(exp["amount"]) for exp in expense)
            print("Highest expense:", highest)
            lowest = min(float(exp["amount"]) for exp in expense)
            print("Lowest expense:", lowest)

    elif choice == "9":
        print("Enter your monthly budget:")
        budget = float(input("Enter your monthly budget: "))
        print("Budget set to:", budget)
        total_expenses = sum(float(exp["amount"]) for exp in expense)
        if total_expenses > budget:
            print("You have exceeded your budget by:", total_expenses - budget)
        else:
            print("You are within your budget. Remaining budget:", budget - total_expenses)

    elif choice == "10":
        if budget is None:
            print("No budget set. Please set a budget first.")
        else:
            total_expenses = sum(float(exp["amount"]) for exp in expense)
            remaining = budget - total_expenses
            print("Total expenses:", total_expenses)
            print("Remaining budget:", remaining)
            if remaining < 0:
                print("You have exceeded your budget by:", abs(remaining))

            else:
                print("You are within your budget. Remaining budget:", budget - total_expenses)

    elif choice == "11":
        if len(expense) == 0:
            print("No expenses yet")
        else:
            category_expenses = {}
            for exp in expense:
                category = exp["name"]
                amount = float(exp["amount"])
                if category in category_expenses:
                    category_expenses[category] += amount
                else:
                    category_expenses[category] = amount
            print("Expenses by categories:")
            for category, total in category_expenses.items():
                print("-", category, "| Total:", total)

    elif choice == "12":
        if len(expense) == 0:
            print("No expenses yet")
        else:
            category_expenses = {}
            for exp in expense:
                category = exp["name"]
                amount = float(exp["amount"])
                if category in category_expenses:
                    category_expenses[category] += amount
                else:
                    category_expenses[category] = amount
            highest_category = max(category_expenses, key=category_expenses.get)
            highest_amount = category_expenses[highest_category]
            print("Highest spending category:", highest_category, "| Total:", highest_amount)

    elif choice == "13":
        if len(expense) == 0:
            print("No expenses yet")
        else:
            print("Date processing options:")
            print("1. Filter expenses by date")
            print("2. Show expenses for a specific month")
            print("3. Show expenses for a specific year")
            date_choice = input("Choose an option (1-3): ")
            if date_choice == "1":
                filter_date = input("Enter date (YYYY-MM-DD): ")
                filtered_expenses = [exp for exp in expense if exp["date"].startswith(filter_date)]
                total_filtered = sum(float(exp["amount"]) for exp in filtered_expenses)
                print("Total expenses for", filter_date, ":", total_filtered)
                if len(filtered_expenses) == 0:
                    print("No expenses found for this date.")
                else:
                    print("Expenses for", filter_date, ":")
                    for exp in filtered_expenses:
                        print("-", exp["name"], "|", exp["amount"], "|", exp["date"])

            elif date_choice == "2":
                filter_month = input("Enter month (YYYY-MM): ")
                filtered_expenses = [exp for exp in expense if exp["date"].startswith(filter_month)]
                total_filtered = sum(float(exp["amount"]) for exp in filtered_expenses)
                print("Total expenses for", filter_month, ":", total_filtered)
                if len(filtered_expenses) == 0:
                    print("No expenses found for this month.")
                else:
                    print("Expenses for", filter_month, ":")
                    for exp in filtered_expenses:
                        print("-", exp["name"], "|", exp["amount"], "|", exp["date"])

            elif date_choice == "3":
                filter_year = input("Enter year (YYYY): ")
                filtered_expenses = [exp for exp in expense if exp["date"].startswith(filter_year)]
                total_filtered = sum(float(exp["amount"]) for exp in filtered_expenses)
                print("Total expenses for", filter_year, ":", total_filtered)
                if len(filtered_expenses) == 0:
                    print("No expenses found for this year.")
                else:
                    print("Expenses for", filter_year, ":")
                    for exp in filtered_expenses:
                        print("-", exp["name"], "|", exp["amount"], "|", exp["date"])
            else:
                print("Invalid option. Please choose a valid option (1-3).")

    elif choice == "14":
        import json
        with open("expenses.json", "w") as f:
            json.dump(expense, f)
        print("Expenses saved to expenses.json")


    elif choice == "15":
        try:
            import json
            with open("expenses.json", "r") as f:
                expense = json.load(f)
            print("Expenses loaded from expenses.json")
        except FileNotFoundError:
            print("No existing expenses.json file found.")

