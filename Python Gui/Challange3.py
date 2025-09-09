from tkinter import *
import os

# --- Functions ---
def store():
    if not os.path(r"../docs/DancerEntry.txt"):
        with open (r"../docs/DancerEntry.txt") as f :
            f.write()
    else:
        with open (r"../docs/DancerEntry.txt") as f :
            f.write()



# --- GUI Here ---
root = Tk()


root.geometry("600x200")


Name = Label(root,Text="Name")
Age = Label(root,Text="Age")
Date_of_Birth= Label(root,Text="D.O.B")

stringVar = StringVar()
intVar = IntVar()

NameEntry = Entry(root,textvariable=stringVar)
AgeEntry = Entry(root,textvariable=intVar)
Date_of_Birth_Entry= Entry(root,textvariable=intVar)

NameEntry.grid(row=0,column=1)
AgeEntry.grid(row=0,column=2)
Date_of_Birth_Entry.grid(row=0,column=3)




root.mainloop()