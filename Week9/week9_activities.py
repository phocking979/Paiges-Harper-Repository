
# Read the file and create a customers list, where each element is a customer list or tuple
def load_data(file_path):
    """
    Reads a CSV-formatted text file and converts it into a list of tuples
    
    Args:
        file_path (str): The name or path of the text file
    Returns:
        list: A list of tuples containing customer data
    """
    customers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Skip the header row 
            next(file)
            for line in file:
                # Data processing with tuples and lists
                # Splitting by "," and stripping extra quotes from the raw text
                parts = [part.strip('"') for part in line.strip().split('","')]
                
                # Parameter/Data validation
                # Ensures we have the expected number of fields before creating a tuple
                if len(parts) >= 11:
                    customers.append(tuple(parts))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found")
    return customers

def sort_customers(customer_list, index):
    """
    Sorting function to avoid code duplication
    
    Args:
        customer_list (list): The list of customer tuples
        index (int): The tuple index to sort by (1 for Company, 2 for Contact)
    Returns:
        list: A new sorted list
    """
    return sorted(customer_list, key=lambda x: x[index].lower())

def search_customers(customer_list, search_term, index):
    """
    Search function for partial matches
    
    Args:
        customer_list (list): The list of customer tuples
        search_term (str): The string to look for
        index (int): The tuple index to search within
    Returns:
        list: Filtered list of matching tuples
    """
    results = []
    # Search for a given name or part of a name
    search_term = search_term.lower()
    for cust in customer_list:
        if search_term in cust[index].lower():
            results.append(cust)
    return results

# Separate functions for each type of processing
def display_records(customer_list, format_type="company"):
    """
    Handles all output formatting
    
    Args:
        customer_list (list): Data to display
        format_type (str): Dictates which columns to show or if labels are needed
    """
    if not customer_list:
        print("\nNo records found")
        return

    print("*" * 90)
    
    # Display company name, contact name, and phone (Sorted by Company)
    if format_type == "company":
        print(f"{'Company Name':<40} {'Contact Name':<25} {'Phone'}")
        for cust in customer_list:
            print(f"{cust[1]:<40} {cust[2]:<25} {cust[9]}")
            
    # Display contact name, company name, and phone (Sorted by Contact)
    elif format_type == "contact":
        print(f"{'Contact Name':<25} {'Company Name':<40} {'Phone'}")
        for cust in customer_list:
            print(f"{cust[2]:<25} {cust[1]:<40} {cust[9]}")
            
    # Display matching records with fields labeled for searches
    else:
        for cust in customer_list:
            print(f"COMPANY: {cust[1]}")
            print(f"CONTACT: {cust[2]}")
            print(f"PHONE:   {cust[9]}")
            print(f"LOCATION: {cust[5]}, {cust[8]}") # City, Country 
            print("*" * 30)
    print("*" * 90)

# Use a loop that shows a menu of options
def display_menu():
    # Prints the menu to the console
    print("\n*** Northwind Customer Management ***")
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")

def main():
    # Avoid global variables by passing parameters
    data = load_data('NorthwindCustomersTable.txt')
    
    if not data:
        return

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        # Call appropriate function for the option selection
        if choice == '1':
            sorted_data = sort_customers(data, 1) # Index 1 is CompanyName 
            display_records(sorted_data, "company")
        
        elif choice == '2':
            sorted_data = sort_customers(data, 2) # Index 2 is ContactName 
            display_records(sorted_data, "contact")
        
        elif choice == '3':
            term = input("Enter company name search term: ").strip()
            # Parameter validation (ensuring input isn't empty)
            if term:
                results = search_customers(data, term, 1)
                display_records(results, "labeled")
            else:
                print("Search term cannot be empty")
            
        elif choice == '4':
            term = input("Enter contact name search term: ").strip()
            if term:
                results = search_customers(data, term, 2)
                display_records(results, "labeled")
            else:
                print("Search term cannot be empty")
            
        elif choice == '5':
            print("Closing application")
            break
        
        else:
            print("Invalid input. Please choose 1 through 5")

if __name__ == "__main__":
    main()