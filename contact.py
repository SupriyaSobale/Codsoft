contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print("Contact added successfully")

def view_contact_list():
    if not contacts:
        print("Contact list is empty")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone Number: {details['phone_number']}")

def search_contact():
    search_term = input("Enter contact name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term in [name, details['phone_number']]:
            print(f"Name: {name}, Phone Number: {details['phone_number']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("Contact not found")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contacts:
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new address: ")
        
        contacts[name]['phone_number'] = phone_number
        contacts[name]['email'] = email
        contacts[name]['address'] = address
        print("Contact updated successfully")
    else:
        print("Contact not found")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("Contact not found")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
