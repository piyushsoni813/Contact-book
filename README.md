# Contact Book

A simple and intuitive command-line contact management application built with Python. Easily manage your contacts with add, view, search, update, and delete functionalities.

## Features

- **Add Contact**: Create new contacts with name, phone, email, and address
- **View Contacts**: Display all contacts in your contact book
- **Search Contact**: Find a specific contact by name
- **Update Contact**: Modify an existing contact's information
- **Delete Contact**: Remove contacts from your contact book
- **Interactive Menu**: User-friendly command-line interface

## Project Structure

```
Contact-book/
├── main.py          # Main application with Contact and ContactBook classes
├── contact.json     # Sample contact data (JSON format)
├── README.md        # This file
└── LICENSE          # Apache License 2.0
```

## Requirements

- Python 3.6+
- No external dependencies required

## Usage

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/piyushsoni813/Contact-book.git
   cd Contact-book
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Follow the menu prompts**:
   ```
   ===== CONTACT BOOK =====
   1. Add Contact
   2. View Contacts
   3. Search Contact
   4. Update Contact
   5. Delete Contact
   6. Exit
   ```

## How to Use Each Feature

### 1. Add Contact
- Select option `1` from the menu
- Enter the contact's name, phone number, email, and address
- The contact will be saved to the contact book

### 2. View Contacts
- Select option `2` from the menu
- All contacts will be displayed with their complete information

### 3. Search Contact
- Select option `3` from the menu
- Enter the contact's name to search
- The matching contact details will be displayed

### 4. Update Contact
- Select option `4` from the menu
- Enter the name of the contact you want to update
- Provide the new phone number, email, and address
- The contact information will be updated

### 5. Delete Contact
- Select option `5` from the menu
- Enter the name of the contact you want to delete
- The contact will be removed from the contact book

### 6. Exit
- Select option `6` to exit the application

## Code Architecture

### Contact Class
Represents a single contact with the following attributes:
- `name`: Contact's full name
- `phone`: Contact's phone number
- `email`: Contact's email address
- `address`: Contact's physical address

### ContactBook Class
Manages multiple contacts and provides the following methods:
- `add_contact()`: Add a new contact
- `view_contacts()`: Display all contacts
- `search_contact()`: Find a contact by name
- `update_contact()`: Update contact information
- `delete_contact()`: Remove a contact

## Sample Data

The `contact.json` file contains 50 sample contacts with diverse names and locations across India, useful for testing and demonstration purposes.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Author

Created by [piyushsoni813](https://github.com/piyushsoni813)

## Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests with improvements

## Future Enhancements

Potential features for future versions:
- Persistent storage (JSON/Database integration)
- Contact categories or groups
- Birthday reminders
- Contact image support
- Export contacts to various formats (CSV, vCard, etc.)
- Advanced search and filtering options
- Duplicate contact detection
