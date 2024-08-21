import tkinter as tk
from tkinter import ttk

# Pencere oluşturma
pencere = tk.Tk()
pencere.title("Genişletilmiş UI Örneği")
pencere.geometry("800x600")
pencere.resizable(True,True)

# 1. Satır
lblEtiket = tk.Label(pencere, text="Label", bd=5, relief="solid")
lblEtiket.grid(row=0, column=0, padx=30, pady=10)

enGiris = tk.Entry(pencere, width=30, font=30, bg="red", fg="white", bd=0)
enGiris.grid(row=0, column=1, padx=10, pady=10)

btnDugme = tk.Button(pencere, text="Tıkla", bg="blue", fg="yellow", border=10)
btnDugme.grid(row=0, column=2, padx=10, pady=10)

# 2. Satır
lblEtiket1 = tk.Label(pencere, text="Label 2", bd=5, relief="solid")
lblEtiket1.grid(row=1, column=0, padx=30, pady=10)

enGiris2 = tk.Entry(pencere, width=30, font=30, bg="red", fg="white", bd=0)
enGiris2.grid(row=1, column=1, padx=10, pady=10)

btnDugme1 = tk.Button(pencere, text="Tıkla 2", bg="blue", fg="yellow", border=10)
btnDugme1.grid(row=1, column=2, padx=10, pady=10)

# 3. Satır - ComboBox
lblCombo = tk.Label(pencere, text="Seçenekler", bd=5, relief="solid")
lblCombo.grid(row=2, column=0, padx=30, pady=10)

comboBox = ttk.Combobox(pencere, values=["Seçenek 1", "Seçenek 2", "Seçenek 3"])
comboBox.grid(row=2, column=1, padx=10, pady=10)

btnDugme2 = tk.Button(pencere, text="Tıkla 3", bg="blue", fg="yellow", border=10)
btnDugme2.grid(row=2, column=2, padx=10, pady=10)

# 4. Satır - Aynı hücreye iki label ekleme
frame = tk.Frame(pencere)
frame.grid(row=3, column=0, padx=30, pady=10)

label1 = tk.Label(frame, text="Label 1", bd=5, relief="solid")
label1.pack(side=tk.TOP)

label2 = tk.Label(frame, text="Label 2", bd=5, relief="solid")
label2.pack(side=tk.TOP)

# 4. Satır - Radiobutton
radioBtn1 = tk.Radiobutton(pencere, text="Radio 1", value=1)
radioBtn1.grid(row=3, column=1, padx=10, pady=10)

radioBtn2 = tk.Radiobutton(pencere, text="Radio 2", value=2)
radioBtn2.grid(row=3, column=2, padx=10, pady=10)

# 5. Satır - Listbox
lblListbox = tk.Label(pencere, text="Listbox", bd=5, relief="solid")
lblListbox.grid(row=4, column=0, padx=30, pady=10)

listbox = tk.Listbox(pencere)
listbox.insert(1, "Öğe 1")
listbox.insert(2, "Öğe 2")
listbox.insert(3, "Öğe 3")
listbox.grid(row=4, column=1, padx=10, pady=10)

# 5. Satır - Scale
scale = tk.Scale(pencere, from_=0, to=100, orient=tk.HORIZONTAL)
scale.grid(row=4, column=2, padx=10, pady=10)

# 6. Satır - Text
lblText = tk.Label(pencere, text="Text", bd=5, relief="solid")
lblText.grid(row=5, column=0, padx=30, pady=10)

text = tk.Text(pencere, height=5, width=30)
text.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

# 7. Satır - Message
message = tk.Message(pencere, text="Bu bir mesaj", width=200, bd=5, relief="solid")
message.grid(row=6, column=0, padx=30, pady=10)

# 7. Satır - Spinbox
spinbox = tk.Spinbox(pencere, from_=0, to=10)
spinbox.grid(row=6, column=1, padx=10, pady=10)

# 8. Satır - Progressbar
progressbar = ttk.Progressbar(pencere, length=200, mode='indeterminate')
progressbar.grid(row=7, column=0, padx=30, pady=10)
progressbar['value'] = 50

# 8. Satır - Scrollbar
scrollbar = tk.Scrollbar(pencere, orient=tk.HORIZONTAL)
scrollbar.grid(row=7, column=1, padx=10, pady=10)

pencere.mainloop()
