import tkinter as tk
from tkinter import ttk
import time as t

#Yeni eklenen kütüphane
from tkcalendar import DateEntry

pencere = tk.Tk()
pencere.title("User Interface")
pencere.geometry("800x600")
pencere.resizable(False, False)


#Label (Etiket) kullanıcılara bilgi vermek için kullanılan araçlardır.
#Değerleri değiştirilebilir ancak sadece kod ile. Kullanıcı tarafından müdahale edilemez
lblEtiket = tk.Label(pencere, text="Bu bir etiket", font=("Arial", 15),bd=2, relief="solid")
#lblEtiket.place(x=50, y = 50)
lblEtiket.grid(row = 0, column=0, padx=5, pady= 5)

# Entry (Giris) kullanıcıdan bilgi almak için kullanılan araşlardır ve değerleri daima 
# string olarak döner!!!
enGiris = tk.Entry(pencere, width=15,font=("Helvetica", 15), bg="blue", fg="white", bd=3)
enGiris.grid(row=1, column=0, padx=5, pady=10)

# Button (Dugme) Form üzerindeki veriler ile işlem gerçekleştirmek için 
# kullanılan araçtır. Kendisine bağlanan fonksiyonu çalıştırır.
# Peki ya fonksiyonu nereye bağlarız : )
btnDugme = tk.Button(pencere, text="Tıkla", bg="red", fg="white", bd=2)
btnDugme.grid(row=0, column=1, padx=5, pady=5)

# ComboBox (Kombine Kutusu) aralarından seçilebilecek değerleri içeren araçtır.
deger = ["Deger1", "Deger2", "Deger3"]
cmbBox = ttk.Combobox(pencere,values=deger)
cmbBox.grid(row=1, column=1, padx=5, pady=5)

#Frame (Cerceve) üzerine yerleştirilen araçları toplu olarak hareket ettirilmesini sağlayan
# göresel olarak benzer fonksiyonu gerçekleştirecek araçları gruplayan bir araçtır. 
frmTabela = tk.Frame(pencere, bd=4, relief=tk.RIDGE, border=3, borderwidth=3,width=100, height=100)
frmTabela.grid(row=0, column=4)

lblEtiket2 = tk.Label(frmTabela, text="Frame Üstü", font=10)
lblEtiket2.pack(side= tk.LEFT,  padx=5, pady=5)

btnDugme2 = tk.Button(frmTabela, text="Frm Tıkla", font =10)
btnDugme2.pack(side=tk.LEFT, padx=5, pady=5)

#Birkaç seçenek arasından sadece bir tanesinin seçilebilir olması durumunda 
#kullanılan araçtır. 
rdButton = tk.Radiobutton(pencere, text="Grp 1 Btn1", variable=1, value=1)
rdButton.grid(row=2,column=0)

rdButton1 = tk.Radiobutton(pencere, text="Grp 1 Btn 2", variable=1,  value=2)
rdButton1.grid(row=3,column=0)
rdButton1.select()


rdButton2 = tk.Radiobutton(pencere, text="Grp 2 Btn 1", variable=2, value=3)
rdButton2.grid(row=4,column=0)

rdButton3 = tk.Radiobutton(pencere, text="Grp 2 Btn 2",variable=2,  value=34)
rdButton3.grid(row=5,column=0)
rdButton3.select()


btn3 = tk.Button(pencere, text="Extra", font = 15)
btn3.grid(row=6, column=0)

listBox = tk.Listbox(pencere, height=3, relief=tk.RIDGE, bd=3, border=3)
listBox.insert(1, "İlk Eleman")
listBox.insert(2, "İkinci Eleman")
listBox.insert(3, "Üçüncü Eleman")
listBox.grid(row=3, column=1, rowspan=4)


# Scale : Slider tutup sürüklenerek belirlenen aralıkta değerler alan araçtır.
slider = tk.Scale(pencere, from_=0, to= 100, orient=tk.HORIZONTAL, bd=2, border=2, borderwidth=2)
slider.grid(row=2, column=3, columnspan=3, rowspan=2)


# Belirlenen aralıkta değerler alan ve ok tuşları ile değeri artırılıp
# azaltılan araçtır.
spinner = tk.Spinbox(pencere, from_=0, to=100)
spinner.grid(row=10, column=20)

#CheckBox : Bir verinin kullanılıp kullanılmayacağına ilişkin işaretlemenin 
# yapıldığı araçtır.
cBox = tk.Checkbutton(pencere,text="Python")
cBox.grid(row=10, column=4)


# ProbressBar : Halihazırda gerçekleşen bir olayın ilerleme sürecine ilişkin 
# kullanıcılara bilgi veren bir araçtır.
pBar = ttk.Progressbar(pencere, length=100, mode="indeterminate")
pBar.grid(row=11, column=4)


tarih = DateEntry(pencere, date_pattern="dd-mm-yyyy")
tarih.grid(row=12, column=2, rowspan=3, columnspan=4)



for i in range(0):
    pBar["value"] = i
    t.sleep(0.01)
    pencere.update()
pencere.mainloop()