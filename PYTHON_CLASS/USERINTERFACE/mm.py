import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My GUI")
root.geometry("910x540")
root.configure(bg="#f0f0f0")

frm1 = tk.Frame(root,relief="ridge", borderwidth=2, height=400, width=780)
frm1.grid(row=0, column=0, sticky="nswe", padx=10, pady=5)

frm2 = tk.Frame(root,relief="ridge", borderwidth=2, height=200, width=780)
frm2.grid(row=1, column=0, sticky="we", padx=10, pady=5)

frm3 = tk.Frame(root,relief="ridge", borderwidth=2, height=200, width=780)
frm3.grid(row=2, column=0, sticky="we", padx=10, pady=5)

#Frame 1 
#Title of Frame
lblTitle = tk.Label(frm1, text="SENSOR READS", font= ("Arial",16), bd=1, relief="sunken")
lblTitle.grid(row=0, column=0, columnspan=5, padx=10,pady=10,sticky="nswe")
              
lbl1 = tk.Label(frm1, text="Label1", font=("Arial",16))
lbl1.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

lbl2 = tk.Label(frm1, text="Label2", font=("Arial",16))
lbl2.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

lbl3 = tk.Label(frm1, text="Label3", font=("Arial",16))
lbl3.grid(row=1, column=2, sticky="nsew", padx=10, pady=5)

lbl4 = tk.Label(frm1, text="Label4", font=("Arial",16))
lbl4.grid(row=1, column=3, sticky="nsew", padx=10, pady=5)

lbl5 = tk.Label(frm1, text="Label5", font=("Arial",16))
lbl5.grid(row=1, column=4, sticky="nsew", padx=10, pady=5)

lbl_en1 = tk.Label(frm1, text="", width=10, font=("Arial", 16), bd=1, relief="sunken")
lbl_en1.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

lbl_en2 = tk.Label(frm1, text="", width=10, font=("Arial", 16), bd=1, relief="sunken")
lbl_en2.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

lbl_en3 = tk.Label(frm1, text="", width=10, font=("Arial", 16), bd=1, relief="sunken")
lbl_en3.grid(row=2, column=2, sticky="nsew", padx=10, pady=5)

lbl_en4 = tk.Label(frm1, text="", width=10, font=("Arial", 16), bd=1, relief="sunken")
lbl_en4.grid(row=2, column=3, sticky="nsew", padx=10, pady=5)

lbl_en5 = tk.Label(frm1, text="", width=10, font=("Arial", 16), bd=1, relief="sunken")
lbl_en5.grid(row=2, column=4, sticky="nsew", padx=10, pady=5)

#Frame 2
lblTitle = tk.Label(frm2, text="RECEPIES TO SET", font= ("Arial",16), bd=1, relief="sunken")
lblTitle.grid(row=0, column=0, columnspan=6, padx=10,pady=10,sticky="nswe")
              
lbl1 = tk.Label(frm2, text="Label1", font=("Arial",16))
lbl1.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

lbl2 = tk.Label(frm2, text="Label2", font=("Arial",16))
lbl2.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

lbl3 = tk.Label(frm2, text="Label3", font=("Arial",16))
lbl3.grid(row=1, column=2, sticky="nsew", padx=10, pady=5)

lbl4 = tk.Label(frm2, text="Label4", font=("Arial",16))
lbl4.grid(row=1, column=3, sticky="nsew", padx=10, pady=5)

lbl5 = tk.Label(frm2, text="Label5", font=("Arial",16))
lbl5.grid(row=1, column=4, sticky="nsew", padx=10, pady=5)


lbl6 = tk.Label(frm2, text="Label5", font=("Arial",16))
lbl6.grid(row=1, column=5, sticky="nsew", padx=10, pady=5)

txt0 = tk.Text(frm2, width=10, height=1, font=("Arial", 16), bd=1, relief="sunken")
txt0.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

txt1 = tk.Text(frm2, width=10, height=1, font=("Arial", 16), bd=1, relief="sunken")
txt1.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

txt2 = tk.Text(frm2, width=10, height=1, font=("Arial", 16), bd=1, relief="sunken")
txt2.grid(row=2, column=2, sticky="nsew", padx=10, pady=5)

txt3 = tk.Text(frm2, width=10, height=1, font=("Arial", 16), bd=1, relief="sunken")
txt3.grid(row=2, column=3, sticky="nsew", padx=10, pady=5)

txt4 = tk.Text(frm2, width=10, height=1, font=("Arial", 16), bd=1, relief="sunken")
txt4.grid(row=2, column=4, sticky="nsew", padx=10, pady=5)

cmb = ttk.Combobox(frm2, values=["Marul", "Salatalık"], width=10, font=("Arial", 16))
cmb.grid(row=2, column=5, sticky="nsew", padx=10, pady=5)

#Frame 3
lblTitle = tk.Label(frm3, text="MANUAL OVERRIDE", font=("Arial", 16), bd=1, relief="sunken")
lblTitle.grid(row=0, column=0, columnspan=6, padx=10, pady=5, stick="nsew")

btn1 = tk.Button(frm3, text = "ON", font=("Arial", 16) ,background="lightgreen")
btn1.grid(row=1,column=0)



# Set the weight of each column in frm1 to 1
for i in range(5):
    frm1.columnconfigure(i, weight=1)
    frm2.columnconfigure(i, weight=1)
    frm3.columnconfigure(i,weight=1)
root.mainloop()