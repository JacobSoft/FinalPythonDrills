# Python 3.6.1
# File Transfer Manager by Jake Clark
# Browse for source and destination folders and transfer them based on modification date

from tkinter import *
from tkinter import ttk
import functions


class fileTransfer:

    def __init__(self, master):
        
        master.panedwindow = ttk.Panedwindow(master, orient = VERTICAL)
        master.panedwindow.pack(fill = BOTH, expand = False)
        master.title("File Manager")
    
        self.frame1 = ttk.Frame(master.panedwindow, width = 480, height = 100, relief = SUNKEN)
        self.frame2 = ttk.Frame(master.panedwindow, width = 480, height = 150, relief = SUNKEN)
        self.frame2.config(padding = (5, 15))
        self.frame3 = ttk.Frame(master.panedwindow, width = 480, height = 100, relief = SUNKEN)
        self.frame3.config(padding = (5, 5))
        self.frame4 = ttk.Frame(master.panedwindow, width = 480, height = 50, relief = SUNKEN)
        self.frame4.config(padding = (5, 5))
    
        master.panedwindow.add(self.frame1, weight = 1)
        master.panedwindow.add(self.frame2, weight = 1)
        master.panedwindow.add(self.frame3, weight = 1)
        master.panedwindow.add(self.frame4, weight = 1)
    
        self.label1 = ttk.Label(self.frame1, text = 'Welcome to File Manager! Please select below:')
        self.label1.pack(fill = BOTH)
        self.logo = PhotoImage(file = 'transfer.png')
        self.label1.config(justify = CENTER,
                         foreground = '#E2EAD9', background = '#CC99FF',
                         font = ("Arial", 14, 'bold'), compound = 'left', image = self.logo)
        
        self.srcfolder = ttk.Entry(self.frame2, width = 80)
        self.srcfolder.pack(anchor = 'nw')
        self.srcfolder.insert(0, 'Browse for source folder...')
        self.btn_browse = ttk.Button(self.frame2, text = 'Browse Source', command = lambda: functions.browseSrcFiles(self))
        self.btn_browse.pack(anchor = 'nw')
                
        self.dstfolder = ttk.Entry(self.frame2, width = 80)
        self.dstfolder.pack(anchor = 'nw')
        self.dstfolder.insert(0, 'Browse for destination folder...')
        self.btn_browse2 = ttk.Button(self.frame2, text = 'Browse Destination', command = lambda: functions.browseDstFiles(self))
        self.btn_browse2.pack(anchor = 'nw')

        self.infoLbl = Label(self.frame3, text = "Most recent file transfer:")
        self.infoLbl.pack()
        self.infoWindow = Text(self.frame3, width = 60, height = 5)
        self.infoWindow.pack()
        
        
        self.btn_transfer = ttk.Button(self.frame4, text = 'Transfer Files!', command = lambda: functions.moveFiles(self))
        self.btn_transfer.grid(row = 0, column = 0)
        self.btn_clear = ttk.Button(self.frame4, text = 'Clear Fields', command = lambda: functions.onClear(self))
        self.btn_clear.grid(row = 0, column = 1)

        functions.createDB(self)
        functions.lastTransfer(self)


            
def main():            

    root = Tk()
    ft = fileTransfer(root)
    root.mainloop()
    
if __name__ == "__main__": main()
