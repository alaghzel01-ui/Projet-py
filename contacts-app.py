contacts = []

while True:
    print("")
    print("1. Add contact")
    print("2. Show all contacts")
    print("3. Search contact")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contact = {"name": name, "phone": phone, "email": email}
        contacts.append(contact)
        print("Contact added!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet")
        else:
            print("")
            print("All contacts:")
            for contact in contacts:
                print("-", contact["name"], "|", contact["phone"], "|", contact["email"])

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"] == search_name:
                print("Found:", contact["name"], "|", contact["phone"], "|", contact["email"])
                found = True
        if not found:
            print("Contact not found")

    elif choice == "4":
        print("Goodbye,thank you!")
        break

    else:
        print("Invalid option")