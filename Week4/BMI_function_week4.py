import sys
def calculate_bmi():
    '''
    calculate bmi based on inputs of height and weight

    Args: none

    return: none
    '''
    # 2: Show exception handling using Python code specific to exception handling
    try:
        # 1: Data type validation (Input Validation)
        print("--- BMI Calculator ---")
        try:
            weight_lb = float(input("Enter weight in lbs: "))
            height_ft = int(input("Enter feet: "))
            height_in = int(input("Enter inches: "))
        except ValueError:
            print("Error: Please enter numeric values only.")
            sys.exit()

        # 1: Range and constraint validation (Parameter Validation)
        # 3: Use of a nested if statement to validate height constraints
        if weight_lb > 0 and weight_lb <= 1000:
            if height_ft >= 0 and height_ft <= 8:
                if height_in >= 0 and height_in < 12:
                    total_inches = (height_ft * 12) + height_in
                else:
                    raise ValueError("Inches must be between 0 and 11.")
            else:
                raise ValueError("Height in feet must be between 0 and 8.")
        else:
            raise ValueError("Weight must be between 1 and 1000 lbs.")

        # Final check for total height logic
        if total_inches <= 0:
            raise ValueError("Total height must be greater than zero.")

        # Calculation
        bmi = (weight_lb / (total_inches ** 2)) * 703

        # Assertion to assure valid parameters are passed to the output phase
        assert isinstance(bmi, float), "BMI result must be a float."
        assert bmi > 0, "BMI must be a positive value."

        # Output
        print(f"\nYour calculated BMI is: {bmi:.1f}")
        print("BMI VALUE LEGEND (Source: https://en.wikipedia.org/wiki/Body_mass_index)")
        print("Underweight: Less than 18.5")
        print("Normal weight: 18.5 - 24.9")
        print("Overweight: 25.0 - 29.9")
        print("Obesity: 30.0 or greater")

    # 2: Exception handling block to catch errors and terminate gracefully
    except (ValueError, TypeError, AssertionError) as e:
        print(f"Program Terminated: {e}")
        sys.exit()

calculate_bmi()