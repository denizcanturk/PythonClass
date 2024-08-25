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
		# Aç Kapa anahtarı ile server başlatacak ve durduracak olan fonksiyon
        pass

    def startServer(self):
		#Server ı başlatacak olan fonksiyon
        pass

    def stopServer(self):
		# Server ı durduracak olan fonksiyon
        pass

    def acceptConnections(self):
		# Genel bağlantıları kabul edecek olan fonksiyon
        pass

    def labelUpdates(self):
		#Bağlantı kabulunden sonra sayacı güncelleyecek olan fonksiyon
        pass

    def handleClient(self, clientSocket):
		# İstemciler ile ilgilecenecek olan fonksiyon
        pass

    def broadcastMsg(self, msg):
		#Alınan mesajı tüm istemcilere gönderecek olan fonksiyon
        pass

    def sendMessage(self, event=None):
		# Girilen txt i msg olarak gönderecek olan fonksiyon.
        pass

    def updateTextArea(self, message):
		#text area ya bağlantı durumlarının ve msg ların girilmesini sağlayacak olan fonksiyon.
        pass

if __name__ == "__main__":
    app = ServerApp()
    app.mainloop()
