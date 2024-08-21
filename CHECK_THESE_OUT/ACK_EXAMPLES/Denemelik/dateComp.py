import tkinter as tk
from tkcalendar import DateEntry


def dateChange(event=None):
    date1 = d1.get_date()
    date2 = d2.get_date()
    print(date1)
    print(date2)
    #print(str(date1-date2).split(" ")[0])

pencere = tk.Tk()
pencere.geometry("300x280")
d1 = DateEntry(pencere, date_format="dd-mm-yy")
d1.grid(row=0, column=0, padx=5, pady=5)

d2 = DateEntry(pencere, date_format="dd-mm-yy")
d2.grid(row=0, column=1, padx=5, pady=5)

d2.bind("<<DateEntrySelected>>", dateChange)
d1.bind("<<DateEntrySelected>>", dateChange)
pencere.mainloop()