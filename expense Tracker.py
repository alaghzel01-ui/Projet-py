expense =  []
while True:
    print("")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Show total expenses")
    print("4. Search expense")
    print("5. Delete expense")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")

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
            expense.append({"name": type_of_expense, "amount": amount}) 
            print("Expense added!")            


    elif choice == "2":
        if len(expense) == 0:
            print("No expenses yet")
        else:
            print("")
            print("All expenses:")
            for exp in expense:
                print("-", exp["name"], "|", exp["amount"])

    elif choice == "3":
        total = sum(float(exp["amount"]) for exp in expense)
        print("Total expenses:", total)

    elif choice == "4":
        search_name = input("Enter expense to search: ").strip().capitalize()
        found = False
        for exp in expense:
            if exp["name"] == search_name:
                print("Found:", exp["name"], "|", exp["amount"])
                found = True
        if not found:
            print("Expense not found")

    elif choice == "5":
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

    elif choice == "6":
        print("Exiting...")
        break


