from tkinter import *

root = Tk()


canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
# --- Functions ---
def resize_gui():
    """
    Gets the values from the entry boxes and resizes the window.
    """
    try:
        new_width = width_value.get()
        new_height = height_value.get()
        # Ensure the values are positive numbers before resizing
        if new_width > 0 and new_height > 0:
            root.geometry(f"{new_width}x{new_height}")
        else:
            print("Width and height must be positive numbers.")
    except TclError:
        print("Please enter valid numbers for width and height.")


window_width = canvas_width
window_height = canvas_height


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

width_value = IntVar(value=window_width)
height_value = IntVar(value=window_height)


width_label = Label(root, text="GUI's Width:")
width_label.grid(row=0, column=0, padx=20, pady=15, sticky="w")

width_entry = Entry(root, textvariable=width_value, width=10)
width_entry.grid(row=0, column=1, padx=20, pady=15)


height_label = Label(root, text="GUI's Height:")
height_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

height_entry = Entry(root, textvariable=height_value, width=10)
height_entry.grid(row=1, column=1, padx=20, pady=10)


resize_button = Button(root, text="Apply New Size", command=resize_gui)

resize_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop