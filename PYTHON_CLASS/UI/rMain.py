import customtkinter as ctk

# Ana pencereyi oluşturma
root = ctk.CTk()
root.title("CustomTkinter Tüm Widgetlar Örneği")
root.geometry("500x700")
root.minsize(300, 400)  # width, height
# Temayı ayarla (isteğe bağlı)
ctk.set_appearance_mode("dark")  # Seçenekler: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Seçenekler: "blue", "green", "dark-blue"

# Label widget oluştur ve yerleştir
label = ctk.CTkLabel(root, text="Bu bir CustomTkinter Label")
label.place(relx=0.5, rely=0.05, relwidth=0.3,anchor="center")

# Button widget oluştur ve yerleştir
button = ctk.CTkButton(root, text="Tıkla", command=lambda: print("Buton Tıklandı"))
button.place(relx=0.5, rely=0.15, anchor="center")

# Entry widget oluştur ve yerleştir
entry = ctk.CTkEntry(root, placeholder_text="Buraya bir şeyler yazın")
entry.place(relx=0.5, rely=0.25, anchor="center")

# CheckBox widget oluştur ve yerleştir
checkbox = ctk.CTkCheckBox(root, text="Kabul ediyorum")
checkbox.place(relx=0.5, rely=0.35, anchor="center")

# RadioButton widget oluştur ve yerleştir
radiobutton1 = ctk.CTkRadioButton(root, text="Seçenek 1", value=1)
radiobutton1.place(relx=0.5, rely=0.45, anchor="center")
radiobutton2 = ctk.CTkRadioButton(root, text="Seçenek 2", value=2)
radiobutton2.place(relx=0.5, rely=0.55, anchor="center")

# Slider widget oluştur ve yerleştir
slider = ctk.CTkSlider(root, from_=0, to=100)
slider.place(relx=0.5, rely=0.65, anchor="center")

# ProgressBar widget oluştur ve yerleştir
progressbar = ctk.CTkProgressBar(root, mode="indeterminate")
progressbar.set(0.5)  # İlerlemeyi %50'ye ayarla
progressbar.place(relx=0.5, rely=0.75, anchor="center")
progressbar.start()

# Switch widget oluştur ve yerleştir
switch = ctk.CTkSwitch(root, text="Değiştir")
switch.place(relx=0.5, rely=0.85, anchor="center")

# Combobox widget oluştur ve yerleştir
combobox = ctk.CTkComboBox(root, values=["Seçenek 1", "Seçenek 2", "Seçenek 3"])
combobox.place(relx=0.5, rely=0.95, anchor="center")

# TabView widget oluştur ve yerleştir
# tabview = ctk.CTkTabview(root)
# tabview.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.9, anchor="n")

# tabview.add("Sekme 1")
# tabview.add("Sekme 2")
# tabview.add("Sekme 3")

# tab1_label = ctk.CTkLabel(tabview.tab("Sekme 1"), text="Sekme 1'in İçeriği")
# tab1_label.place(relx=0.5, rely=0.5, anchor="center")

# tab2_label = ctk.CTkLabel(tabview.tab("Sekme 2"), text="Sekme 2'nin İçeriği")
# tab2_label.place(relx=0.5, rely=0.5, anchor="center")

# tab3_label = ctk.CTkLabel(tabview.tab("Sekme 3"), text="Sekme 3'ün İçeriği")
# tab3_label.place(relx=0.5, rely=0.5, anchor="center")

# Ana döngüyü çalıştırma
root.mainloop()