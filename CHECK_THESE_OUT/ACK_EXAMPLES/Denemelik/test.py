import tkinter as tk
from tkinter.filedialog import askopenfilename

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog and get file path as a string
    file_path = askopenfilename()

    # Ensure file_path is a string before opening the file
    if isinstance(file_path, str) and file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    else:
        print("No file selected or invalid file path.")

# Call the function to select and read the file
select_file()