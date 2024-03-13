class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class BusinessManagement:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
        else:
            print("No contacts available.")

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            print("Matching contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
        else:
            print("No matching contacts found.")

# Example usage:
if __name__ == "__main__":
    business_management = BusinessManagement()
    
    # Adding contacts
    contact1 = Contact("John Doe", "john@example.com", "1234567890")
    contact2 = Contact("Jane Smith", "jane@example.com", "9876543210")
    business_management.add_contact(contact1)
    business_management.add_contact(contact2)
    
    # Displaying contacts
    business_management.display_contacts()
    
    # Searching contact
    business_management.search_contact("John Doe")
