from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile, askopenfile

def savefile():
    sfiles = [('all files', '*.*'),('python files', '*.py'),('text files', '*.txt')]
    sfile = asksaveasfile(filetypes = sfiles, defaultextension = sfiles)

def openfile():
    ofile = askopenfile(mode='r', filetypes = [('all files', '*.*'),('python files', '*.py'), ('text files', '*.txt')])
    if ofile:
        content = ofile.read()
        print(content)

root = Tk()
root.geometry("100x100")
root.title("filehandling")

sbutton = Button(root, text="save", command=savefile)
sbutton.pack()

obutton = Button(root, text="open", command=openfile)
obutton.pack()

root.mainloop()