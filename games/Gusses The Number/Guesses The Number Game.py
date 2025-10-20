import tkinter as tk
from tkinter import messagebox
import random
import os
import sys

# Function to get the correct path for resource files in a PyInstaller bundle
def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller.
    PyInstaller creates a temporary folder and stores path in _MEIPASS
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # For development/regular execution
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Guess The Number Game")
        
        # --- Game State Variables ---
        self.HI_SCORE_FILE = "Hi-score.txt"
        self.secret_number = 0
        self.guesses = 0
        # Load hi-score immediately upon starting
        self.hi_score = self.load_hi_score()
        
        # --- Tkinter Variables ---
        self.feedback_text = tk.StringVar()
        self.score_text = tk.StringVar()
        
        # --- Setup GUI Layout ---
        self.setup_ui()
        self.bind_keyboard_events()
        
        # --- Start the first game ---
        self.start_new_game()

    def setup_ui(self):
        # 1. Title Label - Added fill='x' to allow horizontal stretching
        title_label = tk.Label(self.master, text="Guess The Number (1-100)", font=("Arial", 16, "bold"))
        title_label.pack(pady=5, fill='x')

        # 2. Input Field - Added fill='x' and padx for margin when stretching
        self.guess_entry = tk.Entry(self.master, font=("Arial", 14), justify='center', state=tk.NORMAL)
        self.guess_entry.pack(pady=5, padx=40, fill='x')
        self.guess_entry.focus_set() 
        
        # Bind ALL physical key presses to our custom handler
        self.guess_entry.bind('<Key>', self._handle_keypress_event)
        
        # 3. Keypad Frame
        keypad_frame = tk.Frame(self.master)
        keypad_frame.pack(pady=10)
        
        # Define the layout of the keypad buttons
        keypad_layout = [
            ('7', '8', '9'),
            ('4', '5', '6'),
            ('1', '2', '3'),
            ('Clear', '0', 'Enter')
        ]
        
        # Create and place the keypad buttons using grid
        for r, row in enumerate(keypad_layout):
            for c, key in enumerate(row):
                if key == 'Enter':
                    # Enter button calls check_guess directly
                    button = tk.Button(keypad_frame, text=key, width=8, height=2, font=("Arial", 12), command=self.check_guess, bg="#90EE90")
                elif key == 'Clear':
                    # Clear button calls keypad_press with 'Clear'
                    button = tk.Button(keypad_frame, text=key, width=8, height=2, font=("Arial", 12), command=lambda k=key: self.keypad_press(k), bg="#F08080")
                else: # Numeric buttons (0-9)
                    # Numeric buttons call keypad_press with the digit
                    button = tk.Button(keypad_frame, text=key, width=8, height=2, font=("Arial", 12), command=lambda k=key: self.keypad_press(k))
                
                button.grid(row=r, column=c, padx=5, pady=5)
                
        # 4. Feedback Label - Added fill='x'
        self.feedback_label = tk.Label(self.master, textvariable=self.feedback_text, font=("Arial", 12))
        self.feedback_label.pack(pady=5, fill='x')
        
        # 5. Score and Hi-Score Label - Added fill='x'
        self.score_label = tk.Label(self.master, textvariable=self.score_text, font=("Arial", 10))
        self.score_label.pack(pady=5, fill='x')

        # 6. New Game Button
        new_game_button = tk.Button(self.master, text="Start New Game", command=self.start_new_game)
        new_game_button.pack(pady=10)

        self.update_score_display()

    def bind_keyboard_events(self):
        """Binds global physical keyboard keys as a fallback."""
        # Bind Return to the master window as a backup to submit the guess
        self.master.bind('<Return>', lambda event: self.check_guess())
        
        # The specific bindings for 0-9 and Backspace are handled by 
        # _handle_keypress_event on the Entry widget for superior control.

    def _handle_keypress_event(self, event):
        """
        Custom handler for physical keyboard presses on the Entry widget.
        We return 'break' for keys we handle to stop Tkinter's default action.
        """
        key = event.keysym
        
        # 1. Handle Digits (0-9)
        if key.isdigit():
            # Manually insert the digit if the input length is acceptable
            self.keypad_press(key)
            return 'break' # Stop default text insertion

        # 2. Handle Enter (Return)
        if key == 'Return':
            self.check_guess()
            return 'break' # Stop default action

        # 3. Handle Backspace (Clear last digit)
        if key == 'BackSpace':
            self.delete_last_digit()
            return 'break' # Stop default deletion

        # 4. Allow other keys (like Tab, Shift) to pass
        return None 

    def delete_last_digit(self):
        """Deletes the last character in the entry field, simulating backspace."""
        if self.guess_entry['state'] == tk.NORMAL:
            current_text = self.guess_entry.get()
            # Delete from the second-to-last character (index -1) to the end (tk.END)
            self.guess_entry.delete(len(current_text) - 1, tk.END)

    def keypad_press(self, key):
        """Handles clicks on the 0-9 and Clear buttons, and physical keyboard numeric input."""
        
        # Only allow input if the game is active
        if self.guess_entry['state'] == tk.NORMAL:
            if key.isdigit():
                # Check for max length (3 digits for max 100)
                if len(self.guess_entry.get()) < 3:
                    self.guess_entry.insert(tk.END, key)
            elif key == 'Clear':
                self.guess_entry.delete(0, tk.END)

    def start_new_game(self):
        """Initializes a new round of the game."""
        self.secret_number = random.randint(1, 100)
        self.guesses = 0
        self.feedback_text.set("Guess a number between 1 and 100.")
        self.guess_entry.delete(0, tk.END) 
        self.guess_entry.config(state=tk.NORMAL) # Enable the Entry field
        self.guess_entry.focus_set() # Ensure keyboard focus is on the input field
        self.update_score_display()

    def check_guess(self):
        """Processes the user's guess when the Enter button is clicked or Enter key is pressed."""
        current_guess_str = self.guess_entry.get()
        
        # Only process guess if a game is active
        if self.guess_entry['state'] != tk.NORMAL:
            return

        if not current_guess_str:
            self.feedback_text.set("Please enter a number.")
            return

        try:
            guess = int(current_guess_str)
            self.guess_entry.delete(0, tk.END) # Clear the field after reading
        except ValueError:
            self.feedback_text.set("Error: Must be a whole number.")
            return

        if not (1 <= guess <= 100):
            self.feedback_text.set("Number must be between 1 and 100.")
            return

        self.guesses += 1

        if guess > self.secret_number:
            self.feedback_text.set("Too High! Try a lower number.")
        elif guess < self.secret_number:
            self.feedback_text.set("Too Low! Try a higher number.")
        else:
            self.end_game()
        
        self.update_score_display()

    def end_game(self):
        """Handles the end of the game when the number is guessed."""
        self.feedback_text.set(f"YOU GOT IT! The number was {self.secret_number}!")
        self.guess_entry.config(state=tk.DISABLED) # Disable the input after the game ends
        
        # Check and update hi-score
        if self.hi_score == float('inf') or self.guesses < self.hi_score:
            messagebox.showinfo("New Hi-score!", 
                                 f"New Hi-score: {self.guesses} attempts! Congratulations!")
            self.hi_score = self.guesses
            self.save_hi_score()
        else:
            messagebox.showinfo("Game Over", 
                                 f"You guessed it in {self.guesses} attempts.")
        
        self.update_score_display()

    def update_score_display(self):
        """Updates the score text label."""
        self.score_text.set(f"Current Guesses: {self.guesses} | HI-SCORE: {self.hi_score if self.hi_score != float('inf') else 'N/A'}")

    # --- Hi-Score File Management ---

    def load_hi_score(self):
        """Loads the hi-score from the file using the PyInstaller-compatible path."""
        # Use resource_path for file access, ensuring it works inside the bundled exe
        file_path = resource_path(self.HI_SCORE_FILE) 
        
        try:
            # We assume the file might be created by the user in the working directory 
            # if running outside the bundle, or simply present in the same directory 
            # as the final executable.
            with open(file_path, "r") as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError, IsADirectoryError):
            # If no score exists, set a high value so any score beats it
            return float('inf') 

    def save_hi_score(self):
        """Saves the current hi-score to the file using the PyInstaller-compatible path."""
        # Use resource_path for file access
        file_path = resource_path(self.HI_SCORE_FILE)
        
        try:
            # We only save if hi_score is not the default infinity value
            if self.hi_score != float('inf'):
                # Using 'w' will create the file if it doesn't exist, which is what we want.
                with open(file_path, "w") as file:
                    file.write(str(self.hi_score))
        except Exception as e:
            # If the PyInstaller temp folder is read-only, this might fail, 
            # so we print an error but let the program continue.
            print(f"Error saving hi-score: {e}")


# --- Main Application Loop ---
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x550")
    root.resizable(True, True) 
    
    game_gui = GuessingGameGUI(root)
    
    root.mainloop()
