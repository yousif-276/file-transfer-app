#Introductory project by Yousif Alyousif.
#Function of the app will be to move files from one directory to another.
"Author: Yousif Alyousif"

import tkinter as tk #import library
from tkinter import filedialog
import os
import shutil
import os.path
from tkinter import *


#design the GUI
#create window
window = tk.Tk()
#create title
label = tk.Label(
    text='File Transfer Application',
    fg='black',
    bg='grey'
    
)
#add title to window
label.pack()

#create the open file function
def open():
    window.filename = filedialog.askopenfilename(initialdir="/gui/images", title='Select a file')
    file_name_label = tk.Label(window, text=window.filename).pack()
    if window.filename:
        window.file_name.set(window.filename)
        print(window.filename)
    
#create open file button
open_button = tk.Button(
    text='Browse files',
    fg='black',
    bg='grey',
    width=30,
    height=1,
    command=open
)
#add button to window
open_button.pack()

#create destination function
def open_dir():
    window.directory = filedialog.askdirectory(initialdir="/gui/images", title='Select a destination')
    dir_name_label = tk.Label(window, text=window.directory).pack()   
#create destination button
destination_button = tk.Button(
    text='Choose destination directory',
    fg='black',
    bg='grey',
    width=30,
    height=1,
    command=open_dir
)
#add button to window
destination_button.pack()

#define transfer function
def file_transfer():
    shutil.copy(window.filename, window.directory)
    
#create transfer button
transfer_button = tk.Button(
    text='Transfer file',
    fg='black',
    bg='grey',
    width=30,
    height=1,
    command=file_transfer
)
#add button to window
transfer_button.pack()

#run
window.mainloop()
 


