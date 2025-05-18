from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile

def savefile():
    files = [('all files', '*.*'), ('python files', '*.py'), ('text document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)

root = Tk()
root.geometry("100x100")
root.title("filehandling")

savebutton = Button(root, text="save", command=savefile)
savebutton.pack()

root.mainloop()