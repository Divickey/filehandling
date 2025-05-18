from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile

def openfile():
    file = askopenfile(mode = 'r', filetypes = [('all files', '*.*'),('python files', '*.py'), ('text files', '*.txt')])
    if file:
        content = file.read()
        print(content)

root = Tk()
root.geometry("100x100")
root.title("filehandling")

openbutton = Button(root, text="open", command=openfile)
openbutton.pack()



root.mainloop()