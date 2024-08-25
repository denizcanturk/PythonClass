import customtkinter as ctk
import socket as sc
import threading as tr

class ClientApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chat Client")
        self.geometry("400x480")
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

        self.textArea = ctk.CTkTextbox(self, font=("Courier", 16), text_color="light green", height=380, wrap=ctk.WORD)
        self.textArea.grid(row=1, column=0, sticky="ew")

        self.messageEntry = ctk.CTkEntry(self, font=("Courier", 16))
        self.messageEntry.grid(row=2, column=0, sticky="nsew")
        self.messageEntry.bind("<Return>", self.sendMessage)

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

    def sendMessage(self, event=None):
        msg = self.messageEntry.get()
        if msg and self.client_socket:
            try:
                self.client_socket.send(msg.encode("utf-8"))
                self.updateTextArea(f"You: {msg}\n")
                self.messageEntry.delete(0, ctk.END)
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
                except Exception as e:
                    self.updateTextArea(f"Error disconnecting from server: {e}\n")
            
            self.client_socket = None
            self.connectSwitch.deselect()
            self.connectSwitch.configure(text="Connect", state="normal")
            self.updateTextArea("Disconnected from server.\n")

            # Use after() to schedule the thread join
            self.after(100, self.join_receive_thread)

    def join_receive_thread(self):
        if self.receive_thread and self.receive_thread.is_alive():
            self.receive_thread.join(timeout=0.1)
        self.receive_thread = None

    def updateTextArea(self, message):
        self.after(0, self.textArea.insert, ctk.END, message)

if __name__ == "__main__":
    app = ClientApp()
    app.mainloop()