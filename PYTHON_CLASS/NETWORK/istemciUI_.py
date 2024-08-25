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
		# Anahtar durumuna göre bağlanacak ya da bağlantıyı kesecek olan fonksiyon
        pass
        
    def setUsername(self, event=None):
		# Kullanıcı adının girilmesini garanti altına alacağımız fonksiyon
        pass

    def setIPAddress(self):
		# Server IP adresini alacağımız fonksiyon
        pass

    def connectToServer(self):
		# Adından belli sanırsam
        pass
        
    def receiveMessages(self):
		
        pass

    def sendMessage(self, event=None):
        pass
        
    def disconnectFromServer(self):
        pass

    def updateTextArea(self, message):
        pass

if __name__ == "__main__":
    app = ClientApp()
    app.mainloop()
