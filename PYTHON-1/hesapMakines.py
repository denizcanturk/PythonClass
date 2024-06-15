import tkinter as tk

def hesapla():
    metin = giris.get()
    result = eval(metin)
    giris.insert(tk.END,"=" + str(result))

anaPencere = tk.Tk()

anaPencere.title("Hesap Makinesi")
anaPencere.geometry("500x100")

giris = tk.Entry(anaPencere, width=15)
giris.pack(side=tk.LEFT)

btn = tk.Button(anaPencere, text="Hesapla", command=hesapla)
btn.pack(side=tk.LEFT)



anaPencere.mainloop()