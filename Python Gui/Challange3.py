from tkinter import *
import os

# --- Functions ---
def Print():
    filepath = "../docs/DanceEntry.txt"
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            data = f.read()
        if data.strip() == "":
            print("No participants found yet.")
        else:
            print("\n--- Participant List ---")
            print(data)
            print("------------------------")
    else:
        print("No entry file found yet!")


def store():
    filepath = "../docs/DanceEntry.txt"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "a") as f:
        f.write(f"Name: {stringVar.get()}, Age: {intVar.get()}, D.O.B: {dobVar.get()}\n")

    # --- clear fields after save ---
    stringVar.set("")
    intVar.set(0)
    dobVar.set("")

    print("✅ Participant entry saved successfully!")


# --- GUI ---
root = Tk()
root.geometry("600x200")
root.title("Dancer Entry Form")

# Labels
Label(root, text="Name").grid(row=0, column=0)
Label(root, text="Age").grid(row=1, column=0)
Label(root, text="D.O.B").grid(row=2, column=0)

# Variables
stringVar = StringVar()
intVar = IntVar()
dobVar = StringVar()

# Entries
NameEntry = Entry(root, textvariable=stringVar)
AgeEntry = Entry(root, textvariable=intVar)
Date_of_Birth_Entry = Entry(root, textvariable=dobVar)

NameEntry.grid(row=0, column=1,)
AgeEntry.grid(row=1, column=1,)
Date_of_Birth_Entry.grid(row=2, column=1,)

# Buttons
Button(root, text="Save Entry", command=store).grid(row=3, column=0,)
Button(root, text="Print Participants", command=Print).grid(row=3, column=1 )

root.mainloop()
