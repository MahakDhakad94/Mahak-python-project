class ContactBook:
    def __init__(self):
        self.contacts = []  # List to store contacts
        self.unique_contacts = set()  # Set to store unique contacts

    def add_contact(self, name, number):
        contact = {'name': name, 'number': number}
        self.contacts.append(contact)
        self.unique_contacts.add(name.lower())  # Adding lowercased name to ensure uniqueness

    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact['name']}, Number: {contact['number']}")

    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                print(f"Contact found - Name: {contact['name']}, Number: {contact['number']}")
                found = True
                break
        if not found:
            print(f"No contact found for '{name}'.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                self.unique_contacts.remove(name.lower())
                print(f"Contact '{name}' removed.")
                break
        else:
            print(f"No contact found for '{name}'.")

# Sample usage:
contact_book = ContactBook()

# Adding contacts
contact_book.add_contact('Mahak', '1234567890')
contact_book.add_contact('Sejal', '9876543210')
contact_book.add_contact('Pratham', '1111111111')  # Duplicate name 'Mahak'

# Displaying contacts
contact_book.display_contacts()

# Searching for a contact
contact_book.search_contact('Pratham')


# Displaying updated contacts
contact_book.display_contacts()
