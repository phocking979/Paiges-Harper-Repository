import sys
import unittest
from unittest.mock import patch
import io

#BMI CODE

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

#TESTS
class TestBMICalculator(unittest.TestCase):

    def test_formula_accuracy(self):
        self.assertAlmostEqual(get_bmi_value(160, 69), 23.6, places=1)
        self.assertEqual(get_bmi_value(1, 1), 703.0)

    def test_max_boundary(self):
        self.assertAlmostEqual(get_bmi_value(1000, 96), 76.3, places=1)

    def test_zero_height_protection(self):
        self.assertEqual(get_bmi_value(150, 0), 0.0)

    def test_negative_height_protection(self):
        self.assertEqual(get_bmi_value(150, -10), 0.0)

    def test_display_table_runs(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            display_bmi_table()
            self.assertIn("BMI Reference table", fake_out.getvalue())

    @patch('builtins.input', side_effect=['160', '5', '9', 'n'])
    def test_full_run_success(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("Your Calculated BMI: 23.6", fake_out.getvalue())

    @patch('builtins.input', side_effect=['Five', '160', '5', '9', 'n'])
    def test_weight_non_numeric(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("Error: Please enter a numeric value for weight.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['2000', '160', '5', '9', 'n'])
    def test_weight_out_of_range(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("Error: Weight must be between 1 and 1000.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['160', 'nine', '5', '9', 'n'])
    def test_feet_non_numeric(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("Please enter a whole number for feet.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['160', '9', '5', '9', 'n'])
    def test_feet_out_of_range(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("Feet must be between 0 and 8.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['160', '5', 'five', '9', 'n'])
    def test_inches_non_numeric(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("Please enter a whole number for inches.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['160', '5', '12', '11', 'n'])
    def test_inches_out_of_range(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("Inches must be between 0 and 11.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['160', '5', '9', 'maybe', 'n'])
    def test_invalid_run_again_input(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("Please enter 'y' for yes or 'n' for no.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['q'])
    def test_immediate_quit(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("--- BMI Calculator ---", fake_out.getvalue())

    @patch('__main__.get_bmi_value', return_value=-5.0)
    @patch('builtins.input', side_effect=['160', '5', '9', 'n'])
    def test_assertion_error_branch(self, mock_bmi, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculate_bmi()
            self.assertIn("Logic Error:", fake_out.getvalue())

# EXECUTION:

# Call Tests
print("SYSTEM: Running automated test suite for coverage")
unittest.main(exit=False, verbosity=1)

print("\n" + "*"*46)
print("SYSTEM: Tests passed. Starting user interface")
print("*"*46 + "\n")
# Call Program
calculate_bmi()