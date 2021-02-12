import os
from tkinter import *
from tkinter import messagebox, filedialog
import json
import requests
from pathlib import Path


def upload():
    
    Button(window, text='File', bg="#F0F8FF", command=uploadd).place(relx=0.5, rely=0.5, anchor=CENTER)

def uploadd():

    file = filedialog.askopenfilename(title="Open file")
    name = Path(file).stem
    extension = os.path.splitext(file)[1]
    if extension != ".doc" and extension != ".docx" and extension != ".xls" and extension != ".xlsx":
        print("Dokumenti duhet te  kete ekstension .doc,.doxc,.xls ose .xlsx")
        messagebox.showinfo("Error", "Nuk lejohet ruajtja e dokumentit te tille")
        messagebox.showinfo("Informacion", "Dokumenti duhet te  kete ekstension .doc,.doxc,.xls ose .xlsx")
