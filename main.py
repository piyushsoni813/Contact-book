# ==========================
# CLASS
# Blueprint for one contact.
# Every contact will have the same structure.
# ==========================
class Contact:

    # CONSTRUCTOR
    # Runs automatically when a Contact object is created.
    def __init__(self, name: str, phone: str, email: str, address: str):

        # ATTRIBUTES
        # Store information that belongs to THIS contact.
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    # METHOD
    # Behavior that every Contact can perform.
    def display(self):

        # RETURN
        # Give the formatted contact information back.
        return (
            f"Name: {self.name}\n"
            f"Phone: {self.phone}\n"
            f"Email: {self.email}\n"
            f"Address: {self.address}"
        )


# ==========================
# CLASS
# Manages many Contact objects.
# ==========================
class ContactBook:

    # CONSTRUCTOR
    # Create an empty ContactBook.
    def __init__(self):

        # ATTRIBUTE
        # Empty list to store Contact objects.
        self.contacts = []

    # METHOD
    # Add a Contact object to the book.
    def add_contact(self, contact: Contact):

        # PARAMETER
        # 'contact' is the object received by this method.

        # APPEND
        # Save the object inside the list.
        self.contacts.append(contact)

        print("Contact added successfully.")

    # METHOD
    # Show every contact in the book.
    def view_contacts(self):

        # Check if the book is empty.
        if not self.contacts:
            print("No contacts found.")
            return

        # LOOP
        # Visit one Contact object at a time.
        for contact in self.contacts:

            # METHOD CALL
            # Ask the Contact object to display itself.
            print(contact.display())

            print("-" * 30)

    # METHOD
    # Find a contact by name.
    def search_contact(self, name: str):

        # LOOP
        # Check every Contact until a match is found.
        for contact in self.contacts:

            # ATTRIBUTE ACCESS
            if contact.name == name:

                # RETURN
                # Give the found Contact back.
                return contact

        print("Contact not found.")
        return None

    # METHOD
    # Remove a contact from the book.
    def delete_contact(self, name: str):

        for contact in self.contacts:

            if contact.name == name:

                # REMOVE
                # Delete the Contact object from the list.
                self.contacts.remove(contact)

                print("Contact deleted successfully.")
                return

        print("Contact not found.")

    # METHOD
    # Change a contact's information.
    def update_contact(self,
                       name: str,
                       phone: str,
                       email: str,
                       address: str):

        for contact in self.contacts:

            if contact.name == name:

                # ATTRIBUTE UPDATE
                # Replace old values with new ones.
                contact.phone = phone
                contact.email = email
                contact.address = address

                print("Contact updated successfully.")
                return

        print("Contact not found.")


# OBJECT
# Create one ContactBook object.
book = ContactBook()


# WHILE LOOP
# Keep the program running until Exit is chosen.
while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    # INPUT
    # Get the user's menu choice.
    choice = input("Enter your choice: ")

    if choice == "1":

        # LOCAL VARIABLES
        # Store user input temporarily.
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        # OBJECT CREATION
        # Build one Contact object.
        contact = Contact(name, phone, email, address)

        # METHOD CALL
        # Store it inside the ContactBook.
        book.add_contact(contact)

    elif choice == "2":

        book.view_contacts()

    elif choice == "3":

        name = input("Enter name to search: ")

        # RETURN VALUE
        # Receive either a Contact or None.
        contact = book.search_contact(name)

        if contact:
            print(contact.display())

    elif choice == "4":

        name = input("Enter name to update: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        book.update_contact(name, phone, email, address)

    elif choice == "5":

        name = input("Enter name to delete: ")

        book.delete_contact(name)

    elif choice == "6":

        print("Thank you for using Contact Book!")

        # BREAK
        # Stop the infinite loop and exit.
        break

    else:

        print("Invalid choice. Please try again.")
