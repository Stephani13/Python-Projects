import webbrowser
from tkinter import *


class Window:
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x300')
        self.master.title('Web Generator')

        self.varEntry = StringVar()

        self.btnSubmit=Button(self.master, text= "Submit", command = self.submit)
        self.btnSubmit.grid(row=3, column = 0)

        self.lblEnter = Label(self.master, text= "Enter content here")
        self.lblEnter.grid(row=0 , column= 0)

        self.text = Entry(self.master, text=self.varEntry)
        self.text.grid(row=1, rowspan = 2 ,column=0)

    def submit(self):
        text = self.varEntry.get()
        text1 = "\
            <html>\
                <body>\
                    <h1>\
                {}\
                    </h1>\
                </body>\
            </html>".format(text)

        file = open("chalenge_html.html", "w")
        file.write(text)
        file.close()

        webbrowser.open_new_tab("chalenge_html.html")


        
        






if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root = mainloop()
        
