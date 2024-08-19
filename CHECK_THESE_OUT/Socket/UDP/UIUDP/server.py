import tkinter as tk
import socket
import threading

class ServerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chat Server")
        self.geometry("400x500")

        self.text_area = tk.Text(self, state="disabled")
        self.text_area.grid(row=0, column=0, sticky="nsew")

        self.msg_entry = tk.Entry(self)
        self.msg_entry.grid(row=1, column=0, sticky="nsew")
        self.msg_entry.bind("<Return>", self.send_message)

        self.start_button = tk.Button(self, text="Start Server", command=self.start_server)
        self.start_button.grid(row=2, column=0, sticky="nsew")

        self.stop_button = tk.Button(self, text="Stop Server", command=self.stop_server, state="disabled")
        self.stop_button.grid(row=3, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=3)
        self.grid_columnconfigure(0, weight=1)

        self.server_socket = None
        self.client_addresses = set()
        self.receive_thread = None
        self.running = False

    def start_server(self):
        if not self.server_socket:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                self.server_socket.bind(("0.0.0.0", 61127))
                self.text_area.config(state="normal")
                self.text_area.insert(tk.END, "Server started and listening...\n")
                self.text_area.config(state="disabled")
                self.start_button.config(state="disabled")
                self.stop_button.config(state="normal")
                self.running = True
                self.receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
                self.receive_thread.start()
            except Exception as e:
                self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Error starting server: {e}\n")
                self.text_area.config(state="disabled")

    def stop_server(self):
        if self.server_socket:
            self.text_area.config(state="normal")
            self.text_area.insert(tk.END, "Stopping server...\n")
            self.text_area.config(state="disabled")

            self.running = False
            self.server_socket.close()
            self.server_socket = None
            self.client_addresses.clear()
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            self.text_area.config(state="normal")
            self.text_area.insert(tk.END, "Server stopped.\n")
            self.text_area.config(state="disabled")

    def receive_messages(self):
        while self.running:
            try:
                message, addr = self.server_socket.recvfrom(1024)
                message = message.decode("utf-8")
                if message:
                    self.text_area.config(state="normal")
                    self.text_area.insert(tk.END, f"Received from {addr}: {message}\n")
                    self.text_area.config(state="disabled")
                    if addr not in self.client_addresses:
                        self.client_addresses.add(addr)
                    self.broadcast(f"Server: {message}")
            except Exception as e:
                if not self.running:
                    break
                self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Error receiving message: {e}\n")
                self.text_area.config(state="disabled")

    def broadcast(self, message):
        for addr in self.client_addresses:
            try:
                self.server_socket.sendto(message.encode("utf-8"), addr)
            except Exception as e:
                self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Error broadcasting message to {addr}: {e}\n")
                self.text_area.config(state="disabled")

    def send_message(self, event=None):
        message = self.msg_entry.get()
        if message:
            self.text_area.config(state="normal")
            self.text_area.insert(tk.END, f"Server: {message}\n")
            self.text_area.config(state="disabled")
            self.msg_entry.delete(0, tk.END)
            self.broadcast(f"Server: {message}")

if __name__ == "__main__":
    app = ServerApp()
    app.mainloop()
