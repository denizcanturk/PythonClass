import tkinter as tk
from tkinter import ttk
import random  # For simulating sensor readings
from projectLibs.worker import Worker
from projectLibs.dbmanager import Database


# Assuming the Database class is in the same file or imported from another module
# from your_database_module import Database  

class Application(tk.Tk):
    def __init__(self, db_file):
        super().__init__()
        self.title("İlk Pencerem")
        self.geometry("900x600")

        # Initialize the database
        self.db = Database(db_file)
        print("Database initialized")

        # Fetch recipes from the database
        self.recipes = self.db.fetch_recipes()
        print("Fetched recipes:", self.recipes)  # Debugging statement

        # Setup Frames
        self.setup_frames()

        # Setup Widgets
        self.setup_widgets()

        # Create a SensorReader to update sensor readings every 5 seconds
        self.SensorReader = Worker(5, self.update_sensor_readings)
        self.SensorReader.start()

        # Bind combobox selection change to the update function
        self.cmbSecim.bind("<<ComboboxSelected>>", self.update_entries)

    def setup_frames(self):
        self.ustFrame = tk.Frame(self, borderwidth=2, relief="ridge")
        self.ustFrame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        self.ortaFrame = tk.Frame(self, borderwidth=2, relief="ridge")
        self.ortaFrame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.altFrame = tk.Frame(self, borderwidth=2, relief="ridge")
        self.altFrame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        for i in range(8):
            if i > 5:
                self.altFrame.columnconfigure(i, weight=1)
            else:
                self.ortaFrame.columnconfigure(i, weight=1)
                self.ustFrame.columnconfigure(i, weight=1)
                self.altFrame.columnconfigure(i, weight=1)

    def setup_widgets(self):
        self.setup_frame1_widgets()
        self.setup_frame2_widgets()
        self.setup_frame3_widgets()

    def setup_frame1_widgets(self):
        lblFrm1Title = tk.Label(self.ustFrame, text="SENSOR READS", font=("Arial", 16), bd=1, relief="ridge")
        lblFrm1Title.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

        labels = ["CO2", "Ph", "Su S", "Ort S", "Nem", "EC"]
        for i, text in enumerate(labels):
            tk.Label(self.ustFrame, text=text, font=("Arial", 16), bd=1, relief="sunken").grid(row=1, column=i, padx=5, pady=5, sticky="nswe")

        self.sensor_labels = []
        for i in range(6):
            sensor_label = tk.Label(self.ustFrame, text="", font=("Arial", 16), bd=1, relief="sunken")
            sensor_label.grid(row=2, column=i, padx=5, pady=5, sticky="nswe")
            self.sensor_labels.append(sensor_label)

    def setup_frame2_widgets(self):
        lblfrm2Title = tk.Label(self.ortaFrame, text="RECEPIES TO SET", font=("Arial", 16), bd=1, relief="ridge")
        lblfrm2Title.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="nswe")

        labels = ["CO2", "Ph", "Su S", "Ort S", "Nem", "EC"]
        for i, text in enumerate(labels):
            tk.Label(self.ortaFrame, text=text, font=("Arial", 16), bd=1, relief="sunken").grid(row=1, column=i, padx=5, pady=5, sticky="nswe")

        self.entries = []
        for i in range(6):
            entry = tk.Entry(self.ortaFrame, width=8, font=("Arial", 16), relief="sunken")
            entry.grid(row=2, column=i, padx=5, pady=5, sticky="nsew")
            self.entries.append(entry)

        lblSecim = tk.Label(self.ortaFrame, text="Receipt Selection : ", font=("Arial", 16))
        lblSecim.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="e")

        # Populate combobox with recipe names from the database
        recipe_names = list(self.recipes.keys())
        self.cmbSecim = ttk.Combobox(self.ortaFrame, values=recipe_names, font=("Arial", 16))
        self.cmbSecim.grid(row=3, column=4, columnspan=2, padx=5, pady=5, sticky="nswe")

    def setup_frame3_widgets(self):
        lblFrm3Title = tk.Label(self.altFrame, text="MANUAL OVERRIDE", font=("Arial", 16), bd=1, relief="ridge")
        lblFrm3Title.grid(row=0, column=0, columnspan=8, padx=5, pady=5, sticky="nswe")

        labels = ["LED", "Fan", "Min-A", "Min-B", "Asit", "Su I", "Ort I", "Hum"]
        for i, text in enumerate(labels):
            tk.Label(self.altFrame, text=text, font=("Arial", 16), bd=1, relief="sunken").grid(row=1, column=i, padx=5, pady=5, sticky="nswe")

        self.buttons = []
        for i in range(8):
            button = tk.Button(self.altFrame, text="ON", background="lightgreen")
            button.grid(row=2, column=i, padx=5, pady=5, sticky="ew")
            self.buttons.append(button)

    def update_entries(self, event):
        selected_recipe = self.cmbSecim.get()
        if selected_recipe in self.recipes:
            values = self.recipes[selected_recipe]
            for entry, value in zip(self.entries, values):
                entry.delete(0, tk.END)  # Clear the existing value
                entry.insert(0, value)  # Insert the new value

    def update_sensor_readings(self):
        # Simulate sensor data updates
        simulated_values = [f"{random.uniform(5, 7):.1f}" for _ in range(6)]
        for label, value in zip(self.sensor_labels, simulated_values):
            label.config(text=value)

    def on_closing(self):
        self.SensorReader.stop()
        self.db.close()
        self.destroy()

if __name__ == "__main__":
    # Ensure the database file exists or create it
    db_file = '/home/debinci/Desktop/proje/PYTHON-2/USERINTERFACE/recipes.db'

    app = Application(db_file)
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()