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
    else:
        headers = {
        "Authorization": "Bearer "
                         "ya29.A0AfH6SMA3xNK3SsiMBh-GELHA5OzNswxynJUCPD9jK1dj5V92a2ONWF6jSuD1cJXJRLckA_bvxFE1tW-_ik3O1W-P785e9ypZnIbhTBypKC6rgCoJxudiwrdVex5PPeKBvB0DH5coWI1qlO_hlYrcm2tGSF-I"}
        para = {
        "name": name,
        "parents": ["1KUB53Qiow3i1Rs_ufhAZJX-o07G1hFYs"]
         }

        files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(file, "rb")
        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files

        )
        print(r.text)
