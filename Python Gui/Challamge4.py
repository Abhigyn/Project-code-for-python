import tkinter as tk
from tkinter import messagebox as tmsg
import os # <-- Import the os module for directory operations
from datetime import datetime # <-- Import datetime to add a timestamp

# --- Main Application Window ---
root = tk.Tk()
root.title("Main Application")
root.geometry("400x300")

# --- Functions ---
def submit_rating():
    """Gets the rating, saves it to a file, and shows a confirmation."""
    # 1. Get the rating value from the slider
    rating_value = myslider.get()
    
    # 2. Define the file path and ensure the directory exists
    file_path = '../docs/Rating_App.txt'
    directory = os.path.dirname(file_path) # Gets the directory part: ../docs
    if not os.path.exists(directory):
        os.makedirs(directory) # Creates the directory if it doesn't exist

    # 3. Write the rating to the file
    try:
        # Use 'a' to append to the file; 'w' would overwrite it each time
        with open(file_path, 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - Rating: {rating_value}/10\n")
            
        # 4. Show confirmation message to the user
        tmsg.showinfo("Thanks!", f"You rated us {rating_value}/10. Your rating has been saved!")

    except Exception as e:
        # Show an error message if saving fails
        tmsg.showerror("Error", f"Failed to save rating: {e}")

    finally:
        # 5. Close the pop-up window
        rating_window.destroy()

def open_rating_window():
    """Creates a new pop-up window for rating."""
    global myslider, rating_window

    rating_window = tk.Toplevel(root)
    rating_window.title("Rate Us")
    rating_window.geometry("250x150")

    tk.Label(rating_window, text="Please rate us out of 10").pack(pady=10)

    myslider = tk.Scale(rating_window, from_=0, to=10, orient=tk.HORIZONTAL)
    myslider.set(7)
    myslider.pack()

    tk.Button(rating_window, text="Submit", command=submit_rating).pack(pady=10)

# --- Menu Bar Setup ---
main_menubar = tk.Menu(root)
m1 = tk.Menu(main_menubar, tearoff=0)
m1.add_command(label="Rate Project", command=open_rating_window)
m1.add_separator()
m1.add_command(label="Exit", command=root.quit)
main_menubar.add_cascade(label="File", menu=m1)
root.config(menu=main_menubar)

# --- Start the application ---
root.mainloop()