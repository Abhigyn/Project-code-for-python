from tkinter import *


def newFile():
    pass
def openFile():
    pass
def saveFile():
    pass
def quitApp():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass
def About():
    pass


if __name__ == "__main__":
    root = Tk()
    root.title("Untiled - Textpad")
    root.geometry("500x400")

    Textarea = Text(root, font="lucida 13 ")
    Textarea.pack(fill=BOTH)
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

root.mainloop()
