# Python Mini-Games Collection

Welcome to the **Python Mini-Games Collection**! This repository contains a collection of simple, fun, and interactive command-line and GUI mini-games built using Python. It is designed for beginners learning Python, terminal-based entertainment, and practicing logic/typing skills.

## 🎮 Included Mini-Games

This repository contains the following games:

1. **Guess The Word**
   - **Location:** `Guess The Word/guess_the_word.py`
   - **Description:** A classic word-guessing game (similar to Hangman) where players attempt to uncover a hidden word letter-by-letter using words from `words.txt`.

2. **Guessing Number**
   - **Location:** `Guessing Number/main.py`
   - **Description:** A number-guessing game where the computer selects a random secret number, and the player receives hints ("too high" or "too low") to find it.

3. **Math Quiz**
   - **Location:** `Math Quiz/math_quiz.py`
   - **Description:** An interactive arithmetic quiz designed to test quick mental math skills with generated math problems.

4. **Sudoku**
   - **Location:** `Sudoku/src/main.py`
   - **Description:** A full-featured Sudoku application complete with visual assets, tests (`src/Tests.py`), and project configuration managed via `pyproject.toml`.

5. **Tik Tak To**
   - **Location:** `Tik Tak To/tiktakto.py`
   - **Description:** The timeless two-player Tic-Tac-Toe game playable right in your terminal interface.

6. **Typing Practice**
   - **Location:** `Typing Practice/app.py`
   - **Description:** A typing speed and accuracy trainer featuring multiple difficulty settings supported by customizable word files:
     - `easy.txt`
     - `normal.txt`
     - `hard.txt`

## 📂 Project Structure

```plaintext
Mini-Games-python/
│
├── Guess The Word/
│   ├── guess_the_word.py
│   └── words.txt
│
├── Guessing Number/
│   └── main.py
│
├── Math Quiz/
│   └── math_quiz.py
│
├── Sudoku/
│   ├── src/
│   │   ├── assets/         # Splash images and application icons
│   │   ├── main.py
│   │   └── Tests.py
│   ├── tests/
│   └── pyproject.toml
│
├── Tik Tak To/
│   └── tiktakto.py
│
└── Typing Practice/
    ├── app.py
    ├── easy.txt
    ├── normal.txt
    └── hard.txt
```

## 🚀 Getting Started

### Prerequisites

* **Python 3.8+** must be installed on your system. You can download Python from [python.org](https://www.python.org/).

### Installation

1. **Clone the repository** (or download and extract the ZIP file):
   ```bash
   git clone https://github.com/palapeshmarga/Mini-Games-python.git
   cd Mini-Games-python
   ```


2. **(Optional) Set up a Virtual Environment:**
    ```python
    python -m venv venv
    ```
    **On Windows:**
    ```bash
    venv\Scripts\activate
    ```
    **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

## 🎯 How to Play
Run any game directly with Python from the main repository directory:

- **Guess The Word:**
    ```bash
    python "Guess The Word/guess_the_word.py"
    ```

- **Guessing Number:**
    ```bash
    python "Guessing Number/main.py"
    ```

- **Math Quiz:**
    ```bash
    python "Math Quiz/math_quiz.py"
    ```
**and so on...**
---

## 🤝 Contributing
**Contributions are welcome! If you would like to add a new mini-game or improve existing ones:**

1. Fork this repository.

2. Create a feature branch (`git checkout -b feature/NewGame`).

3. Commit your changes (`git commit -m 'Add New Game'`).

4. Push to the branch (`git push origin feature/NewGame`).

5. Open a Pull Request.