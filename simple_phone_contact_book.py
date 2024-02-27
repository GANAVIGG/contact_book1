import sqlite3

# Function to create a new contact
def create_contact(conn, name, cell_number, email):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO contacts (name, cell_number, email) VALUES (?, ?, ?)''', (name, cell_number, email))
    conn.commit()
    print("Contact created successfully")

# Function to display all contacts
def display_contacts(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM contacts''')
    contacts = cursor.fetchall()
    print("ID\tName\tCell Number\tEmail")
    for contact in contacts:
        print(f"{contact[0]}\t{contact[1]}\t{contact[2]}\t{contact[3]}")

# Function to connect to the database
def connect_to_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                             name TEXT,
                                                             cell_number TEXT,
                                                             email TEXT)''')
    return conn

# Main function
def main():
    db_name = 'contacts.db'
    conn = connect_to_db(db_name)

    while True:
        print("\n1. Create Contact")
        print("2. Display Contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            cell_number = input("Enter cell number: ")
            email = input("Enter email: ")
            create_contact(conn, name, cell_number, email)
        elif choice == '2':
            display_contacts(conn)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
