contacts = {}
while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        email = input("Enter email: ")
        contacts[name] = {"number": number, "email": email}
        print("Contact added!")
    elif choice == "2":
        for name, info in contacts.items():
            print(f"\nName: {name}")
            print(f"Number: {info['number']}")
            print(f"Email: {info['email']}")
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            info = contacts[name]
            print(f"\nName: {name}")
            print(f"Number: {info['number']}")
            print(f"Email: {info['email']}")
        else:
            print("Contact not found!")
    elif choice == "4":
        break
    else:
        print("Invalid choice!")