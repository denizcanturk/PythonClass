#SENDING EMAIL

import smtplib

smptObj =smtplib.SMTP("smtp.gmail.com", 587) #465 or leave empty
smptObj.ehlo()

smptObj.starttls()

passed = input("Password : ")

inport getpass

passwd = getpass.getpass("Password : ")

#generate a password

emain = getpass.getpass("Email : ")
paswd = getpass.getpass("Password ")
smptObj.login(emain,paswd)

#will receive accepted..

from_a = emain
to_a = emain

sub : input()
mesa : input()
msg = "Subject: " +sub +"\n"+ mesa

smptObj.sendMail(from_a, to_a, msg)

# result should be {}

smptObj.quit()
#Closes the connection


#RECEIVING MAILS

