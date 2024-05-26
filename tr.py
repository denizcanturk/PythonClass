import tkinter as tk
import pyttsx3 as p

talker = p.init()

def okuBakiyim():
    talker.say(giris.get())
    talker.runAndWait()
    talker.stop()

root = tk.Tk()
root.geometry("300x50")
root.title("Talk To Me!")

giris = tk.Entry(root, width=20, font=30, bd=0)
giris.pack(side=tk.LEFT, padx=5)

dugme = tk.Button(root, text="Konus", font=30, bg="red", fg="white", command=okuBakiyim)
dugme.pack(side=tk.LEFT, padx=5)

root.mainloop()