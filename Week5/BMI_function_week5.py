import sys

# Helper function to reuse the BMI formula logic.
def get_bmi_value(weight_lb, total_inches):
    if total_inches <= 0: return 0.0
    return (weight_lb / (total_inches ** 2)) * 703

# Displays a BMI table from 100-250 lbs and 58-76 inches.
def display_bmi_table():
    """
    Displays a BMI table from 100-250 lbs and 58-76 inches.
    """
    print("\n" + "="*60)
    print("BMI Reference table (Height vs Weight)")
    print("="*60)

    # Print Header (Heights 58 to 76 in 2-inch steps)
    header = "WT/HT |"
    for h in range(58, 78, 2):
        header += f"{h:^5}\""
    print(header)
    print("-" * len(header))

    # Print Rows (Weights 100 to 250 in 10-lb steps)
    for w in range(100, 260, 10):
        row = f"{w:<5} |"
        for h in range(58, 78, 2):
            bmi = get_bmi_value(w, h)
            row += f"{bmi:6.1f}"
        print(row)
    print("-" * len(header))

def calculate_bmi():
    '''
    calculate bmi based on inputs of height and weight

    Args: 
        None
    Returns: 
        None
    Raises:
        ValueError: If inputs are non-numeric or out of valid range.
        TypeError: If an operation is performed on incompatible types.
        AssertionError: If the internal BMI calculation fails logic checks.    
    '''
    print("--- BMI Calculator ---")
    print("Instructions: Enter numeric values or 'q' to quit.")

    while True:
        # Weight Input & Validation
        while True:
            weight_in = input("\nEnter weight in lbs: ").strip().lower()
            if weight_in == 'q': return
            try:
                weight_lb = float(weight_in)
                if 1 <= weight_lb <= 1000:
                    break
                print("Error: Weight must be between 1 and 1000.")
            except ValueError:
                print("Error: Please enter a numeric value for weight.")

        # Feet Input & Validation 
        while True:
            feet_in = input("Enter feet: ").strip().lower()
            if feet_in == 'q': return
            try:
                height_ft = int(feet_in)
                if 0 <= height_ft <= 8:
                    break
                print(" Error: Feet must be between 0 and 8.")
            except ValueError:
                print(" Error: Please enter a whole number for feet.")

        # Inches Input & Validation
        while True:
            inches_in = input("Enter inches: ").strip().lower()
            if inches_in == 'q': return
            try:
                height_in = int(inches_in)
                if 0 <= height_in < 12:
                    break
                print(" Error: Inches must be between 0 and 11.")
            except ValueError:
                print(" Error: Please enter a whole number for inches.")

        # Calculation & Logic Check
        total_inches = (height_ft * 12) + height_in
        
        try:
            # Reused Formula Logic
            bmi = get_bmi_value(weight_lb, total_inches)
            
            assert isinstance(bmi, float), "Result must be a float."
            assert bmi > 0, "BMI must be a positive number."

            # Output 
            print(f"\nYour Calculated BMI: {bmi:.1f}")
            
            # Display the table after the result
            display_bmi_table()

            print("\nBMI Value Legend")
            print("Underweight: < 18.5 | Normal: 18.5-24.9 | Overweight: 25-29.9 | Obese: 30+")

        except (AssertionError, ZeroDivisionError) as e:
            print(f"Logic Error: {e}")

        # Loop Control 
        while True:
            again = input("\nWould you like to run another calculation? (y/n): ").lower()
            if again in ('y', 'yes'):
                break 
            if again in ('n', 'no', 'q', 'quit'):
                print("\nProgram closed. Have a great day!")
                return 
            print("Please enter 'y' for yes or 'n' for no.")

calculate_bmi()
