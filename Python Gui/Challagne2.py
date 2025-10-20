from tkinter import *
# It's good practice to import messagebox for showing errors
from tkinter import messagebox


# --- Functions ---
def name():
    # Just print, no need for 'return'
    print("My Creater name is Abhigyan")

def WhileWorking():
    # Just print, no need for 'return'
    print("My Creater is Just a Student")


def celsius_to_fahrenheit():
    try:
        
        celsius = num.get()
        
        
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F") 
    except TclError:
        
        messagebox.showerror("Input Error", "Please enter a valid number.")

def square_number():
    try:
        
        value = num.get()
        
        print(f"Square of {value} is {value * value}")
    except TclError:
        messagebox.showerror("Input Error", "Please enter a valid number.,Only a Whole number")

root = Tk()
root.title("My Challange 2")
root.geometry("900x600")
root.minsize(630,100)

num = IntVar()

b1 = Button(root,fg="blue",text="Print name of creater",bg="red",command= name)
b1.grid(column=0,row=0, padx=5, pady=5) # Added some padding for better looks

b4 = Button(root,fg="blue",text="During creation of it profaction of creater",bg="red",command=WhileWorking)
b4.grid(column=1,row=0, padx=5, pady=5)

b3 = Button(root,fg="blue",text="print square of n number",bg="red",command=square_number)
b3.grid(column=2,row=0, padx=5, pady=5)

b2 = Button(root,fg="blue",text="Print celsius of n number into fahrenheit",bg="red",command=celsius_to_fahrenheit)
b2.grid(column=3,row=0, padx=5, pady=5)

usernumentry = Entry(root, textvariable=num) 
usernumentry.grid(row=1,column=0, pady=10)

root.mainloop()