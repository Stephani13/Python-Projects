import shutil
import os
import datetime
import tkinter
from tkinter import *
from tkinter import filedialog as fd
import os




class Window(Frame):
    def  __init__(self,master):
        Frame.__init__(self)


        self.master = master
        self.master.geometry('400x200')

        self.master.title('Check files')
        


        self.btnBrowse1 = Button(self.master, text="Browse...", command = self.directory)
        self.btnBrowse1.grid(row = 0, column= 0)

        self.btnBrowse2 = Button(self.master, text="Browse...", command = self.directory)
        self.btnBrowse2.grid(row = 1, column= 0)

        self.btnCheck = Button(self.master, text = "Check for files...",width= 15, height = 2)
        self.btnCheck.grid(row = 4, rowspan = 2,column = 0)

        self.btnClose = Button(self.master, text = "Close Program", width= 10, height = 2, command = self.cancel)
        self.btnClose.grid(row = 4, rowspan =2, column = 20 )

        self.txt1 = Entry(self.master, text = '')
        self.txt1.grid(row=0 , column = 1, columnspan = 20)

        self.txt2 = Entry(self.master)
        self.txt2.grid(row=1 , column = 1, columnspan = 20)
    def cancel(self):
        self.master.destroy()

    def directory(self):
        direct = print(fd.askdirectory())
        self.txt1.config(text=direct)

  




if __name__ == "__main__":
    root = Tk()
    App = Window(root)
    root.mainloop()

###set where the source of the files are
##source = '/Users/tiffy/Desktop/B/'
##
###set ddestination path
##destination = '/Users/tiffy/Desktop/A/'
##files = os.listdir(source)
##
##
##for i in files:
##    limit = datetime.datetime.now() + datetime.timedelta(hours=1)
##    if limit > datetime.datetime.now():
##        
        #we are saying move the files represented by 'i' to their new destination
        shutil.copy(source+i, destination)
    
    
