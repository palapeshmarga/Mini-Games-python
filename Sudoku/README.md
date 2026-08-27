# 🧩 Flet Sudoku Game

A modern, responsive, full-featured Sudoku application built with Python and [Flet](https://flet.dev/). Features dynamic grid highlighting, note-taking mode, conflict detection, difficulty selection, and a live timer.

---

## ✨ Features

* **3 Difficulty Levels:** Choose between Easy, Normal, and Hard mode upon starting.
* **Responsive Layout:** Designed to scale and center dynamically across Web, Desktop (Windows, macOS, Linux), and Mobile screens.
* **Live Game Timer & Pause System:** Track your completion speed with a built-in timer and an interactive pause/resume/restart menu.
* **Interactive Notes Mode:** Toggle note-taking to mark potential candidates in empty cells with real-time error tracking.
* **Smart Conflict Detection:** Highlights invalid placements across rows, columns, and 3x3 blocks in real time.
* **Automatic Solver & Generator:** Generates playable boards on the fly using randomized backtracking algorithms.

---

## 🛠️ Requirements & Installation

Make sure you have Python 3.8+ and Flet installed:

```bash
pip install flet --upgrade
```

# 🧩 Flet Sudoku Game

A modern, responsive, full-featured Sudoku application built with Python and [Flet](https://flet.dev/). Features dynamic grid highlighting, note-taking mode, conflict detection, difficulty selection, and a live timer.

---

## ✨ Features

* **3 Difficulty Levels:** Choose between Easy, Normal, and Hard mode upon starting.
* **Responsive Layout:** Designed to scale and center dynamically across Web, Desktop (Windows, macOS, Linux), and Mobile screens.
* **Live Game Timer & Pause System:** Track your completion speed with a built-in timer and an interactive pause/resume/restart menu.
* **Interactive Notes Mode:** Toggle note-taking to mark potential candidates in empty cells with real-time error tracking.
* **Smart Conflict Detection:** Highlights invalid placements across rows, columns, and 3x3 blocks in real time.
* **Automatic Solver & Generator:** Generates playable boards on the fly using randomized backtracking algorithms.

---

## 🛠️ Requirements & Installation

Make sure you have Python 3.8+ and Flet installed:

```bash
pip install flet --upgrade
```

## 🚀 Running the App

1. Clone or download this repository.

2. Ensure both main.py and Tests.py are located in the same directory.

3. Run the application:

```bash
python main.py
```

## 📁 Project Structure

Plaintext

├── main.py          # Flet GUI application, layout components, and game loop  
└── Tests.py         # Sudoku puzzle generation, backtracking solver, and difficulty logic


## 🎮 How to Play

1. Select your desired difficulty (Easy, Normal, or Hard) and click Start.

2. Click on any cell on the grid to select it.

3. Use the keypad below the board to enter numbers or erase values using the backspace button.

4. Toggle the Edit Note icon to add or remove candidate numbers within a cell.

5. Use the top Pause icon to pause the timer or restart the match at any time.