def main():
    # Define names of the files we're working with
    input_filename = 'names.txt'
    output_filename = 'nofound.txt'

    try:
        # Open the names.txt file in read mode 
        with open(input_filename, 'r') as file:
            names_list = [line.strip() for line in file.readlines()]

        # Create/open nofound.txt in append mode
        with open(output_filename, 'a') as output_file:
            
            # Infinite loop to keep asking for names
            while True:
                user_input = input("Enter a name (or type 'exit' to quit): ").strip()

                # Code for exiting
                if user_input.lower() == 'exit':
                    print("Exiting program.")
                    break

                # Search for the user's name in names_list
                if user_input in names_list:
                    # If found 
                    print(f"The name '{user_input}' is already in the file.")
                else:
                    # If NOT found
                    output_file.write(user_input + "\n")
                    
                    print(f"The name '{user_input}' has been written to {output_filename}.")

    # If names.txt is missing, show an error message
    except FileNotFoundError:
        print(f"Error: Could not find '{input_filename}'. Please ensure it is in the same folder.")

if __name__ == "__main__":
    main()