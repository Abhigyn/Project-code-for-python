from tkinter import *

def click(event):
    global scvar
    text = event.widget.cget("text")
    current_text = scvar.get()
    
    if text == "=":
        if current_text:
            try:
                # Using str() to handle both integers and floats
                value = str(eval(current_text))
                scvar.set(value)
            except Exception as e:
                scvar.set("ERROR")
    elif text == "C":
        scvar.set("")
    else:
        # Prevent starting with an operator or multiple operators together
        if text in "+-*/" and (not current_text or current_text[-1] in "+-*/"):
            return
        scvar.set(current_text + text)
    
    Screen.update()
    # Move view to the end of the entry text
    Screen.xview_moveto(1)

def on_mousewheel(event):
    if root.tk.call('tk', 'windowingsystem') == 'win32':
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    elif root.tk.call('tk', 'windowingsystem') == 'aqua':
        canvas.yview_scroll(int(-1*event.delta), "units")
    else:
        canvas.yview_scroll(int(-1*event.delta), "units")

# --- START: NEW KEYBOARD FUNCTION ---
def on_keypress(event):
    key = event.char
    # Map common keyboard keys to calculator buttons
    if key in '0123456789.+-*/':
        # Simulate a button click
        click_event = type('obj', (object,), {'widget': type('obj', (object,), {'cget': lambda x: key})})
        click(click_event)
    elif key == '\r':  # The Enter key
        click_event = type('obj', (object,), {'widget': type('obj', (object,), {'cget': lambda x: '='})})
        click(click_event)
    elif key == '\x08':  # The Backspace key
        current_text = scvar.get()
        scvar.set(current_text[:-1])
# --- END: NEW KEYBOARD FUNCTION ---

root = Tk()
root.geometry("500x400")
root.title("Calculator")
root.wm_iconbitmap(r"I:\Study\Golu lession\Python      Projects\images\Calculator.ico")

# --- START: CENTERING THE WINDOW ---
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_width()
window_height = root.winfo_height()
x_pos = int((screen_width - window_width) / 2)
y_pos = int((screen_height - window_height) / 2)
root.geometry(f"+{x_pos}+{y_pos}")
# --- END: CENTERING THE WINDOW ---

scvar = StringVar()
scvar.set("")

# --- TOP DISPLAY AREA (UNSCROLLED) ---
top_frame = Frame(root)
top_frame.pack(fill=X, padx=10, pady=5)

Screen = Entry(top_frame, textvariable=scvar, font="lucida 40 bold")
h_scrollbar = Scrollbar(top_frame, orient=HORIZONTAL, command=Screen.xview)
Screen.config(xscrollcommand=h_scrollbar.set)

Screen.pack(fill=X, ipady=8)
h_scrollbar.pack(fill=X)

# --- START: VERTICAL SCROLL AREA FOR BUTTONS ---
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

v_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
v_scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=v_scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.bind_all("<MouseWheel>", on_mousewheel)

button_frame = Frame(canvas)
canvas.create_window((0, 0), window=button_frame, anchor="nw")

# --- END: VERTICAL SCROLL AREA SETUP ---

# --- START: BIND KEYPRESS EVENT ---
root.bind("<KeyPress>", on_keypress)
# --- END: BIND KEYPRESS EVENT ---

# Note: All button frames are now placed inside 'button_frame' instead of 'root'
f = Frame(button_frame, bg="grey")
b = Button(f, text="9", padx=20, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=20, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=20, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=20, font="lucida 35 bold")
b.pack(side=LEFT, padx=5, pady=5,)
b.bind("<Button-1>", click)
f.pack()

f = Frame(button_frame, bg="grey")
b = Button(f, text="6", padx=20, font="lucida 37 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=20, font="lucida 37 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=20, font="lucida 37 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=22, font="lucida 37 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(button_frame, bg="grey")
b = Button(f, text="3", padx=20, font="lucida 37 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=20, font="lucida 37 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=20, font="lucida 37 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=23, font="lucida 37 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(button_frame, bg="grey")
b = Button(f, text="=", padx=22, font="lucida 33 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=20, font="lucida 33 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=20, font="lucida 33 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=30, font="lucida 33 bold")
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()