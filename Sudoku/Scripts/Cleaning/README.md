# Folder Cleaner

Automate your workspace organization with **Folder Cleaner**. If you have a cluttered directory with mixed file types and do not have time to sort them manually, this script automatically categorizes and moves your files into dedicated folders based on their extensions.

---

## Features

Scans target directories and automatically sorts files into six categories:

* **Documents**: Text files, office documents, spreadsheets, presentations, and markup (`.pdf`, `.docx`, `.xlsx`, `.pptx`, `.txt`, `.md`, `.csv`, etc.)
* **Photos**: Images, vector graphics, RAW files, and design formats (`.jpg`, `.png`, `.gif`, `.svg`, `.webp`, `.psd`, etc.)
* **Videos**: Video files and animations (`.mp4`, `.mkv`, `.avi`, `.mov`, `.webm`, etc.)
* **Musics**: Audio files, tracks, and voice recordings (`.mp3`, `.wav`, `.flac`, `.aac`, `.m4a`, etc.)
* **System_Files**: Executables, installers, disk images, archives, and logs (`.exe`, `.zip`, `.rar`, `.iso`, `.bat`, `.sh`, `.log`, etc.)
* **Unknown**: Any file extension not categorized above.

---

## Usage

### Windows
Open Command Prompt or PowerShell and run:

```cmd
python cleaning_folder.py --path "C:\path\to\your\folder"
```

### macOS
Open Terminal and run:

```bash
python3 cleaning_folder.py --path "/path/to/your/folder"
```

### Linux
Open Terminal and run:

```bash
python3 cleaning_folder.py --path "/path/to/your/folder"
```

---

## Display Help Menu

To view argument options directly from the command line:

**Windows:**
```cmd
python cleaning_folder.py -h
```

**macOS / Linux:**
```bash
python3 cleaning_folder.py -h
```
