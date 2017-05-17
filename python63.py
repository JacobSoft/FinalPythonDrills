import shutil
import os



def moveFiles():
    source = "C:/Users/Student/Desktop/foldera/"
    files = os.listdir(source)
    files.sort()
    destination = "C:/Users/Student/Desktop/folderb/"
    for f in files:
        src = source+f
        dst = destination+f
        shutil.move(src, dst)

moveFiles()       

        
