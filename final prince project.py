import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

def number_guessing_game():
    def start_game():
        nonlocal target_number, attempts, guess_history
        difficulty = difficulty_var.get()
        if difficulty == "Easy":
            target_number = random.randint(1, 50)
        elif difficulty == "Medium":
            target_number = random.randint(1, 100)
        else:
            target_number = random.randint(1, 200)
        attempts = 0
        guess_history = []
        result_label.config(text="")
        entry.delete(0, tk.END)
        attempts_label.config(text="Attempts: 0")
        history_label.config(text="Previous guesses: ")
        submit_button.config(state="normal")
        entry.config(state="normal")

    def check_guess():
        try:
            guess = int(entry.get())
            nonlocal attempts
            attempts += 1
            guess_history.append(guess)
            attempts_label.config(text=f"Attempts: {attempts}")
            history_label.config(text="Previous guesses: " + ', '.join(map(str, guess_history)))
            if guess < target_number:
                result_label.config(text="Too low!", fg="blue")
            elif guess > target_number:
                result_label.config(text="Too high!", fg="orange")
            else:
                result_label.config(text="Correct!", fg="green")
                messagebox.showinfo("Congratulations!", f"You guessed the number in {attempts} attempts.")
                submit_button.config(state="disabled")
                entry.config(state="disabled")
        except ValueError:
            result_label.config(text="Invalid input. Please enter a number.", fg="red")

    # Initialize main window
    root = tk.Tk()
    root.title("🎯 Number Guessing Game")
    root.geometry("420x470")
    root.resizable(False, False)
    root.configure(bg="#f0f8ff")  # Light background

    # Fonts
    title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
    label_font = tkFont.Font(family="Arial", size=12)
    button_font = tkFont.Font(family="Verdana", size=10)

    # Game variables
    target_number = 0
    attempts = 0
    guess_history = []

    # Title (with wrapping)
    title = tk.Label(
        root,
        text="Welcome to the Number Guessing Game!",
        font=title_font,
        bg="#f0f8ff",
        wraplength=350,
        justify="center"
    )
    title.pack(pady=10)

    # Difficulty Frame
    difficulty_frame = tk.Frame(root, bg="#f0f8ff")
    difficulty_frame.pack(pady=10)

    tk.Label(difficulty_frame, text="Select Difficulty:", font=label_font, bg="#f0f8ff").pack(anchor="w")

    difficulty_var = tk.StringVar(value="Medium")
    for level in ["Easy", "Medium", "Hard"]:
        tk.Radiobutton(
            difficulty_frame,
            text=level,
            variable=difficulty_var,
            value=level,
            font=label_font,
            bg="#f0f8ff",
            anchor="w"
        ).pack(anchor="w")

    # Start Button
    start_button = tk.Button(
        root,
        text="Start Game",
        font=button_font,
        bg="#4CAF50",
        fg="white",
        command=start_game
    )
    start_button.pack(pady=10)

    # Guess Frame
    guess_frame = tk.Frame(root, bg="#f0f8ff")
    guess_frame.pack(pady=10)

    entry = tk.Entry(guess_frame, font=label_font, state="disabled", width=10, justify="center")
    entry.pack(pady=5)

    submit_button = tk.Button(
        guess_frame,
        text="Submit Guess",
        font=button_font,
        bg="#2196F3",
        fg="white",
        state="disabled",
        command=check_guess
    )
    submit_button.pack()

    # Result & Info
    result_label = tk.Label(root, text="", font=label_font, bg="#f0f8ff")
    result_label.pack(pady=5)

    attempts_label = tk.Label(root, text="Attempts: 0", font=label_font, bg="#f0f8ff")
    attempts_label.pack()

    history_label = tk.Label(
        root,
        text="Previous guesses: ",
        font=label_font,
        bg="#f0f8ff",
        wraplength=350,
        justify="left"
    )
    history_label.pack(pady=5)

    # Restart Button
    restart_button = tk.Button(
        root,
        text="Restart",
        font=button_font,
        bg="#FF9800",
        fg="white",
        command=start_game
    )
    restart_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    number_guessing_game()
