from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os
import datetime
import sqlite3
import time

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
                transferTimeStamp(self)
                clearInfo(self)
                lastTransfer(self)
                

def onClear(self):
    self.srcfolder.delete(0, 'end')
    self.dstfolder.delete(0, 'end')


def createDB(self):
    conn = sqlite3.connect('dbTransferLog.db')
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS tblTransferTime(ID INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT);")
        conn.commit()
    conn.close()

def transferTimeStamp(self):
    now = time.strftime("%m/%d/%Y %H:%M:%S")
    conn = sqlite3.connect('dbTransferLog.db')
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO tblTransferTime (date) VALUES (?)", (now,))
        conn.commit()
    conn.close()    

def lastTransfer(self):
    conn = sqlite3.connect('dbTransferLog.db')
    with conn:
        c = conn.cursor()
        getLT = c.execute("SELECT date FROM tblTransferTime ORDER BY ID DESC LIMIT 1")
        mostRecent = c.fetchone()
        recentTS = mostRecent[0]
        print (recentTS)
        self.infoWindow.insert(END, recentTS)
    conn.close()    

def clearInfo(self):
    self.infoWindow.delete('1.0', 'end')
      

        


