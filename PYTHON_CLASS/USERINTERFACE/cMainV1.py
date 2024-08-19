import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("İlk Pencerem")
        self.geometry("900x600")

        # Recipe data for demonstration
        self.recipes = {
            "Salatalik": ("300", "6.0", "22.0", "24.0", "50", "1.5"),
            "Marul": ("400", "5.5", "21.0", "23.0", "55", "1.8"),
            "Çilek": ("350", "5.8", "23.0", "25.0", "60", "1.7"),
            "Domates": ("500", "6.2", "20.0", "22.0", "65", "2.0")
        }

        # Setup Frames
        self.setup_frames()

        # Setup Widgets
        self.setup_widgets()

        # Bind combobox selection change to the update function
        self.cmbSecim.bind("<<ComboboxSelected>>", self.update_entries)

    def setup_frames(self):
        # Frameler
        self.ustFrame = tk.Frame(self, borderwidth=2, relief="ridge")
        self.ustFrame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        self.ortaFrame = tk.Frame(self, borderwidth=2, relief="ridge")
        self.ortaFrame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.altFrame = tk.Frame(self, borderwidth=2, relief="ridge")
        self.altFrame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")



        # Configure rows and columns to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # for frame in [self.ustFrame, self.ortaFrame, self.altFrame]:
        #     frame.columnconfigure(0, weight=0)
        #     frame.columnconfigure(1, weight=1)
        #     frame.columnconfigure(tuple(range(6)), weight=1)
        for i in range(8):
            if i > 5:
                self.altFrame.columnconfigure(i, weight=1)
            else:
                self.ortaFrame.columnconfigure(i, weight=1)
                self.ustFrame.columnconfigure(i, weight=1)
                self.altFrame.columnconfigure(i, weight=1)

    def setup_widgets(self):
        # Frame 1 Widgets
        self.setup_frame1_widgets()

        # Frame 2 Widgets
        self.setup_frame2_widgets()

        # Frame 3 Widgets
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

        degerler = ["Salatalik", "Marul", "Çilek", "Domates"]
        self.cmbSecim = ttk.Combobox(self.ortaFrame, values=degerler, font=("Arial", 16))
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

if __name__ == "__main__":
    app = Application()
    app.mainloop()
