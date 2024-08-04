#python -m pip install tkinter
import tkinter as tk
from tkinter import ttk

# Ana pencere oluşturma
# Tk() for oluşturmamızı sağlayan sınıfın bir instance ını oluşturuyoruz. 
root = tk.Tk()

# Forma bir başlık veriyoruz
root.title("Tkinter ve ttk Örnek Form")

# Formun boyutlarını belirliyoruz
root.geometry("400x1000")

# Tkinter Araçları - Widgetları

# Label - Bilgi vermek amaçlı kullanılan etiket. Kullanıcı tarafından değiştirilemez
label = tk.Label(root, text="Label Örneği")
label.pack(pady=5)

# Entry (Text Box) - Kullanıcıdan bilgi almak amaçlı kullanılan kutu. (input gibim...)
entry = tk.Entry(root)
entry.pack(pady=5)

# Button - Dügme, bildiginiz dügme... :)
button = tk.Button(root, text="Button Örneği")
button.pack(pady=5)

# Checkbutton - Var yok... 
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Checkbutton Örneği", variable=check_var)
checkbutton.pack(pady=5)

# Radiobutton - Ya o var, ya bu var... 
radio_var = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="Radiobutton 1", variable=radio_var, value=1)
radiobutton2 = tk.Radiobutton(root, text="Radiobutton 2", variable=radio_var, value=2)
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)

# Listbox - Liste içinden seçim yapılması gerektiği durumlar için 
listbox = tk.Listbox(root)
listbox.insert(1, "Listbox Öğesi 1")
listbox.insert(2, "Listbox Öğesi 2")
listbox.insert(3, "Listbox Öğesi 3")
listbox.pack(pady=5)

# Spinbox - Değerlerin aşağı yukarı okları ile de girilebildiği kutucuk
spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack(pady=5)

# Scale - Değerini, çubuğu kaydırarak ayarladığınız bir çeşit input
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack(pady=5)

# Text - Kafana göre metin girebildiğin alan... Not defteri yapmak için güzel olabilir mesela :)
text = tk.Text(root, height=5, width=30)
text.pack(pady=5)

# Message - Label ın bir değişik versiyonu
message = tk.Message(root, text="Bu bir Message widget örneğidir.", width=200)
message.pack(pady=5)

# ttk Widgetları
#Burdan sonrasında çoğu yukarıdakiler ile aynı, olmayanlara yine not düştüm.
# ttk Label
ttk_label = ttk.Label(root, text="ttk Label Örneği")
ttk_label.pack(pady=5)

# ttk Entry (Text Box)
ttk_entry = ttk.Entry(root)
ttk_entry.pack(pady=5)

# ttk Button
ttk_button = ttk.Button(root, text="ttk Button Örneği")
ttk_button.pack(pady=5)

# ttk Checkbutton
ttk_checkbutton = ttk.Checkbutton(root, text="ttk Checkbutton Örneği", variable=check_var)
ttk_checkbutton.pack(pady=5)

# ttk Radiobutton
ttk_radiobutton1 = ttk.Radiobutton(root, text="ttk Radiobutton 1", variable=radio_var, value=1)
ttk_radiobutton2 = ttk.Radiobutton(root, text="ttk Radiobutton 2", variable=radio_var, value=2)
ttk_radiobutton1.pack(pady=5)
ttk_radiobutton2.pack(pady=5)

# ttk Combobox - Seçenekler arasından seç anacım birini
combobox = ttk.Combobox(root, values=["Seçenek 1", "Seçenek 2", "Seçenek 3"])
combobox.pack(pady=5)

# ttk Progressbar - İlerleme cubugu--- Şu havalı yükleniyor yazısı ile birlikte görünen hareketli zımbırtı
progressbar = ttk.Progressbar(root, length=200)
progressbar.pack(pady=5)
progressbar.start()

# ttk Treeview - Agac yapısı, istediğiniz sayıda kolon ekleyerek istediğini bilgileri teşhir etmenizi sağlar. 
# Windows gezginindeki dosyaların listelenmesi gibim..
tree = ttk.Treeview(root, columns=('Size', 'Modified'), show='headings')
tree.heading('Size', text='Size')
tree.heading('Modified', text='Modified')
tree.insert('', 'end', values=('512 KB', '2023-01-01'))
tree.pack(pady=5)

# Ana Pencereyi çalıştırma
# Daima kodun en sonunda olur ve pencerenin bir uygulama olarak çalışmasını sağlar.
root.mainloop()
