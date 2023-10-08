# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:16:47 2023

@author: Elif
"""

#Login sayfası
import random
import time
import datetime
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import *
import mysql.connector

def toggle_eye():
    if psEntry.cget("show") == "":
        psEntry.config(show="•")
        eye_button.config(image=eye_image_close)
    else:
        psEntry.config(show="")
        eye_button.config(image=eye_image_open)

def twitter_open():
    print("twitter üzerinden çalışılacak")

def linked_open():
    print("linkedin üzerinden çalışılacak")

def gmail_open():
    print("gmail üzerinden çalışacak")

def open_link():
    print("çalışıyor")
    root.destroy()
    import Register

def home():
    entered_username = unEntry.get()
    entered_password = psEntry.get()

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="database"  
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM data WHERE username = %s AND password = %s", (entered_username, entered_password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            root.destroy()
            import Home
        else:
            # Başarısız giriş
            messagebox.showerror("Error", "Invalid username or password")
            psEntry.delete(0, END)
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")


root = Tk()
root.title("Log In")
root.geometry("500x550")
root.configure(background="#8D7688")
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)

# Kullanılacak veriler
username = StringVar()
password = StringVar()

# SignIn Label
signLabel = LabelFrame(root, bd=2, relief=RIDGE)
signLabel.configure(background="#F1EEDB")
signLabel.place(x=100, y=70, width=300, height=300)

# Alternatif
alabel = LabelFrame(root, bd=2, relief=RIDGE)
alabel.configure(background="#F1EEDB")
alabel.place(x=75, y=380, width=350, height=55)

# İçindeki yazılar kısmı
title = Label(signLabel, font=("arial", 12, "bold"), text="LOG IN", foreground="#725368", background="#F1EEDB")
title.place(x=124, y=50)

# username kısmı
unlabel = Label(signLabel, font=("arial", 12), text="Username", foreground="#725368", background="#F1EEDB")
unlabel.place(x=25, y=100)

# password kısmı
pslabel = Label(signLabel, font=("arial", 12), text="Password", foreground="#725368", background="#F1EEDB")
pslabel.place(x=25, y=150)

# Entry
unEntry = Entry(signLabel, font=("arial", 12), textvariable=username, width=15)
unEntry.place(x=115, y=100)

# Password
psEntry = Entry(signLabel, font=("arial", 12), textvariable=password, width=15, show="•")
psEntry.place(x=115, y=150)

# link oluşturalım
linkButton = Button(signLabel, text="Create new one", command=open_link, background="#F1EEDB", foreground="black",font=("Open Sans",9,"bold underline"),
                    fg="black",bg="#F1EEDB",activeforeground="#C19185",activebackground="#F1EEDB",cursor="hand2",bd=0)
linkButton.place(x=100, y=255)

# Button oluşturma
loginButton = Button(signLabel, text="Log In", command=home, background="#C19185", foreground="white", width=20, font=("arial", 10, "bold"))
loginButton.place(x=65, y=200)

# alternatif label için oluşturulmuş kısım
gmail_image = PhotoImage(master=alabel, file="gmail.png")
gmail_button = Button(master=alabel, text="Gmail", image=gmail_image, command=gmail_open, compound="left", background="#F1EEDB", foreground="#D2B48C", font="Arial 10", width=100, height=30)
gmail_button.photo = gmail_image  
gmail_button.place(x=6, y=8)

linked_image = PhotoImage(master=alabel, file="linkedin.png")
linked_button = Button(master=alabel, text="LinkedIn", image=linked_image, command=linked_open, compound="left", background="#F1EEDB", foreground="#D2B48C", font="Arial 10", width=100, height=30)
linked_button.photo = linked_image  
linked_button.place(x=120, y=8)

twitter_image = PhotoImage(master=alabel, file="twitter.png")
twitter_button = Button(master=alabel, text="Twitter", image=twitter_image, command=twitter_open, compound="left", background="#F1EEDB", foreground="#D2B48C", font="Arial 10", width=100, height=30)
twitter_button.photo = twitter_image  
twitter_button.place(x=233, y=8)

eye_image_open = PhotoImage(master=signLabel, file="openeye.png")
eye_image_close = PhotoImage(master=signLabel, file="closeye.png")

eye_button = Button(master=signLabel, image=eye_image_close, command=toggle_eye, background="#F1EEDB", bd=0)
eye_button.place(x=260, y=150)

root.mainloop()
