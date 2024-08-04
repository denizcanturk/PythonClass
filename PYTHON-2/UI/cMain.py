#python -m pip install customtkinter
import customtkinter as ctk

# Ana pencereyi oluşturma
root = ctk.CTk()
root.title("CustomTkinter Tüm Widgetlar Örneği")
root.geometry("500x700")

# Temayı ayarla (isteğe bağlı)
ctk.set_appearance_mode("dark")  # Seçenekler: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Seçenekler: "blue", "green", "dark-blue"

# Label widget oluştur ve yerleştir
label = ctk.CTkLabel(root, text="Bu bir CustomTkinter Label")
label.pack(pady=10)

# Button widget oluştur ve yerleştir
button = ctk.CTkButton(root, text="Tıkla", command=lambda: print("Buton Tıklandı"))
button.pack(pady=10)

# Entry widget oluştur ve yerleştir
entry = ctk.CTkEntry(root, placeholder_text="Buraya bir şeyler yazın")
entry.pack(pady=10)

# CheckBox widget oluştur ve yerleştir
checkbox = ctk.CTkCheckBox(root, text="Kabul ediyorum")
checkbox.pack(pady=10)

# RadioButton widget oluştur ve yerleştir
radiobutton1 = ctk.CTkRadioButton(root, text="Seçenek 1", value=1)
radiobutton1.pack(pady=10)
radiobutton2 = ctk.CTkRadioButton(root, text="Seçenek 2", value=2)
radiobutton2.pack(pady=10)

# Slider widget oluştur ve yerleştir
slider = ctk.CTkSlider(root, from_=0, to=100)
slider.pack(pady=10)

# ProgressBar widget oluştur ve yerleştir
progressbar = ctk.CTkProgressBar(root, mode="indeterminate")
progressbar.set(0.5)  # İlerlemeyi %50'ye ayarla
progressbar.pack(pady=10)
progressbar.start()

# Switch widget oluştur ve yerleştir
switch = ctk.CTkSwitch(root, text="Değiştir")
switch.pack(pady=10)

# Combobox widget oluştur ve yerleştir
combobox = ctk.CTkComboBox(root, values=["Seçenek 1", "Seçenek 2", "Seçenek 3"])
combobox.pack(pady=10)

# TabView widget oluştur ve yerleştir
tabview = ctk.CTkTabview(root)
tabview.pack(pady=10, fill="both", expand=True)

tabview.add("Sekme 1")
tabview.add("Sekme 2")
tabview.add("Sekme 3")

tab1_label = ctk.CTkLabel(tabview.tab("Sekme 1"), text="Sekme 1'in İçeriği")
tab1_label.pack(pady=10)

tab2_label = ctk.CTkLabel(tabview.tab("Sekme 2"), text="Sekme 2'nin İçeriği")
tab2_label.pack(pady=10)

tab3_label = ctk.CTkLabel(tabview.tab("Sekme 3"), text="Sekme 3'ün İçeriği")
tab3_label.pack(pady=10)

# Ana döngüyü çalıştırma
root.mainloop()
