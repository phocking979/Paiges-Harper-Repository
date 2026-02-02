def calculate_bmi():
    '''
    calculate bmi based on inputs of height and weight

    Args: none

    return: none
    '''
    weight_lb = float(input("Enter your weight in pounds (lbs): "))
    height_ft = int(input("Enter your height (feet part): "))
    height_in = int(input("Enter your height (inches part): "))

    total_inches = (height_ft * 12) + height_in

    bmi = (weight_lb / (total_inches ** 2)) * 703

    print(f"\nYour calculated BMI is: {bmi:.1f}")
    print("BMI VALUE LEGEND (Source: https://en.wikipedia.org/wiki/Body_mass_index)")
    print("Underweight: Less than 18.5")
    print("Normal weight: 18.5 - 24.9")
    print("Overweight: 25.0 - 29.9")
    print("Obesity: 30.0 or greater")

calculate_bmi()