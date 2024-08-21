import tkinter as tk
import pyttsx3 as p

talker = p.init()

def talk():
    talker.say(enGiris.get())
    talker.runAndWait()
    talker.stop()

root = tk.Tk()

root.title("Python")
root.geometry("300x50")

lblMetin = tk.Label(root, text="Metin:", font=30)
lblMetin.pack(side=tk.LEFT, padx=5)


enGiris = tk.Entry(root, width=15, font=30, bd=0)
enGiris.pack(side=tk.LEFT, padx=5)


btnKonus = tk.Button(root, text="Oku", bg="red", fg="white", command=talk)
btnKonus.pack(side=tk.LEFT, padx=5)


root.mainloop()
