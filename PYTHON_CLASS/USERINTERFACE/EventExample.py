import customtkinter as ctk
import tkinter as tk

class EventDemoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Event Handling Example")
        self.geometry("400x300")

        # Create a label to display event information
        self.eventLabel = ctk.CTkLabel(self, text="Click a button to see event info")
        self.eventLabel.pack(pady=20)

        # Create two buttons to demonstrate event handling
        self.button1 = ctk.CTkButton(self, text="Button 1", command=self.button1_click)
        self.button1.pack(pady=10)

        self.button2 = ctk.CTkButton(self, text="Button 2", command=self.button2_click)
        self.button2.pack(pady=10)

        self.button1.bind("<Enter>", self.on_hover_enter)
        self.button1.bind("<Leave>", self.on_hover_leave)

        # Bind the left mouse click event to a function
        self.bind("<Button-1>", self.mouse_click)
        self.bind("<Button-2>", self.mouse_click)
        self.bind("<Button-3>", self.mouse_click)

    def on_hover_enter(self, event):
        # Change the background color when the mouse enters the button area
        self.button1.configure(bg_color="red")

    def on_hover_leave(self, event):
        # Revert the background color when the mouse leaves the button area
        self.button1.configure(bg_color="green")

    def button1_click(self):
        self.eventLabel.configure(text="Button 1 clicked!")

    def button2_click(self):
        self.eventLabel.configure(text="Button 2 clicked!")

    def mouse_click(self, event):
        # Use event.x and event.y to get the mouse position
        click_x = event.x
        click_y = event.y
        # Display the mouse click position in the label
        self.eventLabel.configure(text=f"Mouse clicked at ({click_x}, {click_y})")

if __name__ == "__main__":
    app = EventDemoApp()
    app.mainloop()
