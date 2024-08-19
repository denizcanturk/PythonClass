import tkinter as tk
import socket
import threading

class ClientApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat Client")
        self.geometry("400x500")

        self.label = tk.Label(self, text="Server IP Address")
        self.label.grid(row=0, column=0, sticky="nsew")

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0, sticky="nsew")
        self.entry.insert(0, "127.0.0.1")  # Default IP

        self.connect_button = tk.Button(self, text="Connect", command=self.connect_to_server)
        self.connect_button.grid(row=2, column=0, sticky="nsew")

        self.disconnect_button = tk.Button(self, text="Disconnect", command=self.disconnect_from_server, state="disabled")
        self.disconnect_button.grid(row=3, column=0, sticky="nsew")

        self.text_area = tk.Text(self, state="disabled")
        self.text_area.grid(row=4, column=0, sticky="nsew")

        self.msg_entry = tk.Entry(self)
        self.msg_entry.grid(row=5, column=0, sticky="nsew")
        self.msg_entry.bind("<Return>", self.send_message)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=3)
        self.grid_rowconfigure(5, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.socket = None
        self.server_address = None
        self.receive_thread = None

    def connect_to_server(self):
        ip = self.entry.get()
        if self.socket is not None:
            self.text_area.config(state="normal")
            self.text_area.insert(tk.END, "Already connected or connection in progress.\n")
            self.text_area.config(state="disabled")
            return

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (ip, 61127)
        self.text_area.config(state="normal")
        self.text_area.insert(tk.END, "Connected to the server\n")
        self.text_area.config(state="disabled")
        self.connect_button.config(state="disabled")
        self.disconnect_button.config(state="normal")
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def disconnect_from_server(self):
        if self.socket:
            self.text_area.config(state="normal")
            self.text_area.insert(tk.END, "Disconnecting...\n")
            self.text_area.config(state="disabled")
            try:
                self.socket.close()
                self.socket = None
                self.server_address = None
                self.connect_button.config(state="normal")
                self.disconnect_button.config(state="disabled")
                self.text_area.config(state="normal")
                self.text_area.insert(tk.END, "Disconnected from server\n")
                self.text_area.config(state="disabled")
            except Exception as e:
                self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Error during disconnection: {e}\n")
                self.text_area.config(state="disabled")

    def send_message(self, event=None):
        if self.socket:
            message = self.msg_entry.get()
            if message:
                try:
                    self.socket.sendto(message.encode("utf-8"), self.server_address)
                    self.text_area.config(state="normal")
                    self.text_area.insert(tk.END, f"You: {message}\n")
                    self.text_area.config(state="disabled")
                    self.msg_entry.delete(0, tk.END)
                except Exception as e:
                    self.text_area.config(state="normal")
                    self.text_area.insert(tk.END, f"Failed to send message: {e}\n")
                    self.text_area.config(state="disabled")

    def receive_messages(self):
        while self.socket:
            try:
                message, addr = self.socket.recvfrom(1024)
                message = message.decode("utf-8")
                if message:
                    self.text_area.config(state="normal")
                    self.text_area.insert(tk.END, f"Server: {message}\n")
                    self.text_area.config(state="disabled")
            except Exception as e:
                if self.socket:
                    self.text_area.config(state="normal")
                    self.text_area.insert(tk.END, f"Error receiving message: {e}\n")
                    self.text_area.config(state="disabled")
                break

if __name__ == "__main__":
    app = ClientApp()
    app.mainloop()
