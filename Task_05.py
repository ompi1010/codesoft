#****TASK 05****
#****CONTACT****
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        search_results = []
        for contact in self.contacts:
            if search_term in (contact.name.lower(), contact.phone_number):
                search_results.append(contact)
        return search_results

    def update_contact(self, name, new_contact):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management Application")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone_number = input("Phone Number: ")
            email = input("Email: ")
            address = input("Address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
        elif choice == "2":
            contact_manager.view_contact_list()
        elif choice == "3":
            search_term = input("Enter the name or phone number to search: ").lower()
            results = contact_manager.search_contact(search_term)
            if results:
                for contact in results:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == "4":
            name = input("Enter the name of the contact you want to update: ").lower()
            new_name = input("New Name: ")
            new_phone = input("New Phone Number: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_manager.update_contact(name, new_contact)
        elif choice == "5":
            name = input("Enter the name of the contact you want to delete: ").lower()
            contact_manager.delete_contact(name)
        elif choice == "6":
            print("Exiting the Contact Management Application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
