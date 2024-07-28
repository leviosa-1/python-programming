import tkinter as tk

def on_button_click(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display input and results
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify='right', font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4) 

# Define the button layout
button_layout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place the buttons
for (text, row, column) in button_layout:
    if text == 'C':
        button = tk.Button(root, text=text, command=clear_entry, padx=20, pady=20, font=('Arial', 12))
    elif text == '=':
        button = tk.Button(root, text=text, command=calculate_result, padx=20, pady=20, font=('Arial', 12))
    else:
        button = tk.Button(root, text=text, command=lambda t=text: on_button_click(t), padx=20, pady=20, font=('Arial', 12))
    button.grid(row=row, column=column)

# Run the Tkinter event loop
root.mainloop()
