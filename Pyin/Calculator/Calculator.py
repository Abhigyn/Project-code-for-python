from tkinter import *
import re
import sys, os



def click(event):
    global scvar
    text = event.widget.cget("text")
    current_text = scvar.get()
    
    if text == "=":
        if current_text:
            try:
                expression = current_text

                # Handle percentage like real calculators
                if "%" in expression:
                    # Case: number + percent / number - percent
                    match = re.match(r"(\d+(\.\d+)?)([+\-])(\d+(\.\d+)?)%", expression)
                    if match:
                        base = float(match.group(1))
                        op = match.group(3)
                        perc = float(match.group(4))
                        value = base + perc*base/100 if op == "+" else base - perc*base/100
                        scvar.set(str(value))
                        return
                    
                    # Case: number * percent / number / percent
                    match = re.match(r"(\d+(\.\d+)?)([*/])(\d+(\.\d+)?)%", expression)
                    if match:
                        base = float(match.group(1))
                        op = match.group(3)
                        perc = float(match.group(4))/100
                        value = base * perc if op == "*" else base / perc
                        scvar.set(str(value))
                        return
                    
                    # Fallback: just replace % with /100
                    expression = expression.replace("%", "/100")
            
                value = str(eval(expression))
                scvar.set(value)
            except Exception as e:
                scvar.set("ERROR")
    elif text == "C":
        scvar.set("")
    else:
        if text in "+-*/%" and (not current_text or current_text[-1] in "+-*/"):
            return
        scvar.set(current_text + text)
    
    Screen.update()
    Screen.xview_moveto(1)

def on_mousewheel(event):
    if root.tk.call('tk', 'windowingsystem') == 'win32':
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    elif root.tk.call('tk', 'windowingsystem') == 'aqua':
        canvas.yview_scroll(int(-1*event.delta), "units")
    else:
        canvas.yview_scroll(int(-1*event.delta), "units")

def on_keypress(event):
    key = event.char
    if key in '0123456789.+-*/%':
        click_event = type('obj', (object,), {'widget': type('obj', (object,), {'cget': lambda x: key})})
        click(click_event)
    elif key == '\r':
        click_event = type('obj', (object,), {'widget': type('obj', (object,), {'cget': lambda x: '='})})
        click(click_event)
    elif key == '\x08':
        current_text = scvar.get()
        scvar.set(current_text[:-1])

root = Tk()
root.geometry("500x400")
root.title("Calculator")

if getattr(sys, 'frozen', False):  
    # Running as exe
    icon_path = os.path.join(sys._MEIPASS, "Calculator.ico")
else:  
    # Running as .py script
    icon_path = "Calculator.ico"

try:
    root.iconbitmap(icon_path)
except:
    pass  # fallback if something goes wrong

scvar = StringVar()
scvar.set("")

top_frame = Frame(root)
top_frame.pack(fill=X, padx=10, pady=5)

Screen = Entry(top_frame, textvariable=scvar, font="lucida 40 bold")
h_scrollbar = Scrollbar(top_frame, orient=HORIZONTAL, command=Screen.xview)
Screen.config(xscrollcommand=h_scrollbar.set)

Screen.pack(fill=X, ipady=8)
h_scrollbar.pack(fill=X)

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

v_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
v_scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=v_scrollbar.set)
canvas.bind_all("<MouseWheel>", on_mousewheel)

button_frame = Frame(canvas)

def update_canvas(e):
    canvas.itemconfig(frame_window, width=canvas.winfo_width())
    canvas.coords(frame_window, canvas.winfo_width()/2, 0)

frame_window = canvas.create_window((canvas.winfo_width()/2, 0), window=button_frame, anchor="n")
canvas.bind("<Configure>", update_canvas)

root.bind("<KeyPress>", on_keypress)

def add_row(buttons, font_size=35):
    f = Frame(button_frame, bg="grey")
    for txt in buttons:
        b = Button(f, text=txt, padx=20, font=f"lucida {font_size} bold")
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)
    f.pack(anchor="center")

add_row(["C", "%", "=", "%"], font_size=33)
add_row(["9", "8", "7", "+"], font_size=37)
add_row(["6", "5", "4", "-"], font_size=38)
add_row(["3", "2", "1", "/"], font_size=38)
add_row(["0", "00", ".","*"], font_size=35)

root.mainloop()
