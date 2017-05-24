import shutil
import os
import datetime


now = datetime.datetime.now()
print(now)
before = now - datetime.timedelta(hours = 24)
print (before)

def moveFiles():
    source = "C:/Users/Student/Desktop/foldera/"
    files = os.listdir(source)
    destination = "C:/Users/Student/Desktop/folderb/"
    for f in files:
        if f.endswith(".txt"):
            modtime = datetime.datetime.fromtimestamp(os.path.getmtime(source+f))
        if modtime < before:
            src = source+f
            dst = destination+f
            shutil.move(src, dst)

moveFiles()       

        
