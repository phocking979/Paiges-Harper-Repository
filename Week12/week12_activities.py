import sqlite3
import os

# Function to connect to the Northwind database
def get_connection():
    # This finds the folder where this .py file is saved
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'Northwind.db')
    return sqlite3.connect(db_path)

# Gets a list of table names
def get_tables():
    conn = get_connection()
    cursor = conn.cursor()
    # Querying the master table to get user-created tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # Using a list comprehension to store names
    tables = [row[0] for row in cursor.fetchall() if row[0] != 'sqlite_sequence']
    conn.close()
    return tables

    # Displays all records with headers and row numbers using cursor.description
def display_table_data(table_name):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        # Use cursor.description to get field names for headings
        headers = [description[0] for description in cursor.description]
        rows = cursor.fetchall()

        # Print Headers
        print(f"\n--- TABLE: {table_name} ---")
        header_row = " | ".join(headers)
        print(f"Row # | {header_row}")
        print("-" * len(header_row) * 2)

        # Print data with Row Numbers
        for idx, row in enumerate(rows, start=1):
            print(f"{idx:<5} | {row}")
            
    except Exception as e:
        print(f"Error reading table: {e}")
    finally:
        conn.close()

# Insert a new record into selected table
def insert_record(table):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        if table == "Customers":
            cid = input("CustomerID: ")
            name = input("Contact Name: ")
            cursor.execute(
                "INSERT INTO Customers (CustomerID, ContactName) VALUES (?, ?)",
                (cid, name)
            )

        elif table == "Employees":
            fname = input("First Name: ")
            lname = input("Last Name: ")
            cursor.execute(
                "INSERT INTO Employees (FirstName, LastName) VALUES (?, ?)",
                (fname, lname)
            )

        elif table == "Products":
            pname = input("Product Name: ")
            price = input("Unit Price: ")

            # simple validation
            if not price.replace('.', '', 1).isdigit():
                print("Invalid price.")
                return

            cursor.execute(
                "INSERT INTO Products (ProductName, UnitPrice) VALUES (?, ?)",
                (pname, float(price))
            )

        conn.commit()
        print("Record inserted successfully.")

    except Exception as e:
        print("Insert error:", e)

    finally:
        conn.close()

# Update a specific field in a selected row
def update_record(table):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        display_table_data(table)

        # Get all rows so we can map row number to actual rowid
        cursor.execute(f"SELECT rowid, * FROM {table}")
        rows = cursor.fetchall()

        # Show rows again with correct numbering
        for i, row in enumerate(rows, start=1):
            print(f"{i}: {row}")

        # User selects row number
        row_choice = int(input("Enter row number to update: ")) - 1

        # Get actual rowid from selected row
        actual_rowid = rows[row_choice][0]

        # Ask for column and value
        field = input("Enter column name to update: ")

        # Get valid column names
        cursor.execute(f"SELECT * FROM {table}")
        valid_fields = [desc[0] for desc in cursor.description]

        if field not in valid_fields:
            print("Invalid column name.")
            return

        new_value = input("Enter new value: ")

        # Update using correct rowid
        query = f"UPDATE {table} SET {field} = ? WHERE rowid = ?"
        cursor.execute(query, (new_value, actual_rowid))

        conn.commit()
        print("Record updated successfully.")

    except Exception as e:
        print("Update error:", e)

    finally:
        conn.close()

# Delete a selected record
def delete_record(table):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        display_table_data(table)

        cursor.execute(f"SELECT rowid, * FROM {table}")
        rows = cursor.fetchall()

        for i, row in enumerate(rows, start=1):
            print(f"{i}: {row}")

        row_choice = int(input("Enter row number to delete: ")) - 1
        actual_rowid = rows[row_choice][0]

        cursor.execute(f"DELETE FROM {table} WHERE rowid = ?", (actual_rowid,))
        conn.commit()

        print("Record deleted successfully.")

    except Exception as e:
        print("Delete error:", e)

    finally:
        conn.close()

# Allows user to Insert, Update, or Delete records
def modify_data():
    allowed = ["Customers", "Employees", "Products"]

    print(f"\nChoose table to modify: {allowed}")
    table = input("Table: ")

    if table not in allowed:
        print("Invalid table.")
        return

    action = input("(I)nsert, (U)pdate, (D)elete: ").upper()

    if action == "I":
        insert_record(table)

    elif action == "U":
        update_record(table)

    elif action == "D":
        delete_record(table)

    else:
        print("Invalid action.")

# The user interface for the assignment
def main_menu():
    while True:
        print("\nNorthwind Database Activity")
        print("1. View Tables and Records")
        print("2. Modify Records")
        print("3. Exit")
        
        user_choice = input("Choose an option: ")
        
        if user_choice == '1':
            all_tables = get_tables()
            print(f"Available tables: {all_tables}")
            selected = input("Type the name of the table to view: ")
            if selected in all_tables:
                display_table_data(selected)
            else:
                print("Table not found.")
                
        elif user_choice == '2':
            modify_data()
            
        elif user_choice == '3':
            print("Exiting.")
            break

if __name__ == "__main__":
    main_menu()
