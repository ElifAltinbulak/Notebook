
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="database"
)

cursor = mydb.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS user_notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    note TEXT
)
"""

cursor.execute(create_table_query)
mydb.commit()

def send_message():
    message = messageEntry.get()
    if message:
        chat_text.config(state=tk.NORMAL)
        chat_text.insert(tk.END, "My new note: " + message + "\n")
        chat_text.config(state=tk.DISABLED)
        messageEntry.delete(0, tk.END)

def show_notes():
    note_text = messageEntry.get()  
    if note_text:
        try:
            # Kullanıcının notunu eklemek için kullanıcı adını alın
            user_name_query = "SELECT username FROM user_notes WHERE id = 1"
            cursor.execute(user_name_query)
            user_name = cursor.fetchone()[0]

            insert_query = "INSERT INTO user_notes (username, note) VALUES (%s, %s)"
            insert_values = (user_name, note_text)
            cursor.execute(insert_query, insert_values)
            mydb.commit()
            messagebox.showinfo("Success", "Note saved successfully!")
            messageEntry.delete(0, tk.END)  
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

def setting_open():
    print("setting açılacak")

def close_window():
    root2.destroy()

def sil():
    uyarı = messagebox.askokcancel("Uyarı", "Tüm veriler silinecek!\nDevam etmek istiyor musunuz?")
    if uyarı:  
        chat_text.config(state=tk.NORMAL)
        chat_text.delete(1.0, tk.END)  
        messagebox.showinfo("Bilgi", "Tüm veriler başarıyla silindi.")

root2 = tk.Tk()
root2.title("Home")
root2.geometry("500x550")

# Icon oluşturma
icon_r = PhotoImage(file="home.png")
root2.iconphoto(False, icon_r)

# Arkaplan değiştirme
background_image = Image.open("resim1.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root2, image=background_photo)
background_label.place(relwidth=1, relheight=1)
background_label.image = background_photo

# Label oluşturma
homeLabel = tk.LabelFrame(root2, bd=1, relief=tk.RIDGE)
homeLabel.configure(background="#f4f4f0")
homeLabel.place(x=0, y=0, width=500, height=50)

# Label oluşturma
chatLabel = tk.Label(root2, bd=1, relief=tk.RIDGE)
chatLabel.configure(background="#f4f4f0")
chatLabel.place(x=0, y=490, width=500, height=60)

# Label üzerinde bilgileri dolduralım
# Username
username = tk.Label(homeLabel, text="Username:", fg="#cea68f", bg="#f4f4f0", font=("arial", 10, "bold"))
username.place(x=60, y=1)
# not
note = tk.Label(homeLabel, text="Notlarınızı kayıt altında tutunuz", fg="#cea68f", bg="#f4f4f0", font=("arial", 10, "bold"))
note.place(x=60, y=20)

# Profil fotoğrafını ekleyin
profil_image = Image.open("profile.png")
profil_photo = ImageTk.PhotoImage(profil_image)
profil_label = tk.Label(homeLabel, image=profil_photo, bg="#f4f4f0", width=40, height=40)
profil_label.image = profil_photo
profil_label.place(x=10, y=0)

#Silgi
silgi_image = PhotoImage(master=homeLabel, file="silgi.png")
silgi_button = tk.Button(master=homeLabel, image=silgi_image, command=sil, background="#f4f4f0", bd=0, width=40, height=45)
silgi_button.photo = silgi_image
silgi_button.place(x=350, y=0)

#Kayıt
kayıt_image = PhotoImage(master=homeLabel, file="save.png")
kayıt_button = tk.Button(master=homeLabel, image=kayıt_image, command=show_notes, background="#f4f4f0", bd=0, width=40, height=45)
kayıt_button.photo = kayıt_image
kayıt_button.place(x=300, y=0)

# Ayarlar
setting_image = PhotoImage(master=homeLabel, file="setting.png")
setting_button = tk.Button(master=homeLabel, image=setting_image, command=setting_open, background="#f4f4f0", bd=0, width=40, height=45)
setting_button.photo = setting_image  # PhotoImage nesnesini saklayın
setting_button.place(x=400, y=0)

#Çıkış
closed_image = PhotoImage(master=homeLabel, file="closed.png")
closed_button = tk.Button(master=homeLabel, image=closed_image, command=close_window, background="#f4f4f0", bd=0, width=40, height=45)
closed_button.photo = closed_image
closed_button.place(x=450, y=0)

# Send tuşu
send_image = PhotoImage(master=chatLabel, file="image/send.png")
send_button = tk.Button(master=chatLabel, image=send_image, command=send_message, background="#f4f4f0", bd=0, width=45, height=55)
send_button.photo = send_image
send_button.place(x=0, y=0)

# Entry oluşturma 
messageEntry = tk.Entry(master=chatLabel, background="#f4f4f0", font=("arial", 12), width=45, bd=0)
messageEntry.place(x=50, y=15)

# Mesajları görüntülemek için Text bileşeni
chat_text = tk.Text(root2, wrap=tk.WORD, state=tk.DISABLED, bg="#fdfaf7", height=10, bd=1)
chat_text.place(x=27, y=80, width=450, height=390)

# Scrollbar 
scrollbar = tk.Scrollbar(chat_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_text.config(state=tk.NORMAL, yscrollcommand=scrollbar.set)
scrollbar.config(command=chat_text.yview)

# Label 
line = tk.Frame(master=chatLabel, width=410, height=2, bg="#d0d2be")
line.place(x=50, y=40)

user_label = tk.Label(homeLabel, fg="#cea68f", bg="#f4f4f0", font=("arial", 10, "bold"))
user_label.place(x=132, y=1)  

root2.mainloop()
