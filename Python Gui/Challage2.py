from tkinter  import *


# --- Function ---
def name():
    return print("My Creater name is Abhigyan")

def WhileWorking():
    return print("My Creater is Just a Student")

def celsius_to_fahrenheit():
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    return print(f"{celsius}°C = {fahrenheit}°F")

def square_number():
    num = 7
    return print(f"Square of {num} is {num * num}")

root = Tk()
root.geometry("900x600")
root.minsize(630,100)
b1 = Button(root,fg="blue",text="Print name of creater",bg="red",command= name)
b1.pack(side=LEFT,anchor="nw")
b2 = Button(root,fg="blue",text="Print celsius of 25 into fahrenheit",bg="red",command=celsius_to_fahrenheit)
b2.pack(side=LEFT,anchor="nw")
b3 = Button(root,fg="blue",text="print square of 7",bg="red",command=square_number)
b3.pack(side=LEFT,anchor="nw")
b4 = Button(root,fg="blue",text="During creation of it profaction of creater",bg="red",command=WhileWorking)
b4.pack(side=LEFT,anchor="nw")




root.mainloop()