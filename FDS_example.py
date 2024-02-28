import sqlite3
# Connect to SQLite database (or create it if it doesn't exist)
connect= sqlite3.connect('contact_book.db')
cursor= connect.cursor()

# Create table
cursor.execute('''
    CREATE TABLE contacts
    (ID INTEGER PRIMARY KEY,
    Name TEXT,
    Cell TEXT,
    Email TEXT)
''')
# Insert 5 rows of data
data= [
    (1, 'Ganavi', '0987654321', 'ganu@example.com'),
    (2, 'kushi', '0987645321', 'kushi@example.com'),
    (3, 'shilpa', '1112223333', 'shilpa@example.com'),
    (4, 'janu', '4445556666', 'janu@example.com'),
    (5, 'poojitha', '1234567890', 'pooji@example.com'),
]
cursor.executemany('INSERT INTO contacts VALUES (?,?,?,?)', data)
# Commit the changes
connect.commit()
# Fetch all data
cursor.execute('SELECT * FROM contacts')
# Display all data
rows = cursor.fetchall()

print("ID\tName\t\tCell#\t\t\tEmail")
print("-" * 50)
for row in rows:
    print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

# Close the connection
connect.close()