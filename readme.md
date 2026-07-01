# 📂 File Organizer

A Python command-line application that automatically organizes files into categorized folders based on their file extensions.

## ✨ Features

- Organize an existing folder
- Create a new folder for organization
- Automatically categorize files
- Supports common file types:
  - Images
  - Documents
  - Spreadsheets
  - Presentations
  - Music
  - Videos
  - Archives
  - Python Files
  - Source Code
  - Executables
- Unknown file types are moved to an **Others** folder.
- User-friendly command-line interface.
- Input validation and error handling.

---

## 📁 Supported Categories

| Category | Extensions |
|----------|------------|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.svg`, `.ico` |
| Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.md`, `.rtf`, `.odt` |
| Spreadsheets | `.xls`, `.xlsx`, `.csv`, `.ods` |
| Presentations | `.ppt`, `.pptx`, `.odp` |
| Music | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Python | `.py`, `.pyw` |
| Code | `.cpp`, `.c`, `.java`, `.js`, `.ts`, `.html`, `.css`, `.php`, `.go`, `.rs`, `.swift`, `.kt` |
| Executables | `.exe`, `.msi`, `.bat`, `.cmd` |
| Others | Any unsupported file type |

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/Abhay-Git-07/File-Organizer.git
```

Navigate into the project folder:

```bash
cd File-Organizer
```

Run the program:

```bash
python file_organizer.py
```

*(Use `python3` instead if required on your operating system.)*

---

## 📖 How to Use

When the program starts, choose one of the following options:

1. Organize an existing folder
2. Create a new folder and organize it
3. Exit

The program will automatically:

- Detect file types
- Create category folders
- Move files into their appropriate folders
- Display the folders that were created

---

## 🛠️ Concepts Practiced

- Functions
- Dictionaries
- Lists
- Loops
- Conditional Statements
- Exception Handling
- File & Directory Management (`os`)
- File Operations (`shutil`)
- Modular Programming

---

## 📌 Future Improvements

- Handle duplicate filenames
- Allow users to customize categories
- Use `pathlib` for cleaner path handling
- Add logging
- Build a graphical user interface (GUI)

---

## 👨‍💻 Author

**Abhay Chauhan**

Built as part of my Python learning journey and project roadmap.

## 🤝 Feedback

I'm still learning, so any suggestions or feedback are always welcome. If you have ideas to improve this project, feel free to open an issue or submit a pull request.

---

⭐ If you found this project helpful, consider giving it a star!
