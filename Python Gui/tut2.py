from tkinter import *

import os
import tkinter.messagebox as tkmsg

# gui logic  here

root = Tk()
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

# def getvalue():
#     print(f"The username is {uservalue.get()}")
#     print(f"The password is {Passwordvalue.get()}")

# user = Label(root,text="Username")
# Password = Label(root,text="Password")
# user.grid()
# Password.grid()

# uservalue = StringVar()
# Passwordvalue = StringVar()

# userentry = Entry(root,textvariable = uservalue)
# Passwordentry = Entry(root,textvariable = Passwordvalue)

# userentry.grid(row=0,column=1)
# Passwordentry.grid(row=1,column=1)

# Button(text="Submit",command=getvalue).grid()

# Label(root,text="Welcome To Legend Travels",font="Comicsansms 13 bold").grid(row=0,column=3)

# name = Label(root,text="Name")
# Phone = Label(root,text="Phone")
# Gender = Label(root,text="Gender")
# Emergency_Contact = Label(root,text="Emergency Contact")
# Payment_Methoud = Label(root,text="Payment Methoud")

# name.grid(row=1,column=1)
# Phone.grid(row=2,column=1)
# Gender.grid(row=3,column=1)
# Emergency_Contact.grid(row=4,column=1)
# Payment_Methoud.grid(row=5,column=1)

# namevalue = StringVar()
# Phonevalue = StringVar()
# Gendervalue = StringVar()
# Emergency_Contactvalue = StringVar()
# Payment_Methoudvalue = StringVar()
# foodservicevalue = StringVar()

# namentry = Entry(root,textvariable=namevalue)
# Phonentry = Entry(root,textvariable=Phonevalue)
# Genderentry = Entry(root,textvariable=Gendervalue)
# Payment_Methoudentry = Entry(root,textvariable=Payment_Methoudvalue)
# Emergency_Contactentry = Entry(root,textvariable=Emergency_Contactvalue)
# foodservicentry = Entry(root,textvariable=foodservicevalue)

# namentry.grid(row=1,column=2)
# Phonentry.grid(row=2,column=2)
# Genderentry.grid(row=3,column=2)
# Emergency_Contactentry.grid(row=4,column=2)
# Payment_Methoudentry.grid(row=5,column=2)

# foodservice = Checkbutton(text="Want your prebook meals",variable=foodservicevalue)
# foodservice.grid(row=6,column=2)

# def store():
#     filepath = "../docs/LegendTravelsEntry.txt"
#     os.makedirs(os.path.dirname(filepath), exist_ok=True)

#     with open(filepath, "a") as f:
#         f.write(f"Name: {namevalue.get()}, Gender: {Gendervalue.get()}, Phone No: {Phonevalue.get()}Emergency Contact:  {Emergency_Contactvalue.get()} PaymentMethod:{Payment_Methoudvalue.get()} foodservice:{foodservicevalue.get()}\n")
#     print("✅ Participant entry saved successfully!")

# Button(text="Submit To LegendTravels",command=store).grid(row=7,column=2)

# def harry():
#     print("Work")

# def Help():
#     tkmsg.showinfo("Help Windoe","I will help you")

# def Rate():
#     ValueM = tkmsg.askquestion("Rating Window","Was your experince good?")
#     if ValueM == "Yes":
#         msg = ("Great, Rate us on appstore")
#     else:
#         msg= ("Tell us What went wrong. We will call you")
#     tkmsg.showinfo("Experince", msg)



canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")


# can_widget = Canvas(root,width=canvas_width,height=canvas_height)
# can_widget.pack()
# can_widget.create_line(0,0,800,400,fill="red")
# can_widget.create_line(0,400,800,0,fill="red")
# can_widget.create_rectangle(3,5,700,300,fill="blue")
# can_widget.create_text(400,200,text="Python")
# can_widget.create_oval(3,5,700,300)

# widget = Button(root,text="Click me please")
# widget.grid()
# widget.bind("<Button-1>", harry)
# widget.bind("<Double-1>c", quit)

# mymenu = Menu(root)
# mymenu.add_command(label="file",command=harry)
# mymenu.add_command(label="exit",command=quit)
# root.config(menu=mymenu)

# Mainmenubar = Menu(root)
# m1 = Menu(Mainmenubar,tearoff=0)
# m1.add_command(label="New project",command=harry)
# m1.add_command(label="Print",command=harry)
# m1.add_separator()
# m1.add_command(label="Save",command=harry)
# m1.add_command(label="Save as",command=harry)
# Mainmenubar.add_cascade(label="File",menu=m1)
# m2 = Menu(Mainmenubar,tearoff=0)
# m2.add_command(label="copy",command=harry)
# m2.add_command(label="Paste",command=harry)
# m2.add_command(label="Cut",command=harry)
# m2.add_separator()
# m2.add_command(label="Find",command=harry)
# Mainmenubar.add_cascade(label="Edit",menu=m2)
# m3 = Menu(Mainmenubar,tearoff=0)
# m3.add_command(label="Help",command=Help)
# m3.add_command(label="Rate Us",command=Rate)
# Mainmenubar.add_cascade(label="About Us",menu=m3)

# root.config(menu=Mainmenubar)

# myslider = Scale(root,from_=0, to=100)
# myslider.pack()

# def getdolars():
#     tkmsg.showinfo("Amount Credtided!",f"We have credted {myslider2.get()} dollars to your bank accont")

# Label(root,text="How many dollars you want?").pack

# myslider2 = Scale(root,from_=0, to=100,orient=HORIZONTAL,tickinterval=50)
# myslider2.set(2)
# myslider2.pack()
# Button(root,text="Get $$",command=getdolars).pack()

# def order():
#     food_items = {1: "Dosa", 2: "Idly", 3: "Paratha", 4: "Samosa"}
#     choice = var.get()
#     if choice in food_items:
#         tkmsg.showinfo("Received Your Order!",
#                       f"We have received your order: {food_items[choice]}.\nThanks for ordering!")
#     else:
#         tkmsg.showwarning("No Selection", "Please select something before submitting!")

# var = IntVar()
# # var.set(1)

# Label(root,text="What would you like to have sir?",justify=LEFT,padx=14,font="lucida 19 bold").pack()

# radio = Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack(anchor="w")
# radio = Radiobutton(root,text="Idly",padx=14,variable=var,value=2).pack(anchor="w")
# radio = Radiobutton(root,text="Paratha",padx=14,variable=var,value=3).pack(anchor="w")
# radio = Radiobutton(root,text="Samosa",padx=14,variable=var,value=4).pack(anchor="w")


# Button(text="Sumit your order!",command=order).pack()
# def Add():
#     global i
#     lbx.insert(ACTIVE,f"{i}")
#     i+=1
# i = 0
# lbx = Listbox(root)
# lbx.pack()
# lbx.insert(END,"First item of listbox")

# Button(root,text="Add item",command=Add).pack()

# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT,fill=Y)

# listbox = Listbox(root,yscrollcommand=scrollbar.set)
# for i in range(344):
#     listbox.insert(END,f"Item{i}")

# listbox.pack(fill=BOTH)
# scrollbar.config(command=listbox.yview)

# def upload():
#     statusvar.set("Busy..")
#     sbar.update()
#     import time
#     time.sleep(2)
#     statusvar.set("Ready")


# statusvar = StringVar()
# statusvar.set("Ready")
# sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor=W)
# sbar.pack(side=BOTTOM,fill=X)
# Button(root,text="Upload",command=upload).pack()

# class GUI(Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("500x400")

#     def Status(self):
#         self.var = StringVar()
#         self.var.set("Ready")
#         self.Statusbar = Label(self,textvariable=self.var,relief=SUNKEN,anchor=W)
#         self.Statusbar.pack(side=BOTTOM,fill=X)

# if __name__ == "__main__":
#     Window = GUI()
#     Window.Status()
#     Window.mainloop()

# root.wm_iconbitmap(r"I:\Study\Golu lession\Python      Projects\images\icon.ico")
# width = root.winfo_screenheight()
# height = root.winfo_screenheight()
# print(f"{width}x{height}")
# Button(root,text="Close",command=root.destroy).pack()


root.mainloop()