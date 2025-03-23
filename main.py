import random
import time
import tkinter as tk
from tkinter import messagebox

def start_game():
    def check_guess():
        nonlocal lives, correct_number
        try:
            guess = int(entry.get())
            entry.delete(0, tk.END)
            if guess > correct_number:
                feedback_label.config(text="📈 Too High!", fg="red")
                lives -= 1
            elif guess < correct_number:
                feedback_label.config(text="📉 Too Low!", fg="blue")
                lives -= 1
            else:
                feedback_label.config(text="🎉 Congratulations! You Won!", fg="green")
                messagebox.showinfo("Game Over", "You won!")
                root.quit()
            
            lives_label.config(text=f"❤️ Lives Remaining: {lives}")
            if lives == 0:
                messagebox.showinfo("Game Over", f"You Lost! The correct number was {correct_number}")
                root.quit()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

    def reset_game():
        nonlocal lives, correct_number
        correct_number = random.randint(1, 100)
        lives = difficulty_levels[difficulty.get()]
        lives_label.config(text=f"❤️ Lives Remaining: {lives}")
        feedback_label.config(text="Guess a number between 1 and 100", fg="black")
        entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("🎯 Number Guessing Game")
    root.geometry("500x350")
    root.configure(bg="#f0f0f0")
    
    title_label = tk.Label(root, text="🔢 Welcome to the Number Guessing Game!", font=("Arial", 14, "bold"), bg="#f0f0f0")
    title_label.pack(pady=10)
    
    difficulty_levels = {"Easy": 10, "Medium": 7, "Hard": 5}
    difficulty = tk.StringVar(value="Easy")
    
    difficulty_frame = tk.Frame(root, bg="#f0f0f0")
    difficulty_frame.pack()
    tk.Label(difficulty_frame, text="Select Difficulty:", bg="#f0f0f0").pack(side=tk.LEFT)
    tk.OptionMenu(difficulty_frame, difficulty, *difficulty_levels.keys()).pack(side=tk.LEFT)
    
    tk.Button(root, text="🎮 Start Game", command=reset_game, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10).pack(pady=5)
    
    lives = difficulty_levels[difficulty.get()]
    correct_number = random.randint(1, 100)
    
    lives_label = tk.Label(root, text=f"❤️ Lives Remaining: {lives}", font=("Arial", 10, "bold"), bg="#f0f0f0")
    lives_label.pack(pady=5)
    
    feedback_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 10), bg="#f0f0f0")
    feedback_label.pack()
    
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    
    tk.Button(root, text="✅ Submit Guess", command=check_guess, bg="#008CBA", fg="white", font=("Arial", 10, "bold"), padx=10).pack(pady=5)
    
    tk.Button(root, text="🚪 Quit", command=root.quit, bg="#f44336", fg="white", font=("Arial", 10, "bold"), padx=10).pack(pady=5)
    
    root.mainloop()

start_game()
