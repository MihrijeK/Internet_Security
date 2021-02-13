#importimi i librarive
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from guizero import  error
import tkinter as tk
import json
import requests
from PIL import Image, ImageTk

#krijimi i nje dritareje permes tkinter
window = Tk()

#ndryshimi i specifikave te dritares
window.configure(bg='#1569C7')
window.title("Ngarkimi i fajllit ne Google Drive")
window.geometry('500x200')
#vendosja e ikones te aplikacionit
window.iconbitmap("img/up.ico")

#krijimi i  variablave te tipit string
token=token_var = tk.StringVar()
folder_var = tk.StringVar()

#krijimi i label l dhe vendosja e specifikave te saj
l = Label(window, text="  Ngarkimi i fajllave ne Google Drive permes Python ",font=('calibre', 12, 'normal'),fg='white',bg='#1569C7')

#percaktimi i pozicionit te label-it ne dritare
l.place(relx=0.1,rely=0.3,anchor=NW)

#vendosja e fotos me size te percaktuar
image = Image. open('img/fotoo.jpg')
image = image. resize((60, 50), Image. ANTIALIAS)
my_img = ImageTk. PhotoImage(image)
panel = Label(window, image = my_img)

#percaktimi i pozicionit te fotos ne dritare
panel.place(relx=0.4,rely=0.5,anchor=NW)


#krijimi i funksionit upload
def upload():
    #fshirja e labels te caktuar pas shtypjes se menus Upload
    panel.destroy()
    l.destroy()

    #krijimi i labels dhe percaktimi i specifikate te tyre
    tk.Label(window, text='Token', font=('calibre', 11, 'normal'), fg='white',bg='#1569C7').place(relx=0.1, rely=0.1, anchor=NE)
    tk.Label(window, text='Folder', font=('calibre', 11, 'normal'), fg='white',bg='#1569C7').place(relx=0.1, rely=0.25, anchor=NE)




def helpp():
    messagebox.showinfo("Help", "Zgjedh Upload dhe vendos nje file ")


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Upload", command=upload)
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=helpp)
menubar.add_cascade(label="Help", menu=helpmenu)
window.config(menu=menubar)
window.mainloop()
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Upload", command=upload)
