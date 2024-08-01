import sqlite3

#Create a connection to the SQLite database
def create_connection():
    try:
        connection = sqlite3.connect("library.sqlite3")
        return connection
    except Exception as e:
          print(e)

#Create the books table if it doesnot exist
def create_table(connection):
   CREATE_BOOK_TABLE_QUERY="""
        CREATE TABLE IF NOT EXISTS books(
		id INTEGER PRIMARY KEY,
		title TEXT NOT NULL,
		author TEXT NOT NULL,
		year INTEGER,
		isbn TEXT
        );
    """
   
cursor = connection.cursor()
cursor.execute(CREATE_BOOK_TABLE_QUERY)
print("Successfully created table.")


#from library_db import add_book, view_books, update_book, delete_book

# Menu for the Library Management System
def menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete book")
    print("5. Exit")

    choice = input("Enter choice:")
    return choice


# Main function to run the library management system
def main():
     connection = create_connection()
     create_table(connection)
     while True:
        choice = menu()
        if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                year = int(input("Enter year: "))
                isbn = input("Enter ISBN: ")
                add_book(title, author, year, isbn)
        
        elif choice == '3':
                id = int(input("Enter book ID to update: "))
                title = input("Enter new title: ")
                author = input("Enter new author: ")
                year = int(input("Enter new year: "))
                isbn = input("Enter new ISBN: ")
                update_book(id, title, author, year, isbn)
        elif choice == '4':
                id = int(input("Enter book ID to delete: "))
                delete_book(id)
        elif choice == '5':
                break
        else:
                print("Invalid choice. Please try again.")


# Add a new book to the books table
def add_book(title, author ,year,isbn):
    connection = create_connection()
    cursor = connection.cursor()
        
    cursor.execute("INSERT INTO books(title, author, year,isbn) VALUES(?,?,?,?)", (title, author, year,isbn))
    connection.commit()
    connection.close()

def view_books():
       connection = create_connection()
       cursor = connection.cursor()
       cursor.execute("SELECT * FROM books")
       rows = cursor.fetchall()
       connection.close()
       return rows
#Update an existing book in the books table
def update_book(id,title,author,year,isbn):
     connection = create_connection()
     cursor = connection.cursor()
     cursor.execute("UPDATE books SET title=?, author =?, year=?,isbn=? WHERE id=?",
               (title, author, year,isbn,id))
     connection.commit()
     connection.close()


#Delete a book from the books table
def delete_book(id):
     connection = create_connection()
     cursor = connection.cursor()
     cursor.execute("DELETE FROM books WHERE id = ?", (id,))
     connection.commit()
     connection.close()


if __name__ == "__main__":
     main()