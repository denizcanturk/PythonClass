import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.minsize(width=400,height=200)

        # Create two frames
        self.frame1 = ctk.CTkFrame(self, corner_radius=5)
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.44, relheight=0.65)

        self.frame2 = ctk.CTkFrame(self, corner_radius=5)
        self.frame2.place(relx=0.50, rely=0.05, relwidth=0.44, relheight=0.65)

        self.frame3 = ctk.CTkFrame(self, corner_radius=10)
        self.frame3.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.2)

        # Add some content to the frames
        label1 = ctk.CTkLabel(self.frame1, text="Frame 1")
        label1.place(relx=0.5, rely=0.5, anchor="center")

        label2 = ctk.CTkLabel(self.frame2, text="Frame 2")
        label2.place(relx=0.5, rely=0.5, anchor="center")

        btn1 = ctk.CTkButton(self.frame1,text="asf")
        btn1.grid(row=0, column=1, padx=5, pady=5)

        btn2 = ctk.CTkButton(self.frame2, text="button 2")
        btn2.place(relx=0.1, rely=0.1,relwidth=0.2)

if __name__ == "__main__":
    app = App()
    app.mainloop()