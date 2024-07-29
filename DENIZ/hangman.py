import random as rd
import tkinter as tk
from tkinter import messagebox 
d1 = \
""" 
          
          
          
          
          
          
  ____"""
d2 = \
""" 
    |      
    |      
    |      
    |      
    |      
    |      
  __|__"""
d3 = \
"""     _____
    |/      
    |      
    |      
    |      
    |      
    |      
  __|__"""
d4 = \
"""     _____ 
    |/    |
    |     |
    |      
    |      
    |      
    |      
  __|__"""
d5= \
"""     _____ 
    |/    |
    |     |
    |     O 
    |      
    |      
    |      
  __|__"""
d6 = \
"""     _____ 
    |/    |
    |     |
    |     O 
    |     | 
    |     | 
    |      
  __|__"""
d7= \
"""     _____ 
    |/    |
    |     |
    |     O 
    |    /| 
    |     | 
    |      
  __|__"""
d8 = \
"""     _____ 
    |/    |
    |     |
    |     O 
    |    /|\\
    |     | 
    |      
  __|__"""
d9 = \
"""     _____ 
    |/    |
    |     |
    |     O 
    |    /|\\
    |     | 
    |    / 
  __|__"""
d10 = \
"""     _____ 
    |/    |
    |     |
    |     O 
    |    /|\\
    |     | 
    |    / \\
  __|__"""


wordList= [
    "Elma",
    "Araba",
    "Bilgisayar",
    "Kalem",
    "Kitap",
    "Masa",
    "Sandalye",
    "Kapı",
    "Pencere",
    "Telefon",
    "Televizyon",
    "Yatak",
    "Buzdolabı",
    "Çamaşır",
    "Kedi",
    "Köpek",
    "Ayakkabı",
    "Ceket",
    "Pantolon",
    "Gömlek"
]

class AdamAsmaca(tk.Tk):
    def __init__(self):
        super().__init__()
        self.buttons=[]
        self.hangSteps = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
        self.letters = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
        self.count = 10
        self.title("Adam Asmaca")
        self.geometry("400x650")
        self.resizable(False, False)
        self.drawWidgets()
        self.startTheGame()

    def lockTheGame(self):
        for btn in self.buttons:
            btn.config(bg="red", state="disabled")

    def findAllOccurances(self, letter):
        indices = []
        idx = self.pickedWord.find(letter)
        while idx != -1:
            indices.append(idx)
            idx = self.pickedWord.find(letter, idx + 1)
        return indices

    def updateWordMask(self, letter):
        indices = self.findAllOccurances(letter)
        for idx in indices:
            self.wordMask = self.wordMask[:idx] + letter + self.wordMask[idx + 1:]
        

    def startTheGame(self):
        self.pickedWord = rd.choice(wordList).upper()
        print(self.pickedWord)
        self.wordMask = "_"*len(self.pickedWord)
        self.entWord.delete(0,tk.END)
        self.entWord.insert(0,self.wordMask)
        for btn in self.buttons:
            btn.config(bg="white", state="normal")
        self.count = 10
        self.display.delete(0.0,tk.END)

    def onButtonClick(self, button,letter):
        button.config(bg="red", state="disabled")
        if letter in self.pickedWord:
            self.updateWordMask(letter)
            self.entWord.delete(0,tk.END)
            self.entWord.insert(0,self.wordMask)
        else:
            self.count -= 1
                
            if self.count >= 0:
                self.display.delete(0.0, tk.END)
                self.display.insert(0.0,self.hangSteps[(len(self.hangSteps)-self.count)-1])
                
            if self.count == 0:
                self.remaining.config(text=f"{self.count} hakkınız kaldı")
                self.lockTheGame()
                messagebox.showerror("Oyun Bitti", "Kaybettiniz! :(") 


    def drawWidgets(self):
        self.display = tk.Text(self, width=15, height=9,font=("Helvatica",30),state="normal",relief="groove")
        self.display.pack(fill="both")
        self.entWord = tk.Entry(self, text="",width=10,font=("Arial",30),bd=0, justify='center')
        self.entWord.pack(anchor="center", pady=5)

        num_buttons_per_row = 10
        row = 0
        column = 0
        self.frm = tk.Frame(self)
        self.frm.pack(anchor="center", fill="both",pady=5)

        for letter in self.letters:
            button = tk.Button(self.frm, text=letter)
            button.config(command= lambda b=button, l=letter: self.onButtonClick(b,l))
            button.grid(row=row, column=column, padx=1, pady=1)
            self.buttons.append(button)
            
            column += 1
            if column == num_buttons_per_row:
                column = 0
                row += 1

        self.remaining = tk.Label(self.frm, text="", font=("Helvatica",15), )
        self.remaining.grid(row=4, column=0, columnspan=10,pady=10)

        self.reset = tk.Button(self, text="Reset", command=None)
        self.reset.pack(side=tk.LEFT, padx=5, pady=5)
        self.replay = tk.Button(self, text="Play",command=self.startTheGame)
        self.replay.pack(side=tk.LEFT, padx=5, pady=5)


if __name__ == "__main__":
    app = AdamAsmaca()
    app.mainloop()