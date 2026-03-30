import csv

def load_customer_data(file_path):
    """
    Reads the Northwind text file and converts each row into a dictionary
    
    Args:
        file_path (str): The name/path of the source file
        
    Returns:
        list: A list where every element is a dictionary representing a customer
    """
    customers = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customers.append(row)
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return customers

def display_list(customer_list, sort_field, primary_label, secondary_label):
    """
    Function to sort and display specific customer fields in a table
    """
    if not customer_list:
        print("No data to display")
        return

    sorted_data = sorted(customer_list, key=lambda x: x[sort_field].lower())
    
    print(f"\n{'*'*85}")
    print(f"{primary_label:<40} | {secondary_label:<25} | {'Phone'}")
    print(f"{'*'*85}")
    
    for c in sorted_data:
        # Accessing dictionary values by their keys 
        print(f"{c[primary_label]:<40} | {c[secondary_label]:<25} | {c['Phone']}")

def search_records(customer_list, search_field, user_input):
    """
    Search function that looks for a substring within a specified field
    """
    # Validation
    if not user_input.strip():
        print("Search term cannot be empty")
        return

    #  Creates a new list of customers where the search term is found inside the specified field (not case sensitive)
    matches = [c for c in customer_list if user_input.lower() in c[search_field].lower()]
    
    if not matches:
        print(f"\nNo records found containing: '{user_input}'")
    else:
        print(f"\n--- Found {len(matches)} matches ---")
        for c in matches:
            print("-" * 30)
            # Iterates through all key-value pairs in the customer dictionary 
            for key, value in c.items():
                print(f"{key}: {value}")

def main():
    """
    Main program loop that provides the user interface
    """
    # Load the data from the source file 
    filename = "NorthwindCustomersTable.txt"
    customer_data = load_customer_data(filename)
    
    # If the list is empty (file error), stop the program
    if not customer_data:
        return

    # Navigation Menu
    while True:
        print("\nNorthwind Customer System")
        print("1. Display All (Sorted by Company)")
        print("2. Display All (Sorted by Contact)")
        print("3. Search by Company Name")
        print("4. Search by Contact Name")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            # Sort by Company, show Company first
            display_list(customer_data, 'CompanyName', 'CompanyName', 'ContactName')
            
        elif choice == '2':
            # Sort by Contact, show Contact first
            display_list(customer_data, 'ContactName', 'ContactName', 'CompanyName')
            
        elif choice == '3':
            term = input("Enter Company Name search term: ")
            search_records(customer_data, 'CompanyName', term)
            
        elif choice == '4':
            term = input("Enter Contact Name search term: ")
            search_records(customer_data, 'ContactName', term)
            
        elif choice == '5':
            print("Exiting program")
            break
            
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()