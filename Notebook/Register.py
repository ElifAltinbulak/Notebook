# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:20:35 2023

@author: Elif
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pymysql 
import mysql.connector

def clear():
    usernameEntry.delete(0,tk.END)
    nameEntry.delete(0,tk.END)
    surnameEntry.delete(0,tk.END)
    genderEntry.delete(0,tk.END)
    emailEntry.delete(0,tk.END)
    phonenumberEntry.delete(0,tk.END)
    passwordEntry.delete(0,tk.END)
    cityEntry.delete(0,tk.END)
    countryEntry.delete(0,tk.END)
    
def create_account():
    if username.get() == "" or name.get() == "" or surname.get() == "" or gender.get() == "" or email.get() == "" or password.get() == "" or phonenumber.get() == "" or city.get() == "" or country.get() == "":
        messagebox.showerror("Error", "All Fields Are Required")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="database"
            )
            cursor = mydb.cursor()

            # Kullanıcıyı "data" tablosuna ekle
            data_query = "INSERT INTO data (username, name, surname, gender, email, password, phonenumber, city, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data_values = (
                username.get(),
                name.get(),
                surname.get(),
                gender.get(),
                email.get(),
                password.get(),
                phonenumber.get(),
                city.get(),
                country.get(),
            )
            cursor.execute(data_query, data_values)

            # Yeni kullanıcının ID, kullanıcı adı ve şifresini "user_notes" tablosuna ekle
            user_notes_query = "INSERT INTO user_notes (username, password) VALUES (%s, %s)"
            user_notes_values = (
                username.get(),
                password.get(),
            )
            cursor.execute(user_notes_query, user_notes_values)

            mydb.commit()
            mydb.close()
            messagebox.showinfo("Success", "Registration is successful!")
            clear()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

            
def Login_Screen():
    print("Login Ekranı")
    root1.destroy()
    import Login
#Database oluşturma

root1 = tk.Tk()
root1.title("Register")
root1.geometry("500x550")

# Icon oluşturdum
icon_r = PhotoImage(file="register.png")
root1.iconphoto(False, icon_r)

# Kullanılacak veriler
username = tk.StringVar()
name = tk.StringVar()
surname = tk.StringVar()
gender = tk.StringVar()
email = tk.StringVar()
password = tk.StringVar()
phonenumber = tk.IntVar()
city = tk.StringVar()
country = tk.StringVar()


# Arkaplan değiştirme
background_image = Image.open("resim.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root1, image=background_photo)
background_label.place(relwidth=1, relheight=1)
background_label.image = background_photo

# Label oluştur
rlabel = tk.LabelFrame(root1, bd=3, relief=tk.RIDGE, background="#fefdf8")
rlabel.place(x=70, y=117, width=365, height=355)

# Başlık oluşturma
title = tk.Label(root1, font=("arial", 14, "bold"), text="Register", foreground="#a49882", background="#fefdf8")
title.place(x=70, y=70)

# Label için oluşturuyorum
# username
usernameLabel = tk.Label(rlabel, font=("arial", 12), text="Username", foreground="#5b7782", background="#fefdf8")
usernameLabel.place(x=30, y=30)
usernameEntry = tk.Entry(rlabel, font=("arial", 12), textvariable=username, width=20)
usernameEntry.place(x=150, y=30)
# isim
nameLabel = tk.Label(rlabel, font=("arial", 12), text="Name", foreground="#5b7782", background="#fefdf8")
nameLabel.place(x=30, y=60)
nameEntry = tk.Entry(rlabel, font=("arial", 12), textvariable=name, width=20)
nameEntry.place(x=150, y=60)
# soyadı
surnameLabel = tk.Label(rlabel, font=("arial", 12), text="Surname", foreground="#5b7782", background="#fefdf8")
surnameLabel.place(x=30, y=90)
surnameEntry = tk.Entry(rlabel, font=("arial", 12), textvariable=surname, width=20)
surnameEntry.place(x=150, y=90)
# cinsiyet
genderLabel = tk.Label(rlabel, font=("arial", 12), text="Gender", foreground="#5b7782", background="#fefdf8")
genderLabel.place(x=30, y=120)
# cinsiyet Combobox
genderEntry = ttk.Combobox(rlabel, textvariable=gender, font=("arial", 12), values=("Woman", "Man", "I don't want to specify"), width=18)
genderEntry.place(x=150, y=120)
# Email
emailLabel = tk.Label(rlabel, font=("arial", 12), text="Email", foreground="#5b7782", background="#fefdf8")
emailLabel.place(x=30, y=150)
emailEntry = tk.Entry(rlabel, font=("arial", 12), textvariable=email, width=20)
emailEntry.place(x=150, y=150)
# phonenumber
phonenumberLabel = tk.Label(rlabel, font=("arial", 12), text="Phone Number", foreground="#5b7782", background="#fefdf8")
phonenumberLabel.place(x=30, y=180)
phonenumberEntry = tk.Entry(rlabel, font=("arial", 12), textvariable=phonenumber, width=20)
phonenumberEntry.place(x=150, y=180)
# country
countryLabel = tk.Label(rlabel, font=("arial", 12), text="Country", foreground="#5b7782", background="#fefdf8")
countryLabel.place(x=30, y=210)
countryEntry = tk.Entry(rlabel, font=("arial", 12), textvariable=country, width=20)
countryEntry.place(x=150, y=210)
# city
cityLabel = tk.Label(rlabel, font=("arial", 12), text="City", foreground="#5b7782", background="#fefdf8")
cityLabel.place(x=30, y=240)
cityEntry = tk.Entry(rlabel, font=("arial", 12), textvariable=city, width=20)
cityEntry.place(x=150, y=240)
# password
passwordLabel = tk.Label(rlabel, font=("arial", 12), text="Password", foreground="#5b7782", background="#fefdf8")
passwordLabel.place(x=30, y=270)
passwordEntry = tk.Entry(rlabel, font=("arial", 12), textvariable=password, width=20)
passwordEntry.place(x=150, y=270)
# bilgilerini kaydet
registerButton = tk.Button(rlabel, text="Create Account", command=create_account, background="#ddc6b4", foreground="white", font=("arial", 12, "bold"))
registerButton.place(x=200, y=300)
# login ekranı
loginButton = tk.Button(rlabel, text="Sign in", command=Login_Screen, background="#fefdf8", foreground="black",
                     activeforeground="#ddc6b4", font=("Open Sans", 9, "bold underline"), activebackground="white", cursor="hand2", bd=0)
loginButton.place(x=30, y=320)

root1.mainloop()

