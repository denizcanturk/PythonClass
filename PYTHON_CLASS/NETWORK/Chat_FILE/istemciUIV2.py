import customtkinter as ctk
import socket as sc
import threading as tr
import os
import base64

class ClientApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chat Client")
        self.geometry("420x490")
        self.server_ip = ""
        self.server_port = 61127
        self.username = None
        self.client_socket = None
        self.receive_thread = None
        self.connected = False

        # Initialize UI
        self.topFrame = ctk.CTkFrame(self, height=75)
        self.topFrame.grid(row=0, column=0, sticky="nsew")

        self.usernameEntry = ctk.CTkEntry(self.topFrame, placeholder_text="Username", font=("Courier", 16))
        self.usernameEntry.place(x=10, y=10)
        self.usernameEntry.bind("<Return>", self.setUsername)

        self.connectSwitch = ctk.CTkSwitch(self.topFrame, state="off", text="Connect", command=self.toggleConnect)
        self.connectSwitch.place(x=270, y=10)

        self.serverIPEntry = ctk.CTkEntry(self.topFrame, placeholder_text="Server IP", font=("Courier", 16))
        self.serverIPEntry.place(x=10, y=45)

        self.sendFileButton = ctk.CTkButton(self.topFrame, text="Send File", command=self.sendFile)
        self.sendFileButton.place(x=270, y=45)

        self.textArea = ctk.CTkTextbox(self, font=("Courier", 16), text_color="light green", height=380, wrap=ctk.WORD)
        self.textArea.grid(row=1, column=0, sticky="ew")

        self.messageEntry = ctk.CTkEntry(self, font=("Courier", 16))
        self.messageEntry.grid(row=2, column=0, sticky="nsew")
        self.messageEntry.bind("<Return>", self.sendMessage)

        self.progressBar = ctk.CTkProgressBar(self, width=400)
        self.progressBar.grid(row=3, column=0, pady=5, sticky="ew")
        self.progressBar.set(0)
        self.progressBar.grid_remove()  # Hide initially

        self.grid_columnconfigure(0, weight=1)

    def toggleConnect(self):
        if self.usernameEntry.get() == "" or self.serverIPEntry.get() == "":
            self.updateTextArea("Username or Server IP cannot be left blank!\n")
            self.connectSwitch.deselect()
            return
        if self.connected:
            self.disconnectFromServer()
        else:
            self.connectToServer()

    def setUsername(self, event=None):
        self.username = self.usernameEntry.get().strip()

    def setIPAddress(self):
        self.server_ip = self.serverIPEntry.get().strip()

    def connectToServer(self):
        if not self.client_socket:
            self.client_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
            self.client_socket.settimeout(5)  # Set a timeout for connection attempts
            try:
                self.setUsername()
                self.setIPAddress()
                self.client_socket.connect((self.server_ip, self.server_port))
                self.client_socket.send(self.username.encode("utf-8"))
                self.updateTextArea("Connected to server.\n")
                self.connected = True
                self.connectSwitch.configure(text="Disconnect", state="on")
                self.receive_thread = tr.Thread(target=self.receiveMessages, daemon=True)
                self.receive_thread.start()
            except sc.timeout as e:
                self.updateTextArea(f"Connection timed out: {e}\n")
            except Exception as e:
                self.updateTextArea(f"Failed to connect to server: {e}\n")

    def receiveMessages(self):
        while self.connected:
            try:
                msg = self.client_socket.recv(1024).decode("utf-8")
                if msg:
                    if msg.startswith("FILE:"):
                        self.receiveFile(msg)
                    else:
                        self.updateTextArea(f"{msg}\n")
                else:
                    # Server has closed the connection
                    self.disconnectFromServer()
            except sc.timeout:
                continue  # Continue to loop if the socket times out
            except Exception as e:
                self.updateTextArea(f"Error receiving message: {e}\n")
                self.disconnectFromServer()
                break

    def receiveFile(self, file_message):
        _, file_name, file_size, encoded_data = file_message.split(":", 3)
        file_size = int(file_size)
        file_data = base64.b64decode(encoded_data)
        save_path = ctk.filedialog.asksaveasfilename(defaultextension=".*", initialfile=file_name)
        if save_path:
            self.progressBar.grid()
            self.progressBar.set(0)
            with open(save_path, "wb") as file:
                file.write(file_data)
                self.progressBar.set(1)
            self.updateTextArea(f"Received file '{file_name}'\n")
            self.progressBar.grid_remove()
        else:
            self.updateTextArea(f"File reception cancelled for '{file_name}'\n")

    def sendFile(self):
        if not self.connected:
            self.updateTextArea("You must be connected to send a file.\n")
            return
        filename = ctk.filedialog.askopenfilename()
        if filename:
            with open(filename, "rb") as file:
                file_data = file.read()
            encoded_data = base64.b64encode(file_data).decode('utf-8')
            file_name = os.path.basename(filename)
            file_size = len(encoded_data)
            file_message = f"FILE:{file_name}:{file_size}:{encoded_data}"
            self.sendMessage(file_message, show_progress=True)
            self.updateTextArea(f"You: Sent file {file_name}\n")

    def sendMessage(self, msg, show_progress=False):
        if self.client_socket:
            try:
                if show_progress:
                    self.progressBar.grid()
                    self.progressBar.set(0)
                
                if msg.startswith("FILE:"):
                    # Send file data in chunks
                    chunk_size = 1024
                    total_sent = 0
                    for i in range(0, len(msg), chunk_size):
                        chunk = msg[i:i+chunk_size]
                        self.client_socket.send(chunk.encode("utf-8"))
                        total_sent += len(chunk)
                        if show_progress:
                            self.progressBar.set(total_sent / len(msg))
                            self.update_idletasks()
                else:
                    self.client_socket.send(msg.encode("utf-8"))
                
                if show_progress:
                    self.progressBar.grid_remove()
                
                if not msg.startswith("FILE:"):
                    self.updateTextArea(f"You: {msg}\n")
                if msg.lower() == "exit":
                    self.disconnectFromServer()
            except Exception as e:
                self.updateTextArea(f"Error sending message: {e}\n")

    def disconnectFromServer(self):
        if self.connected:
            self.updateTextArea("Disconnecting from server...\n")
            self.connected = False
            if self.client_socket:
                try:
                    self.client_socket.shutdown(sc.SHUT_RDWR)  # Gracefully shut down the socket
                    self.client_socket.close()
                    self.connectSwitch.deselect()
                except Exception as e:
                    self.updateTextArea(f"Error disconnecting from server: {e}\n")
            if self.receive_thread and self.receive_thread.is_alive():
                self.receive_thread.join()
            self.client_socket = None
            self.receive_thread = None
            self.connectSwitch.configure(text="Connect", state="off")
            self.updateTextArea("Disconnected from server.\n")

    def updateTextArea(self, message):
        self.after(0, self.textArea.insert, ctk.END, message)

if __name__ == "__main__":
    app = ClientApp()
    app.mainloop()