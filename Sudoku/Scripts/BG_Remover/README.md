#  Python AI Background Remover

A simple, lightweight Command Line Interface (CLI) tool to instantly remove image backgrounds using artificial intelligence. This script leverages the power of `rembg` and `Pillow` to isolate foregrounds and output transparent PNG images.

---

##  Features

* **AI-Powered**: Uses trained U-2-Net models to accurately detect backgrounds.
* **Smart Defaults**: Saves files to your current script directory automatically if no output path is provided.
* **Flexible CLI**: Pass custom target files and output destinations directly from your terminal.

---

##  Prerequisites & Installation

Make sure you have Python 3 installed. Follow the setup steps below for your operating system.

### 1. Install Dependencies
Open your terminal or command prompt and run the setup command for your OS:

####  Linux (Ubuntu/Debian)
```bash
python3 -m venv venv
source venv/bin/activate
pip install rembg pillow
```

####  macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install rembg pillow
```

####  Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install rembg pillow
```

> **Note for First-Time Users:** The very first time you run this script, it will take a minute to start because it automatically downloads its AI model (~170MB). Subsequent runs will happen instantly.

---

##  Mini Tutorial (How to Run)

Navigate to your script folder inside your terminal and run the commands using the syntax appropriate for your platform.

###  Option 1: Basic Usage (Saves to current folder)
Omitting the `saveto` parameter automatically saves a file named `result.png` right inside the folder where the script lives.

* **Linux:**
  ```bash
  python3 bgRemover.py target=/path/to/your/image.jpg
  ```
* **macOS:**
  ```bash
  python3 bgRemover.py target=/path/to/your/image.jpg
  ```
* **Windows:**
  ```powershell
  python bgRemover.py target=C:\path\to\your\image.jpg
  ```

### 🎛️ Option 2: Custom Output Path
Specify exactly where the output should be saved. Always use a `.png` extension to preserve the transparent background.

* **Linux:**
  ```bash
  python3 bgRemover.py target=/path/to/your/image.jpg saveto=/path/to/save/result.png
  ```
* **macOS:**
  ```bash
  python3 bgRemover.py target=/path/to/your/image.jpg saveto=/path/to/save/result.png
  ```
* **Windows:**
  ```powershell
  python bgRemover.py target=C:\path\to\your\image.jpg saveto=C:\path\to\save\result.png
  ```

---

##  Argument Reference

| Argument | Description | Required? | Default Value |
| :--- | :--- | :--- | :--- |
| `target=` | Absolute or relative path to your source image. | **Yes** | *None* |
| `saveto=` | Target destination path and file name for the output. | No | `result.png` (In script directory) |

---

##  License
This project is open-source and free to use.