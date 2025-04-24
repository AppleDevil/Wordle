import tkinter as tk
import random
from tkinter import messagebox

# Sample word list, replace this with WordsAPI later
WORDS = ["apple", "grape", "melon", "peach", "mango", "lemon"]
TARGET_WORD = random.choice(WORDS).upper()

# GUI setup
root = tk.Tk()
root.title("Wordle Game")
root.geometry("600x700")
root.config(bg="#2E2E2E")  # Dark background for a modern, sleek look

# Fonts and colours
FONT = ('Helvetica', 20, 'bold')
BUTTON_FONT = ('Helvetica', 16, 'bold')
BACKGROUND_COLOR = "#3E3E3E"
HIGHLIGHT_COLOR = "#F1C40F"
BUTTON_COLOR = "#4CAF50"
TEXT_COLOR = "#F4F4F9"
ERROR_COLOR = "#E74C3C"
TILE_COLOR = "#333333"
TILE_TEXT_COLOR = "#FFFFFF"
TILE_BORDER_COLOR = "#7F8C8D"

# 6 rows, 5 columns for Wordle grid
tiles = [[tk.Label(root, text=" ", width=5, height=2, font=FONT, fg=TILE_TEXT_COLOR, bg=TILE_COLOR, relief="solid", bd=3) for _ in range(5)] for _ in range(6)]
for r in range(6):
    for c in range(5):
        tiles[r][c].grid(row=r, column=c, padx=8, pady=8)

# Row tracker
current_row = 0

# Function to set tile colours
def colour_tiles(guess, row):
    for i in range(5):
        letter = guess[i]
        label = tiles[row][i]
        label.config(text=letter)
        if letter == TARGET_WORD[i]:
            label.config(bg="#27AE60")  # Green for correct letter in correct position
        elif letter in TARGET_WORD:
            label.config(bg="#F39C12")  # Yellow for correct letter in wrong position
        else:
            label.config(bg="#BDC3C7")  # Light grey for incorrect letter

# Submit guess function
def submit_guess():
    global current_row
    guess = entry.get().upper()

    if len(guess) != 5:
        result_label.config(text="Enter a 5-letter word!", fg=ERROR_COLOR)
        return

    colour_tiles(guess, current_row)
    if guess == TARGET_WORD:
        result_label.config(text="You got it!", fg=BUTTON_COLOR)
        submit_button.config(state="disabled")
    else:
        current_row += 1
        if current_row == 6:
            result_label.config(text=f"Game over! Word was {TARGET_WORD}", fg=ERROR_COLOR)
            submit_button.config(state="disabled")
    entry.delete(0, tk.END)

# Create entry box for guesses
entry = tk.Entry(root, font=('Helvetica', 24), justify='center', bd=3, relief='solid', width=12, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
entry.grid(row=7, column=0, columnspan=5, pady=15)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_guess, font=BUTTON_FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR, relief="solid", bd=3)
submit_button.grid(row=8, column=0, columnspan=5, pady=10)

# Result label
result_label = tk.Label(root, text="", font=('Helvetica', 16), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
result_label.grid(row=9, column=0, columnspan=5, pady=10)

# Start the app
root.mainloop()
