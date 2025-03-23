# 🎯 Number Guessing Game

## 📌 Overview

This is a fun and interactive Number Guessing Game built using Python and Tkinter. The game challenges players to guess a randomly generated number between 1 and 100. Players can select their difficulty level, which determines the number of lives they have.

## 🚀 Features

- 🔢 Random number generation between 1 and 100.

- 🎚️ Three difficulty levels: Easy (10 lives), Medium (7 lives), Hard (5 lives).

- 🎮 Interactive Tkinter-based GUI.

- ✅ User input validation to prevent errors.

- 📉 Feedback on guesses (Too High or Too Low).

- 🎉 Victory and defeat messages.

- 🔄 Reset option to start a new game.

- 🚪 Quit button to exit the game anytime.

## 🛠️ How to Run

### Prerequisites

Ensure you have Python installed (Python 3.x recommended). Tkinter is included by default in standard Python installations.

Steps to Run

Clone the repository:

git clone https://github.com/msinghsandhu/Number-Guessing-Game
cd number-guessing-game

## Run the script:

python main.py


## 📝 Code Explanation

GUI Layout: Uses Tkinter for buttons, labels, and input fields.

Game Logic:

The program generates a random number.

Players input their guess and receive feedback.

Lives decrease with incorrect guesses.

Players win by guessing correctly or lose when lives reach zero.

Error Handling: Prevents non-numeric inputs.

## 📌 Future Enhancements

- ⏳ Implement a countdown timer for added challenge.

- 🔊 Add sound effects for correct and incorrect guesses.

- 📊 Track and display player stats (e.g., best score, number of attempts).
