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
contact_book.add_contact('Mahak', '9897972138')
contact_book.add_contact('Sejal', '9838837838')
contact_book.add_contact('Sohan', '9468478928')
contact_book.add_contact('Aditi', '9446378291')
contact_book.add_contact('Sures', '8835735728')
contact_book.add_contact('Mahes', '8835653765')
contact_book.add_contact('Rohan', '9863763678')
contact_book.add_contact('Bilal', '9937378294')
contact_book.add_contact('Swety', '8845375694')
contact_book.add_contact('Sweta', '9824266277')


# Displaying contacts
contact_book.display_contacts()

# Searching for a contact
contact_book.search_contact('Pratham')


# Displaying updated contacts
contact_book.display_contacts()
