# TypeMaster - Speed & Accuracy Practice App 🚀

**TypeMaster** is a desktop application built in Python using the **Flet** framework. Designed to improve typing speed and precision, it features real-time feedback, custom practice files, adaptive leveling, and an automatic inactivity timer.

---

## ✨ Key Features

* **3-State Color Highlighting:**
  * 🟩 **Green:** Correctly typed character on the first attempt.
  * 🟥 **Red + Underline:** Incorrectly typed character.
  * 🟧 **Orange:** Character corrected using backspace after an initial error.
* **Level Progression System:** Earn points based on accurate key presses. Automatically level up as you reach variable target scores ($2\times \text{points}$ for basic targets, scaling $\times 1.7$ per level).
* **Inactivity Auto-Reset:** If typing pauses for 5 seconds during an active test, the app resets automatically and alerts the user.
* **Custom Practice Text:** Load custom text line-by-line from local level files (`easy.txt`, `normal.txt`, `hard.txt`).
* **Live WPM Counter:** Dynamic Words Per Minute tracking.

---

## 📋 Requirements & Prerequisites

* **Python:** Version `3.10` or higher
* **Operating System:** Linux / macOS / Windows

---

## 🛠️ Installation & Setup

### 1. Clone or Download the Project
Navigate to your target directory and open your terminal.

### 2. Set Up a Virtual Environment (Recommended)
Create and activate a virtual environment to isolate project dependencies:

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```
