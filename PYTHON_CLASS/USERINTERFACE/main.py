import tkinter as tk
from tkinter import ttk


anaPencere = tk.Tk()
anaPencere.title("İlk Pencerem")
anaPencere.geometry("900x600")

genislik = 880
yukseklik = 180

#Frameler
ustFrame = tk.Frame(anaPencere, borderwidth=2, relief="ridge", width=genislik, height=yukseklik)
ustFrame.grid(row=0, column=0,padx=10, pady=5,sticky="we")

ortaFrame = tk.Frame(anaPencere, borderwidth=2, relief="ridge", width=genislik, height=yukseklik)
ortaFrame.grid(row=1, column=0,padx=10, pady=5,sticky="we")

altFrame = tk.Frame(anaPencere, borderwidth=2, relief="ridge", width=genislik, height=yukseklik)
altFrame.grid(row=2, column=0,padx=10, pady=5,sticky="we")

#Frame 1 Widget lar... 
#Acıklayıcı Etiketler
lblFrm1Title = tk.Label(ustFrame, text= "SENSOR READS",  font=("Arial",16), bd = 1, relief="ridge")
lblFrm1Title.grid(row=0, column=0, columnspan=6, padx=5, pady=5,sticky="nswe")

lblCO2 = tk.Label(ustFrame, text="CO2", font=("Arial",16), bd = 1, relief="sunken")
lblCO2.grid(row=1, column=0,padx=5, pady=5,sticky="nswe")

lblPh = tk.Label(ustFrame, text="Ph", font=("Arial",16), bd = 1, relief="sunken")
lblPh.grid(row=1, column=1,padx=5, pady=5,sticky="nswe")

lblSuSicaklik = tk.Label(ustFrame,text="Su Sicaklik", font=("Arial", 16), bd=1, relief="sunken")
lblSuSicaklik.grid(row=1, column=2, padx=5, pady=5,sticky="nswe")

lblOrtamSicaklik = tk.Label(ustFrame, text="Ortam Sicaklik", font=("Arial", 16), bd=1, relief="sunken")
lblOrtamSicaklik.grid(row=1, column=3, padx=5, pady=5,sticky="nswe")

lblNem = tk.Label(ustFrame, text="Nem", font=("Arial", 16), bd=1, relief="sunken")
lblNem.grid(row=1, column=4, padx=5, pady=5,sticky="nswe")

lblEC = tk.Label(ustFrame, text="EC", font=("Arial", 16), bd=1, relief="sunken")
lblEC.grid(row=1, column=5, padx=5, pady=5,sticky="nswe")

#Sensorden Okudugum Veriler

lblSensorCO2 = tk.Label(ustFrame, text="", font=("Arial",16), bd = 1, relief="sunken")
lblSensorCO2.grid(row=2, column=0,padx=5, pady=5,sticky="nswe")

lblSensorPh = tk.Label(ustFrame, text="", font=("Arial",16), bd = 1, relief="sunken")
lblSensorPh.grid(row=2, column=1,padx=5, pady=5,sticky="nswe")

lblSensorSuSicaklik = tk.Label(ustFrame,text="", font=("Arial", 16), bd=1, relief="sunken")
lblSensorSuSicaklik.grid(row=2, column=2, padx=5, pady=5,sticky="nswe")

lblSensorOrtamSicaklik = tk.Label(ustFrame, text="", font=("Arial", 16), bd=1, relief="sunken")
lblSensorOrtamSicaklik.grid(row=2, column=3, padx=5, pady=5,sticky="nswe")

lblSensorNem = tk.Label(ustFrame, text="", font=("Arial", 16), bd=1, relief="sunken")
lblSensorNem.grid(row=2, column=4, padx=5, pady=5,sticky="nswe")

lblSensorEC = tk.Label(ustFrame, text="", font=("Arial", 16), bd=1, relief="sunken")
lblSensorEC.grid(row=2, column=5, padx=5, pady=5,sticky="nswe")

#Frame 2 (Orta)
lblfrm2Title = tk.Label(ortaFrame,text= "RECEPIES TO SET",  font=("Arial",16), bd = 1, relief="ridge")
lblfrm2Title.grid(row=0, column=0, columnspan=6, padx=5,pady=5, sticky="nswe")

lblsetCO2 = tk.Label(ortaFrame, text="CO2", font=("Arial",16), bd = 1, relief="sunken")
lblsetCO2.grid(row=1, column=0,padx=5, pady=5,sticky="nswe")

lblsetPh = tk.Label(ortaFrame, text="Ph", font=("Arial",16), bd = 1, relief="sunken")
lblsetPh.grid(row=1, column=1,padx=5, pady=5,sticky="nswe")

lblsetSuSicaklik = tk.Label(ortaFrame,text="Su Sicaklik", font=("Arial", 16), bd=1, relief="sunken")
lblsetSuSicaklik.grid(row=1, column=2, padx=5, pady=5,sticky="nswe")

lblsetOrtamSicaklik = tk.Label(ortaFrame, text="Ortam Sicaklik", font=("Arial", 16), bd=1, relief="sunken")
lblsetOrtamSicaklik.grid(row=1, column=3, padx=5, pady=5,sticky="nswe")

lblsetNem = tk.Label(ortaFrame, text="Nem", font=("Arial", 16), bd=1, relief="sunken")
lblsetNem.grid(row=1, column=4, padx=5, pady=5,sticky="nswe")

lblsetEC = tk.Label(ortaFrame, text="EC", font=("Arial", 16), bd=1, relief="sunken")
lblsetEC.grid(row=1, column=5, padx=5, pady=5,sticky="nswe")

#Set Giris Degeleri
entCO2 = tk.Entry(ortaFrame, width=8, font = ("Arial", 16), relief="sunken")
entCO2.grid(row=2, column=0, padx=5, pady=5,sticky="nsew")

entPh = tk.Entry(ortaFrame,width=8, font = ("Arial", 16), relief="sunken")
entPh.grid(row=2, column=1, padx=5, pady=5,sticky="nsew")

entSuSicaklik = tk.Entry(ortaFrame, width=8,font = ("Arial", 16), relief="sunken")
entSuSicaklik.grid(row=2, column=2, padx=5, pady=5,sticky="nsew")

entOrtamSicaklik = tk.Entry(ortaFrame, width=8, font = ("Arial", 16), relief="sunken")
entOrtamSicaklik.grid(row=2, column=3, padx=5, pady=5,sticky="nsew")

entNem = tk.Entry(ortaFrame, width=8, font = ("Arial", 16), relief="sunken")
entNem.grid(row=2, column=4, padx=5, pady=5,sticky="nsew")

entEC = tk.Entry(ortaFrame, width=8, font = ("Arial", 16), relief="sunken")
entEC.grid(row=2, column=5, padx=5, pady=5,sticky="nsew")

lblSecim = tk.Label(ortaFrame, text="Receipt Selection : ", font=("Arial", 16))
lblSecim.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="e")

degerler = ["Salatalik"," Marul", "Çilek", "Domates"]
cmbSecim = ttk.Combobox(ortaFrame, values=degerler, font=("Arial", 16))
cmbSecim.grid(row=3, column=4, columnspan=2, padx=5, pady=5,sticky="nswe")

#altFrame 

lblFrm3Title = tk.Label(altFrame, text= "MANUAL OVERRIDE",  font=("Arial",16), bd = 1, relief="ridge")
lblFrm3Title.grid(row=0, column=0, columnspan=8, padx=5, pady=5,sticky="nswe")

lblLed = tk.Label(altFrame, text="LED", font=("Arial",16), bd = 1, relief="sunken")
lblLed.grid(row=1, column=0,padx=5, pady=5,sticky="nswe")

lblFan = tk.Label(altFrame, text="Fan", font=("Arial",16), bd = 1, relief="sunken")
lblFan.grid(row=1, column=1,padx=5, pady=5,sticky="nswe")

lblA = tk.Label(altFrame,text="Mineral A", font=("Arial", 16), bd=1, relief="sunken")
lblA.grid(row=1, column=2, padx=5, pady=5,sticky="nswe")

lblB = tk.Label(altFrame, text="Mineral B", font=("Arial", 16), bd=1, relief="sunken")
lblB.grid(row=1, column=3, padx=5, pady=5,sticky="nswe")

lblAsit = tk.Label(altFrame, text="Asit", font=("Arial", 16), bd=1, relief="sunken")
lblAsit.grid(row=1, column=4, padx=5, pady=5,sticky="nswe")

lblSuIsitici = tk.Label(altFrame, text="Su Isitici", font=("Arial", 16), bd=1, relief="sunken")
lblSuIsitici.grid(row=1, column=5, padx=5, pady=5,sticky="nswe")

lblOrtamIsitici = tk.Label(altFrame, text="Ortam Isitici", font=("Arial", 16), bd=1, relief="sunken")
lblOrtamIsitici.grid(row=1, column=6, padx=5, pady=5,sticky="nswe")

lblHum = tk.Label(altFrame, text="Hum", font=("Arial", 16), bd=1, relief="sunken")
lblHum.grid(row=1, column=7, padx=5, pady=5,sticky="nswe")

btnLed = tk.Button(altFrame, text = "ON", background="lightgreen")
btnLed.grid(row=2, column=0, padx=5, pady=5,sticky="ew")

btnFan = tk.Button(altFrame, text="ON", background="lightgreen")
btnFan.grid(row=2, column=1, padx=5, pady=5,sticky="ew")

btnA = tk.Button(altFrame, text="ON", background="lightgreen")
btnA.grid(row=2, column=2, padx=5, pady=5,sticky="ew")


btnB = tk.Button(altFrame, text="ON", background="lightgreen")
btnB.grid(row=2, column=3, padx=5, pady=5,sticky="ew")

btnAsit = tk.Button(altFrame, text="ON", background="lightgreen")
btnAsit.grid(row=2, column=4, padx=5, pady=5,sticky="ew")

btnSu = tk.Button(altFrame, text="ON", background="lightgreen")
btnSu.grid(row=2, column=5, padx=5, pady=5,sticky="ew")

btnOrt = tk.Button(altFrame, text="ON", background="lightgreen")
btnOrt.grid(row=2, column=6, padx=5, pady=5,sticky="ew")

btnHum = tk.Button(altFrame, text="ON", background="lightgreen")
btnHum.grid(row=2, column=7, padx=5, pady=5,sticky="ew")















for i in range(6):
     ustFrame.columnconfigure(i, weight=1)
     ortaFrame.columnconfigure(i, weight=1)
     altFrame.columnconfigure(i, weight=1)






anaPencere.mainloop()