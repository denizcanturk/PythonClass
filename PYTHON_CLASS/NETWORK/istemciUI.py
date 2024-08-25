import customtkinter as ctk
import socket as sc
import threading as tr

class ClientApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Chat Client")
        self.geometry("400x480")
        self._windows_set_titlebar_color("red")
        self.server_ip = ""
        self.server_port = 61127
        self.username = None 
        self.client_socket = None #Birden fazla client olacağı için öncelikle boş değişken
        self.receive_thread = None #Oluşturacağımız sonraki thread ler için ilk BOŞ değişken
        self.connected = False  #Program genelinde bağlantı durumunu kontrol etmek için değişken

        # TOP FRAME ve Üzerindeki Widget lar...
        self.topFrame = ctk.CTkFrame(self, height=75)
        self.topFrame.grid(row=0, column=0, sticky="nsew")

        self.usernameEntry = ctk.CTkEntry(self.topFrame, placeholder_text="Username", font=("Courier", 16))
        self.usernameEntry.place(x=10, y=10)
        self.usernameEntry.bind("<Return>", self.setUsername)

        self.connectSwitch = ctk.CTkSwitch(self.topFrame, state="off", text="Connect", command=self.toggleConnect)
        self.connectSwitch.place(x=270, y=10)

        self.serverIPEntry = ctk.CTkEntry(self.topFrame,placeholder_text="Server IP", font=("Courier", 16))
        self.serverIPEntry.place(x=10, y=45)

        #Bağlantı durumu ve gelen giden mesajların gösterileceği alan
        self.textArea = ctk.CTkTextbox(self, font=("Courier", 16), text_color="light green", height=380, wrap=ctk.WORD)
        self.textArea.grid(row=1, column=0, sticky="ew")

        # Göndereceğimiz mesajı yazdığımız alan
        # Ayrıca bir send butonu koymadım, onun yerine Enter a basındad gönder dedim...
        self.messageEntry = ctk.CTkEntry(self, font=("Courier", 16))
        self.messageEntry.grid(row=2, column=0, sticky="nsew")
        self.messageEntry.bind("<Return>", self.sendMessage)

        self.grid_columnconfigure(0, weight=1)

    def toggleConnect(self):
        if self.usernameEntry.get() == "" or self.serverIPEntry.get() == "":
            self.textArea.insert(ctk.END, "Username or Server IP cannot be left blank!\n")
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
            try:
                self.setUsername()
                self.setIPAddress()
                self.client_socket.connect((self.server_ip, self.server_port))
                self.client_socket.send(self.username.encode("utf-8"))
                self.textArea.insert(ctk.END, "Connected to server.\n")
                self.connected = True
                self.connectSwitch.configure(text="Disconnect", state="on")  # Update switch text
                self.receive_thread = tr.Thread(target=self.receiveMessages)
                self.receive_thread.start()
            except Exception as e:
                self.textArea.insert(ctk.END, f"Failed to connect to server: {e}\n")

    def receiveMessages(self):
        while self.connected:
            try:
                msg = self.client_socket.recv(1024).decode("utf-8")
                if msg:
                    self.textArea.insert(ctk.END, f"{msg}\n")
                else:
                    self.disconnectFromServer()
            except Exception as e:
                self.textArea.insert(ctk.END, f"Error receiving message: {e}\n")
                self.disconnectFromServer()
                break

    def sendMessage(self, event=None):
        msg = self.messageEntry.get()
        if msg and self.client_socket:
            self.client_socket.send(msg.encode("utf-8"))
            self.textArea.insert(ctk.END, f"You: {msg}\n")
            self.messageEntry.delete(0, ctk.END)
            if msg=="exit":
                self.disconnectFromServer()

    def disconnectFromServer(self):
        if self.connected:
            self.textArea.insert(ctk.END, "Disconnecting from server...\n")
            self.connected = False
            if self.client_socket:
                try:
                    self.client_socket.send("exit".encode("utf-8"))  # Notify server of disconnection
                    self.client_socket.close()
                    self.connectSwitch.deselect()

                except Exception as e:
                    self.textArea.insert(ctk.END, f"Error disconnecting from server: {e}\n")
            if self.receive_thread and self.receive_thread.is_alive():
                self.receive_thread.join()
            self.client_socket = None
            self.receive_thread = None 
            self.connectSwitch.configure(text="Connect", state="off")  # Update switch text
            self.textArea.insert(ctk.END, "Disconnected from server.\n")

if __name__ == "__main__":
    app = ClientApp()
    app.mainloop()
