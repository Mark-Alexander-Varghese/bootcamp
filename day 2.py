def menu():
    names = []
    while True:
        print("Menu:")
        print("1. To  Add Name")
        print("2. To Remove Name")
        print("3. Check if Name is Present")
        print("4. Display All Names")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter the name to add: ")
            names.append(name)
            print(f"{name} is added to the list.")
        elif choice == "2":
            name = input("Enter the name to remove: ")
            if name in names:
                names.remove(name)
                print(f"{name} has been removed from the list.")
            else:
                print(f"{name} not found in the list.")
        elif choice == "3":
            name = input("Enter name to check: ")
            if name in names:
                print(f"{name} is present in the list.")
            else:
                print(f"{name} is not in the list.")
        elif choice == "4":
            if names:
                print("List of Names:")
                for name in names:
                    print(f" {name}")
            else:
                print("The list is empty.")
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()

