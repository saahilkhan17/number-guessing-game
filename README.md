# 🎮 Number Guessing Game (Python CLI)

A simple **command-line number guessing game** written in Python.
The program randomly selects a number between **1 and 100**, and the player must guess it within a limited number of attempts.

This project is a beginner-friendly Python project demonstrating **loops, conditionals, input validation, and random number generation**.

---

## 🚀 Features

* 🎯 Random number generation between **1–100**
* 🎚 **Difficulty levels**

  * Easy → 10 guesses
  * Medium → 7 guesses
  * Hard → 5 guesses
  * Custom → User chooses number of guesses
* 🔁 **Replay option** after each game
* ⚠ **Input validation** to prevent crashes
* ❌ Quit anytime by typing **Q**



## 🧠 Concepts Used

This project uses basic Python concepts:

* `while` loops
* `if-elif-else` conditions
* `random` module
* string methods (`.lower()`, `.upper()`)
* input validation (`isdigit()`)

---

## 📦 Requirements

* Python **3.x**

No external libraries are required.

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/yourusername/number-guessing-game.git
```

2. Navigate to the project folder

```bash
cd number-guessing-game
```

3. Run the program

```bash
python number-guessing-game.py
```

---

## 🎮 Example Gameplay

```
🎮 Welcome to the Number Guessing Game

Choose difficulty (easy / medium / hard / custom): medium

I have selected a number between 1 and 100

Guess the number (Guesses left: 7): 50
📉 Too big! Try a smaller number

Guess the number (Guesses left: 6): 25
📈 Too small! Try a bigger number
```

---

## 📁 Project Structure

```
number-guessing-game
│
├── RandomGussesing.py
└── README.md
```

---

## 🌟 Future Improvements

Possible upgrades for this project:

* 🏆 Score system
* ⏱ Timer mode
* 🎨 Colored terminal output
* 🖥 GUI version using **Tkinter**
* 💾 Save high scores

---

## 🤝 Contributing

Pull requests are welcome.
If you find a bug or want to improve the game, feel free to open an issue.

---

## 📜 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Created by **Saahil Khan Mehar**

Learning Python and building beginner projects for GitHub.
