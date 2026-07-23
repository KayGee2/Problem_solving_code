
contacts = []

def add_contact():
    print("Add contact")
    
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts.append(new_contact)
    print(f"✅ Contact '{name}' added successfully!")

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact

def delete_contact(name):
    contact = search_contact(name)
    if contact:
        contacts.remove(contact)
        print(f"Contact '{name}' deleted successfully!")
        return True
    else:
        print(f"Contact '{name}' not found!")
        return False

def view_all():
    """Display all contacts in a formatted layout"""
    if not contacts:
        print("📭 No contacts found. Add some contacts first!")
        return
    
    print(f"{'CONTACT LIST'} 📋")

    sorted_contacts = sorted(contacts, key=lambda x: x["name"].lower())
    
    for idx, contact in enumerate(sorted_contacts, 1):
        print(f"{idx}. {contact['name']}")
        print(f"   📞 Phone: {contact['phone']}")
        print(f"   📩 Email: {contact['email']}")
    
    print(f"Total number contacts: {len(contacts)}")

def display_menu():
    print("📇 CONTACT BOOK MENU")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

def main():
    print("🌟 Welcome to the Contact Book! 🌟")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_contact()
        
        elif choice == "2":
            print("Search Contact")
            name = input("Enter name to search: ").strip()
            if name:
                contact = search_contact(name)
                if contact:
                    print(f"✅ Contact found:")
                    print(f"   Name: {contact['name']}")
                    print(f"   Phone: {contact['phone']}")
                    print(f"   Email: {contact['email']}")
                else:
                    print(f"❌ Contact '{name}' not found!")
            else:
                print("❌ Please enter a name!")
        
        elif choice == "3":
            print(" Delete Contact ")
            name = input("Enter name to delete: ").strip()
            if name:
                delete_contact(name)
            else:
                print("❌ Please enter a name!")
        
        elif choice == "4":
            view_all(contact)
        
        elif choice == "5":
            print("👋 Thank you for using the Contact Book. Goodbye!😊")
            break
        
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")
        
    
        input("Press Enter to continue...")

