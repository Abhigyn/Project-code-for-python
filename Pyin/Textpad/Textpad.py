from tkinter import *
from tkinter import messagebox as mg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global File
    root.title("Untitle - Textpad")
    File = None
    Textarea.delete(1.0,END)

def openFile():
    global File
    File = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Doucument","*.txt")])
    if File == "":
        File = None
    else:
        root.title(os.path.basename(File) + " - Text Pad")
        Textarea.delete(1.0,END)
        f = open(File,"r")
        Textarea.insert(1.0,f.read())
        f.close()

def saveFile():
    global File
    if File == None:
        File = asksaveasfilename(initialfile="Untiled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Doucument","*.txt")])
        if File == "":
            File = None
        else:
            f = open(File,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(File) + " - Text Pad")
    else:
        f = open(File,"w")
        f.write(Textarea.get(1.0,END))
        f.close()
def quitApp():
    root.destroy()
def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def About():
    mg.showinfo("Text Pad","Text Pad made by Abhigyan Deepak")


if __name__ == "__main__":
    root = Tk()
    root.title("Textpad")
    root.geometry("500x400")

    Textarea = Text(root, font="lucida 13 ")
    Textarea.pack(fill=BOTH,expand=True)
    File = None

    MenuBar = Menu(root)

    # File Menu
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    # Edit Menu
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # About Menu
    AboutMenu = Menu(MenuBar, tearoff=0)
    AboutMenu.add_command(label="About Textpad", command=About)
    MenuBar.add_cascade(label="About", menu=AboutMenu)

    root.config(menu=MenuBar)

    scroll = Scrollbar(Textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand = scroll.set)

    scroll = Scrollbar(Textarea,orient=HORIZONTAL)
    scroll.pack(side=BOTTOM,fill=X)
    scroll.config(command=Textarea.xview)
    Textarea.config(yscrollcommand = scroll.set)




root.mainloop()
