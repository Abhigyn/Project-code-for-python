from tkinter import *
root = Tk()



# gui logic  here
root.geometry("400x100")
root.minsize(200,100)
root.title("My GUI")
# Photo1 = PhotoImage(file=r"../images/bg2.png")
# Image1 = Label(image=Photo1)
# Title_label = Label(text="Chiku is a very bad boy.\nHis realname is Abhinava.\nAbhigyan also know as Golu.\n He is a very good boy", bg="red", fg="Blue", padx= 100,pady= 1,font="comicsansms 19 bold",borderwidth=2,relief= SUNKEN)
# Title_label.pack(anchor=CENTER,fill=X,)
# Title_label.pack(anchor=CENTER,fill=Y,)
# # Image1.pack()
# f2 = Frame(root,borderwidth=9,bg="grey",relief=SUNKEN)
# f2.pack(side=TOP,fill=X)
# l = Label(f2,text="Welocome To Abhigyan Text Editor",font="Helvetica 16 bold",fg="red")
# l.pack()

# f1 = Frame(root, bg="gray",borderwidth=6,relief=SUNKEN)
# f1.pack(side= LEFT,fill= Y)
# l = Label(f1,text="Project Tkinker - Text Editor",fg="blue",font="Helvetica 8 bold")
# l.pack()

# b1 = Button(root,fg="blue",text="Print now",bg="red")
# b1.pack(side=LEFT,anchor="nw")
# b2 = Button(root,fg="blue",text="Print now",bg="red")
# b2.pack(side=LEFT,anchor="nw")
# b3 = Button(root,fg="blue",text="Print now",bg="red")
# b3.pack(side=LEFT,anchor="nw")
# b4 = Button(root,fg="blue",text="Print now",bg="red")
# b4.pack(side=LEFT,anchor="nw")

def getvalue():
    print(f"The username is {uservalue.get()}")
    print(f"The password is {Passwordvalue.get()}")

user = Label(root,text="Username")
Password = Label(root,text="Password")
user.grid()
Password.grid()

uservalue = StringVar()
Passwordvalue = StringVar()

userentry = Entry(root,textvariable = uservalue)
Passwordentry = Entry(root,textvariable = Passwordvalue)

userentry.grid(row=0,column=1)
Passwordentry.grid(row=1,column=1)

Button(text="Submit",command=getvalue).grid()










root.mainloop()


