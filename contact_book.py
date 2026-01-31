# 1. Start with an empty list
contacts = []

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View All")
    print("3. Exit")
    
    choice = input("Choose (1/2/3): ")
    
    if choice == "1":
        # GET INFO
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        
        # STEP A: Create the dictionary
        person = {
            "name": name,
            "phone": phone
        }
        
        # STEP B: Add to the list
        contacts.append(person)
        
        print("Saved!")

    elif choice == "2":
        print("\nMy Contacts:")
        for c in contacts:
            # We access the keys we created in Step A
            print(c["name"] + ": " + c["phone"])
            
    elif choice == "3":
        print("Goodbye!")
        break