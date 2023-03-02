import tkinter as tk
from ttkbootstrap import Style

# Create the window
root = tk.Tk()
root.title("Shape Calculator")
root.geometry('300x200')

# Create a style
style = Style()

# Create a frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Create a label for the shape selection
shape_label = tk.Label(frame, text="Select a shape:")
shape_label.grid(row=0, column=0)
# Create a dropdown for the shape selection
shapes = ["Triangle", "Square", "Rectangular"]
shape_var = tk.StringVar()
shape_dropdown = tk.OptionMenu(frame, shape_var, *shapes)
shape_dropdown.grid(row=0, column=1)

# Create a label for the operation selection
operation_label = tk.Label(frame, text="Select an operation:")
operation_label.grid(row=1, column=0)
# Create a dropdown for the operation selection
operations = ["Perimeter", "Area"]
operation_var = tk.StringVar()
operation_dropdown = tk.OptionMenu(frame, operation_var, *operations)
operation_dropdown.grid(row=1, column=1)

# Create labels and entry boxes for the dimensions
dim1_label = tk.Label(frame, text="Dimension 1:")
dim1_label.grid(row=2, column=0)
dim1_entry = tk.Entry(frame)
dim1_entry.grid(row=2, column=1)
dim2_label = tk.Label(frame, text="Dimension 2:")
dim2_label.grid(row=3, column=0)
dim2_entry = tk.Entry(frame)
dim2_entry.grid(row=3, column=1)

# Create a function to calculate the result
def calculate():
    shape = shape_var.get()
    operation = operation_var.get()
    dim1 = float(dim1_entry.get())
    dim2 = float(dim2_entry.get())
    
    if shape == "Triangle":
        if operation == "Perimeter":
            result = dim1 + dim2 + math.sqrt(dim1**2 + dim2**2)
        elif operation == "Area":
            result = 0.5 * dim1 * dim2
    elif shape == "Square":
        if operation == "Perimeter":
            result = 4 * dim1
        elif operation == "Area":
            result = dim1**2
    elif shape == "Rectangular":
        if operation == "Perimeter":
            result = 2 * (dim1 + dim2)
        elif operation == "Area":
            result = dim1 * dim2
    
    # Update the result label
    result_label.configure(text=f"{operation} of {shape} = {result}")

# Create a button to calculate the result
calculate_button = tk.Button(frame, text="Calculate", command=calculate )
calculate_button.grid(row=4, column=0)

# display the result
result_label = tk.Label(frame, text="")
result_label.grid(row=4, column=1)

root.mainloop()
