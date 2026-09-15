expense =  []
import datetime

while True:
    print("")
    print("1. Add expense")
    print("2. Show current date and time")
    print("3. Show all expenses")
    print("4. Show total expenses")
    print("5. Search expense")
    print("6. Delete expense")
    print("7. Exit")
    choice = input("Choose an option (1-7): ")

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
            if exp["name"] == search_name:
                print("Found:", exp["name"], "|", exp["amount"])
                found = True
        if not found:
            print("Expense not found")

    elif choice == "6":
        delete_name = input("Enter expense to delete: ").strip().capitalize()
        found = False
        for exp in expense:
            if exp["name"] == delete_name:
                expense.remove(exp)
                print("Expense deleted!")
                found = True
                break
        if not found:
            print("Expense not found")

    elif choice == "7":
        print("Exiting...")
        break
