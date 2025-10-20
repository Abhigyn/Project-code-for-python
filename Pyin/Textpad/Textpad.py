from tkinter import *
from tkinter import messagebox as mg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import sys # Added to help locate bundled resources

# --- Helper function to find the resource path in PyInstaller environment ---
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# ---------------------------------------------------------------------------

def newFile():
    global File
    root.title("Untitle - Textpad")
    File = None
    Textarea.delete(1.0,END)

def openFile():
    global File
    # Note: I corrected the spelling of "Document" in filetypes
    File = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    if File == "":
        File = None
    else:
        root.title(os.path.basename(File) + " - Text Pad")
        Textarea.delete(1.0,END)
        try:
            with open(File,"r") as f:
                Textarea.insert(1.0,f.read())
        except Exception as e:
            mg.showerror("Error", f"Could not read file: {e}")
            File = None # Clear file reference on error

def saveFile():
    global File
    if File == None:
        # Note: I corrected the spelling of "Untiled" to "Untitled"
        File = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if File == "":
            File = None
        else:
            try:
                with open(File,"w") as f:
                    f.write(Textarea.get(1.0,END))
                root.title(os.path.basename(File) + " - Text Pad")
            except Exception as e:
                 mg.showerror("Error", f"Could not save file: {e}")
                 File = None
    else:
        try:
            with open(File,"w") as f:
                f.write(Textarea.get(1.0,END))
        except Exception as e:
            mg.showerror("Error", f"Could not save file: {e}")
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

    # --- UPDATED ICON LINE ---
    # Use the resource_path helper function to correctly load the icon
    # It now looks for 'Textpad.ico'
    try:
        root.iconbitmap(resource_path('Textpad.ico'))
    except TclError:
        print("Could not load Textpad.ico. Running without custom icon.")


    Textarea = Text(root, font="lucida 13")
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

    # Scrollbar setup
    scroll_y = Scrollbar(Textarea)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x = Scrollbar(Textarea,orient=HORIZONTAL)
    scroll_x.pack(side=BOTTOM,fill=X)

    Textarea.config(yscrollcommand = scroll_y.set, xscrollcommand = scroll_x.set)

    scroll_y.config(command=Textarea.yview)
    scroll_x.config(command=Textarea.xview)

    root.mainloop()
