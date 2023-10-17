contacts = {}
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"{name} has been added to your contacts Book.")

def view_contacts():
    if not contacts:
        print("Your contact list is empty.")
    else:
        print("Your Contact Book:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {contact_info['Phone']}")
            print(f"Email: {contact_info['Email']}")
            print(f"Address: {contact_info['Address']}")
            print("")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found = False

    for name, contact_info in contacts.items():
        if search_term in (name, contact_info['Phone']):
            print(f"Name: {name}")
            print(f"Phone: {contact_info['Phone']}")
            print(f"Email: {contact_info['Email']}")
            print(f"Address: {contact_info['Address']}")
            found = True

    if not found:
        print(f"No contact found with the name or phone number: {search_term}")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        address = input("Enter the new address: ")

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"{name}'s contact information has been updated.")
    else:
        print(f"No contact found with the name: {name}")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name}'s contact has been deleted.")
    else:
        print(f"No contact found with the name: {name}")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
