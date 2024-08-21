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

        self.stop_button = tk.Button(self, text="Stop Server", command=self.stop_server, state="normal")
        self.stop_button.grid(row=3, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.server_socket = None
        self.clients = []
        self.accept_thread = None

    def start_server(self):
        if not self.server_socket:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set SO_REUSEADDR option
            try:
                self.server_socket.bind(("0.0.0.0", 61127))  # Bind to all interfaces on port 61127
                self.server_socket.listen(5)
                self.text_area.config(state="normal")
                self.text_area.insert(tk.END, "Server started and listening...\n")
                #self.text_area.config(state="disabled")
                #self.start_button.config(state="disabled")
                #self.stop_button.config(state="normal")
                self.accept_thread = threading.Thread(target=self.accept_connections)
                self.accept_thread.start()
            except Exception as e:
                #self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Error starting server: {e}\n")
                #self.text_area.config(state="disabled")

    def stop_server(self):
        if self.server_socket:
            #self.text_area.config(state="normal")
            self.text_area.insert(tk.END, "Stopping server...\n")
            #self.text_area.config(state="disabled")
            
            # Close all client connections
            for client in self.clients:
                try:
                    client.close()
                except Exception as e:
                    #self.text_area.config(state="normal")
                    self.text_area.insert(tk.END, f"Error closing client connection: {e}\n")
                    #self.text_area.config(state="disabled")
            
            # Close the server socket
            try:
                self.server_socket.shutdown(socket.SHUT_RDWR)
                self.server_socket.close()
            except Exception as e:
                #self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Error closing server socket: {e}\n")
                #self.text_area.config(state="disabled")
            
            self.server_socket = None
            #self.start_button.config(state="normal")
            #self.stop_button.config(state="disabled")
            #self.text_area.config(state="normal")
            self.text_area.insert(tk.END, "Server stopped.\n")
            #self.text_area.config(state="disabled")

            # Stop the accept thread if it's still running
            if self.accept_thread:
                self.accept_thread.join()

    def accept_connections(self):
        while self.server_socket:
            try:
                client_socket, addr = self.server_socket.accept()
                #self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Accepted connection from {addr}\n")
                #self.text_area.config(state="disabled")
                self.clients.append(client_socket)
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
            except Exception as e:
                if self.server_socket:
                    #self.text_area.config(state="normal")
                    self.text_area.insert(tk.END, f"Error accepting connection: {e}\n")
                    #self.text_area.config(state="disabled")
                break

    def handle_client(self, client_socket):
        while True:
            try:
                msg = client_socket.recv(1024).decode("utf-8")
                if not msg:
                    break
                #self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Received: {msg}\n")
                #self.text_area.config(state="disabled")
                self.broadcast(msg)
            except Exception as e:
                #self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Error handling message: {e}\n")
                #self.text_area.config(state="disabled")
                break
        client_socket.close()
        self.clients.remove(client_socket)
        #self.text_area.config(state="normal")
        self.text_area.insert(tk.END, "Client disconnected\n")
        #self.text_area.config(state="disabled")

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                #self.text_area.config(state="normal")
                self.text_area.insert(tk.END, f"Error broadcasting message: {e}\n")
                #self.text_area.config(state="disabled")

    def send_message(self, event=None):
        message = self.msg_entry.get()
        if message:
            #self.text_area.config(state="normal")
            self.text_area.insert(tk.END, f"Server: {message}\n")
            #self.text_area.config(state="disabled")
            self.broadcast(message)
            self.msg_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = ServerApp()
    app.mainloop()
