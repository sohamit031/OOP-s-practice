import json

# 1. LOAD DATA
try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = []

while True:
    print("\n--- SMART CONTACT BOOK ---")
    print(f"Total Contacts: {len(contacts)}")
    print("1. Add Contact")
    print("2. View All")
    print("3. Delete Contact")  # <--- NEW OPTION
    print("4. Exit")
    
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        person = {"name": name, "phone": phone}
        contacts.append(person)
        
        # SAVE
        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
        print("Saved!")

    elif choice == "2":
        print("\nMy Contacts:")
        for c in contacts:
            print(f"- {c['name']}: {c['phone']}")
            
    elif choice == "3":  # <--- DELETE LOGIC
        name_to_delete = input("Name to delete: ")
        found = False
        for person in contacts:
            if person["name"] == name_to_delete:
                contacts.remove(person)  # <--- THE MAGIC LINE
                found = True
                print(f"Deleted {name_to_delete}!")
                
                # SAVE IMMEDIATELY
                with open("contacts.json", "w") as f:
                    json.dump(contacts, f)
                break 
        
        if not found:
            print("Contact not found.")

    elif choice == "4":
        print("Goodbye!")
        break