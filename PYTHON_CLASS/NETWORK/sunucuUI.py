import customtkinter as ctk
import socket as sc
import threading as tr

class ServerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chat Server")
        self.geometry("400x480")
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
            try:
                self.serverSocket.bind(("", self.portNum))
                self.serverSocket.listen(self.maxClientNum)
                self.textArea.insert(ctk.END, "Server started!\nWaiting for incoming connections...\n")
                self.server_running = True
                self.connectSwitch.configure(text="Stop Server", state="on")
                self.acceptThread = tr.Thread(target=self.acceptConnections)
                self.acceptThread.start()
            except Exception as e:
                self.textArea.insert(ctk.END, f"Failed to start server: {e}\n")
                self.connectSwitch.set("off")

    def stopServer(self):
        if self.serverSocket:
            self.textArea.insert(ctk.END, "Stopping the server...\n")
            self.server_running = False
            if self.acceptThread and self.acceptThread.is_alive():
                self.acceptThread.join()  # Wait for the accept thread to finish
            for clientSocket in self.connectedClients.values():
                try:
                    clientSocket.send("Server is shutting down...".encode("utf-8"))
                    clientSocket.close()
                except Exception as e:
                    self.textArea.insert(ctk.END, f"Error disconnecting from client: {e}\n")
            self.serverSocket.close()
            self.serverSocket = None
            self.textArea.insert(ctk.END, "Server stopped.\n")
            self.connectedClients.clear()
            self.clientCount = 0
            self.labelUpdates()
            self.connectSwitch.configure(text="Start Server", state="off")

    def acceptConnections(self):
        while self.server_running:
            try:
                clientSocket, ipAddr = self.serverSocket.accept()
                self.textArea.insert(ctk.END, f"Connection accepted from {ipAddr}\n")
                self.clientCount += 1
                self.labelUpdates()
                clientThread = tr.Thread(target=self.handleClient, args=(clientSocket,))
                clientThread.start()
            except Exception as e:
                if self.server_running:  # Only log if the server is still running
                    self.textArea.insert(ctk.END, f"Error accepting connection: {e}\n")
                break

    def labelUpdates(self):
        self.lblClientCount.configure(text=self.lblDefaulttext + str(self.clientCount))

    def handleClient(self, clientSocket):
        try:
            # First message should be the username
            username = clientSocket.recv(1024).decode("utf-8")
            if not username:
                username = f"Client{len(self.connectedClients) + 1}"

            self.textArea.insert(ctk.END, f"{username} has joined the chat.\n")
            self.connectedClients[username] = clientSocket
            self.broadcastMsg(f"{username} has joined the chat.")

            while self.server_running:
                try:
                    msg = clientSocket.recv(1024).decode("utf-8")
                    if msg == "exit":
                        break
                    self.textArea.insert(ctk.END, f"{username}: {msg}\n")
                    if self.rbBroadcast.get():
                        self.broadcastMsg(f"{username}: {msg}")
                except Exception as e:
                    self.textArea.insert(ctk.END, f"Error handling client: {e}\n")
                    break
        finally:
            clientSocket.close()
            if username in self.connectedClients:
                del self.connectedClients[username]
                self.clientCount -= 1
                self.labelUpdates()
                self.textArea.insert(ctk.END, f"{username} has left the chat.\n")
                self.broadcastMsg(f"{username} has left the chat.")

    def broadcastMsg(self, msg):
        for clientSocket in self.connectedClients.values():
            try:
                clientSocket.send(msg.encode("utf-8"))
            except Exception as e:
                self.textArea.insert(ctk.END, f"Error broadcasting message: {e}\n")

    def sendMessage(self, event=None):
        msg = self.messageEntry.get()
        if msg:
            self.textArea.insert(ctk.END, f"Server: {msg}\n")
            self.broadcastMsg(f"Server: {msg}")
            self.messageEntry.delete(0, ctk.END)

if __name__ == "__main__":
    app = ServerApp()
    app.mainloop()
