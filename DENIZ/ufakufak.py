#Yaşadığın süre ne kadar?
# from datetime import *

# birth = datetime.strptime(input("Your birth date (d.m.Y): "), "%d.%m.%Y")

# age = datetime.now() - birth

# print("You survived {} seconds.".format(age.total_seconds()))

#------------------------------------------
#Ceasar Encryption

# def encrypt(text, value, output=""):
#     for char in text:
#         output = "{}{}".format(output, chr(ord(char) + value))
#     return output

# def decrypt(text, value, output=""):
#     for char in text:
#         output = "{}{}".format(output, chr(ord(char) - value))
#     return output

# i = int(input("Increment value: "))


# text = input("Type your text: ")

# print("Encrypted text: {}".format(encrypt(text, i)))


# text = input("\nType for decrypt: ")

# print("Decrypted text: {}".format(decrypt(text, i)))

#------------------------------------------
#Parola Oluşturucu

# import random
# import string

# def generate_password(length, level, output=[]):
#     chars = string.ascii_letters
#     if level > 1:
#         chars = "{}{}".format(chars, string.digits)
#     if level > 2:
#         chars = "{}{}".format(chars, string.punctuation)

#     for i in range(length):
#         output.append(random.choice(chars))
#     return "".join(output)

# print(("-" * 30) + "\n Password Generator\n" + ("-" * 30))

# password_length = int(input("Length: "))
# password_level = int(input("Level: "))

# password = generate_password(password_length, password_level)

# print("\nYour password is: {}".format(password))

#---------------------------------------------
#Yeni Yıl Ağacı
# height = int(input("Height of Christmas Tree: "))

# for i in range(int(height * 0.7)):
#     print( (" " * (height - ( i // 2))) + ("*" * i))

# for i in range(int(height * 0.7), height):
#     print((" " * (height - 1)) + "||")

#---------------------------------------------
#Takvim Oluşturucu

# import calendar

# print("Bir yıl girin: ")
# yy = input()
# print("\nBir ay girin (1-12 arasında): ")
# mm = input()

# y = int(yy)
# m = int(mm)
# print("\n", calendar.month(y, m))

#---------------------------------------------
#Geri Sayıcı

# import time


# def countdown(user_time):
#    while user_time >= 0:
#        mins, secs = divmod(user_time, 60)
#        timer = '{:02d}:{:02d}'.format(mins, secs)
#        print(timer, end='\r')
#        time.sleep(1)
#        user_time -= 1
#    print('Lift off!')

# user_time = int(input("Enter a time in seconds: "))
# countdown(user_time)

#---------------------------------------------
#https://data-flair.training/blogs/read-data-from-google-sheets-using-python/
#importing libraries
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# import tkinter as tk
# from tkinter import *

# #creating window
# root = Tk()
# root.geometry('600x650')#geometry of window
# root.title('DataFlair')#title for window
# Label(root,text='Lets Display the Content of This File',font='arial 10').pack()

# s=tk.StringVar()#s is string type
# def read_the_sheet():
#     sheet_to_display=s.get()#get the value of s
# # use creds to create a client to interact with the Google Drive API
#     scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#     creds = ServiceAccountCredentials.from_json_keyfile_name('json file.json', scope)
#     client = gspread.authorize(creds)
# # Find a workbook by name and open the first sheet
# # Make sure you use the right name here.
#     sheet = client.open(sheet_to_display).sheet1
# # Extract and print all of the values
#     display_record = sheet.get_all_records()
#     for i in display_record:
#         Message(root,text=i).pack()#display the details in sheet

# Entry(root,textvariable=s).pack()#entry field
# Button(root,text='Display',bg='red',command=read_the_sheet).pack()#button widget on the window
# root.mainloop()

#------------------------------------------------
