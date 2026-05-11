import tkinter as tk
from tkinter import messagebox

def calculate_goal():
    """
    this function handles the core logic:
    first retrieves data from the form
    second validates that the input is numeric
    third performs a calculation and displays the result
    """
    user_name = name_entry.get()
    raw_protein = protein_entry.get()

    # guideline 3: check if the numeric field is actually a number
    try:
        protein_value = float(raw_protein)
    except ValueError:
        # display a popup message indicating the error
        messagebox.showerror("Input Error", "Please enter a valid number for protein grams.")
        return
    
    # guideline 5: string manipulation and calculation
    # calculates total calories from protein (4 calories per gram)
    total_calories = protein_value * 4
    result_text = f"Hello {user_name.strip().title()}! {protein_value}g of protein is {total_calories} calories."

    # guideline 6: show output after button click
    output_label.config(text=result_text, fg="green")

# guideline 1: create the main form
root = tk.Tk()
root.title("Nutrition Goal Tracker")
root.geometry("400x300")

# guideline 2: create labels and text boxes
tk.Label(root, text="Enter Your Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Enter Protein Grams:").pack(pady=5)
protein_entry = tk.Entry(root)
protein_entry.pack(pady=5)

# guideline 4: create a click button to trigger the process
calc_button = tk.Button(root, text="Calculate Calories", command=calculate_goal)
calc_button.pack(pady=20)

# label for displaying results
output_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
output_label.pack(pady=10)

# start the application
root.mainloop()