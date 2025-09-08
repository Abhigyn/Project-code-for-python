from tkinter import  * 


root = Tk()

root.geometry("900x600")
root.minsize(300,200)
Text_bottom = Label(text="Programme is ready",bg="blue",fg="red",font="comicsansms 19 bold",borderwidth=2,relief= SUNKEN)
Text_bottom.pack(side=BOTTOM,fill="x")

root.mainloop()

