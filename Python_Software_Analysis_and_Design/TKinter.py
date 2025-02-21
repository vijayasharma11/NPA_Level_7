import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Text Entry Display")

# Create a Label to display instructions
label = tk.Label(root, text="Enter text:")
label.pack(pady=10)

# Create an Entry widget for user to enter text
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Function to display the entered text
def display_text():
    entered_text = entry.get()  # Get the text entered by the user
    result_label.config(text=f"You entered: {entered_text}")  # Update the result label

# Create a Button to trigger the display function
submit_button = tk.Button(root, text="Submit", command=display_text)
submit_button.pack(pady=10)

# Create a Label to display the result of the entered text
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
