import customtkinter as ctk
import socket as sc
import threading as tr
import os
import base64
from tkinter import filedialog

class ServerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chat Server")
        self.geometry("420x490")
        self.portNum = 61127
        self.maxClientNum = 15
        self.clientCount = 0
        self.lblDefaulttext = "Client Count: "
        self.serverSocket = None
        self.connectedClients = {}
        self.acceptThread = None
        self.server_running = False

        self.topFrame = ctk.CTkFrame(self, height=75)
        self.topFrame.grid(row=0, column=0, sticky="nsew")

        self.connectSwitch = ctk.CTkSwitch(self.topFrame, state="off", text="Start Server", command=self.toggleServer)
        self.connectSwitch.place(x=10, y=10)

        self.rbBroadcast = ctk.CTkCheckBox(self.topFrame, text="Broadcast messages")
        self.rbBroadcast.place(x=10, y=45)

        self.lblClientCount = ctk.CTkLabel(self.topFrame, text=self.lblDefaulttext + str(self.clientCount))
        self.lblClientCount.place(x=270, y=45)

        self.textArea = ctk.CTkTextbox(self, font=("Courier", 16), text_color="light green", height=380, wrap=ctk.CHAR)
        self.textArea.grid(row=1, column=0, sticky="ew")

        self.messageEntry = ctk.CTkEntry(self, font=("Courier", 16))
        self.messageEntry.grid(row=2, column=0, sticky="nsew")
        self.messageEntry.bind("<Return>", self.sendMessage)

        self.progressBar = ctk.CTkProgressBar(self, width=400)
        self.progressBar.grid(row=3, column=0, pady=5, sticky="ew")
        self.progressBar.set(0)
        self.progressBar.grid_remove()  # Hide initially

        self.sendFileButton = ctk.CTkButton(self.topFrame, text="Send File", command=self.sendFile)
        self.sendFileButton.place(x=270, y=10)

        self.grid_columnconfigure(0, weight=1)

    def toggleServer(self):
        if self.server_running:
            self.stopServer()
        else:
            self.startServer()

    def startServer(self):
        if not self.serverSocket:
            self.serverSocket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
            self.serverSocket.setsockopt(sc.SOL_SOCKET, sc.SO_REUSEADDR, 1)
            self.serverSocket.settimeout(1)  # Set a short timeout for non-blocking behavior
            try:
                self.serverSocket.bind(("", self.portNum))
                self.serverSocket.listen(self.maxClientNum)
                self.updateTextArea("Server started!\nWaiting for incoming connections...\n")
                self.server_running = True
                self.connectSwitch.configure(text="Stop Server", state="on")
                self.acceptThread = tr.Thread(target=self.acceptConnections, daemon=True)
                self.acceptThread.start()
            except Exception as e:
                self.updateTextArea(f"Failed to start server: {e}\n")
                self.connectSwitch.configure(text="Start Server", state="off")

    def stopServer(self):
        if self.serverSocket:
            self.updateTextArea("Stopping the server...\n")
            self.server_running = False
            if self.acceptThread and self.acceptThread.is_alive():
                self.acceptThread.join()  # Wait for the accept thread to finish
            for clientSocket in list(self.connectedClients.values()):
                try:
                    clientSocket.send("Server is shutting down...".encode("utf-8"))
                    clientSocket.close()
                except Exception as e:
                    self.updateTextArea(f"Error disconnecting from client: {e}\n")
            self.serverSocket.close()
            self.serverSocket = None
            self.updateTextArea("Server stopped.\n")
            self.connectedClients.clear()
            self.clientCount = 0
            self.labelUpdates()
            self.connectSwitch.configure(text="Start Server", state="off")

    def acceptConnections(self):
        while self.server_running:
            try:
                clientSocket, ipAddr = self.serverSocket.accept()
                self.updateTextArea(f"Connection accepted from {ipAddr}\n")
                self.clientCount += 1
                self.labelUpdates()
                clientThread = tr.Thread(target=self.handleClient, args=(clientSocket,), daemon=True)
                clientThread.start()
            except sc.timeout as e:
                # Handle the timeout exception to continue accepting connections
                pass
            except Exception as e:
                if self.server_running:
                    self.updateTextArea(f"Error accepting connection: {e}\n")

    def labelUpdates(self):
        self.lblClientCount.configure(text=self.lblDefaulttext + str(self.clientCount))

    def handleClient(self, clientSocket):
        try:
            # First message should be the username
            username = clientSocket.recv(1024).decode("utf-8")
            if not username:
                username = f"Client{len(self.connectedClients) + 1}"

            self.updateTextArea(f"{username} has joined the chat.\n")
            self.connectedClients[username] = clientSocket
            self.broadcastMsg(f"{username} has joined the chat.")

            while self.server_running:
                try:
                    msg = clientSocket.recv(1024).decode("utf-8")
                    if not msg:
                        break
                    if msg == "exit":
                        break
                    if msg.startswith("FILE:"):
                        self.receiveFile(msg, username)
                    else:
                        self.updateTextArea(f"{username}: {msg}\n")
                        if self.rbBroadcast.get():
                            self.broadcastMsg(f"{username}: {msg}")
                except Exception as e:
                    self.updateTextArea(f"Error handling client: {e}\n")
                    break
        finally:
            clientSocket.close()
            if username in self.connectedClients:
                del self.connectedClients[username]
                self.clientCount -= 1
                self.labelUpdates()
                self.updateTextArea(f"{username} has left the chat.\n")
                self.broadcastMsg(f"{username} has left the chat.")

    def receiveFile(self, file_message, sender):
        _, file_name, file_size, encoded_data = file_message.split(":", 3)
        file_size = int(file_size)
        file_data = base64.b64decode(encoded_data)
        save_path = filedialog.asksaveasfilename(defaultextension=".*", initialfile=file_name)
        if save_path:
            self.progressBar.grid()
            self.progressBar.set(0)
            with open(save_path, "wb") as file:
                file.write(file_data)
                self.progressBar.set(1)
            self.updateTextArea(f"Received file '{file_name}' from {sender}\n")
            self.progressBar.grid_remove()
        else:
            self.updateTextArea(f"File reception cancelled for '{file_name}' from {sender}\n")

    def broadcastMsg(self, msg, show_progress=False):
        if show_progress:
            self.progressBar.grid()
            self.progressBar.set(0)
        
        total_sent = 0
        chunk_size = 1024
        for clientSocket in list(self.connectedClients.values()):
            try:
                if msg.startswith("FILE:"):
                    # Send file data in chunks
                    for i in range(0, len(msg), chunk_size):
                        chunk = msg[i:i+chunk_size]
                        clientSocket.send(chunk.encode("utf-8"))
                        total_sent += len(chunk)
                        if show_progress:
                            self.progressBar.set(total_sent / len(msg))
                            self.update_idletasks()
                else:
                    clientSocket.send(msg.encode("utf-8"))
            except Exception as e:
                self.updateTextArea(f"Error broadcasting message: {e}\n")
        
        if show_progress:
            self.progressBar.grid_remove()

    def sendMessage(self, event=None):
        msg = self.messageEntry.get()
        if msg:
            self.updateTextArea(f"Server: {msg}\n")
            self.broadcastMsg(f"Server: {msg}")
            self.messageEntry.delete(0, ctk.END)

    def sendFile(self):
        filename = filedialog.askopenfilename()
        if filename:
            with open(filename, "rb") as file:
                file_data = file.read()
            encoded_data = base64.b64encode(file_data).decode('utf-8')
            file_name = os.path.basename(filename)
            file_size = len(encoded_data)
            file_message = f"FILE:{file_name}:{file_size}:{encoded_data}"
            self.broadcastMsg(file_message, show_progress=True)
            self.updateTextArea(f"Server: Sent file {file_name}\n")

    def updateTextArea(self, message):
        self.after(0, self.textArea.insert, ctk.END, message)

if __name__ == "__main__":
    app = ServerApp()
    app.mainloop()