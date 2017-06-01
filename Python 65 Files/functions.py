from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os
import datetime

def browseSrcFiles(self):
    self.srcfolder.delete(0, 'end')
    directory = filedialog.askdirectory()
    print (directory)
    self.srcfolder.insert(0, directory+'/')

def browseDstFiles(self):
    self.dstfolder.delete(0, 'end')
    directory = filedialog.askdirectory()
    print (directory)
    self.dstfolder.insert(0, directory+'/')


now = datetime.datetime.now()
print(now)
before = now - datetime.timedelta(hours = 24)
print (before)

def moveFiles(self):
    source = self.srcfolder.get()
    files = os.listdir(source)
    destination = self.dstfolder.get()
    for f in files:
        if f.endswith(".txt"):
            modtime = datetime.datetime.fromtimestamp(os.path.getmtime(source+f))
            if modtime > before:
                src = source+f
                dst = destination+f
                shutil.move(src, dst)

def onClear(self):
    self.srcfolder.delete(0, 'end')
    self.dstfolder.delete(0, 'end')          

      

        


