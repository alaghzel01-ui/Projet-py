contacts = []

while True:
    print("")
    print("1. Add contact")
    print("2. Show all contacts")
    print("3. Search contact")
    print("4. update contact")
    print("5. Delete contact")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        name = input("Enter name: ").strip().capitalize()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
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
        search_name = search_name.strip().capitalize()
        found = False
        for contact in contacts:
            if contact["name"] == search_name:
                print("Found:", contact["name"], "|", contact["phone"], "|", contact["email"])
                found = True
        if not found:
            print("Contact not found")

    elif choice == "4":
        update_name = input("Enter name of contact to update: ")
        update_name = update_name.strip().capitalize()
        found = False
        for contact in contacts:
            if contact["name"] == update_name:
                print("Found:", contact["name"], "|", contact["phone"], "|", contact["email"])
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email address: ")
                contact["phone"] = new_phone
                contact["email"] = new_email
                print("Contact updated!")
                found = True
                break
        if not found:
            print("Contact not found")

    elif choice == "5":
        delete_name = input("Enter name to delete: ")
        delete_name = delete_name.strip().capitalize()
        found = False
        for contact in contacts:
            if contact["name"] == delete_name:
                contacts.remove(contact)
                print("Contact deleted:", contact["name"])
                found = True
                break
        if not found:
            print("Contact not found")

    elif choice == "6":
        print("Goodbye,thank you!")
        break

    else:
        print("Invalid option")