# 📝 Simple CLI Note-Taking App

This is a lightweight, command-line based note-taking application written in Python. It allows users to create, view, edit, and delete notes, all of which are stored in a JSON file for persistence.

## 📦 Features

- Create new notes with a title and content  
- View all existing notes  
- Edit the content of a note  
- Delete a note by title  
- Saves notes to `notes.json` so they're available between sessions

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Running the App

1. Clone or download the script  
2. Open a terminal and navigate to the directory containing the script  
3. Run the script with:

       python your_script_name.py

> Replace `your_script_name.py` with the actual file name.

## 🧭 Interface

After running, you will see a menu:

       Notes
       Type 1 to create a new note
       Type 2 to view all notes
       Type 3 to delete a note
       Type 4 to edit an existing note
       Type 5 to quit

Follow the prompts to manage your notes.

## 📁 Data Persistence

Notes are stored in a file named `notes.json` in the same directory.  
If the file doesn't exist, it will be created automatically on your first save.

## 🛠 Code Structure

- **Note class**: Represents individual notes with `title` and `content`  
- **save_notes()**: Writes all current notes to `notes.json`  
- **load_notes()**: Loads notes from `notes.json` into memory at the start of each loop iteration

## ✅ Example Usage

1. **Create a new note**  
   Title: `Meeting`  
   Content: `Discuss project roadmap`

2. **View all notes**  
   Output:  
   `Meeting: Discuss project roadmap`

3. **Edit the note**  
   New content: `Discuss updated project roadmap`

4. **Delete the note**  
   Confirmation: `Note deleted`

## 📌 Notes

- Each note must have a unique title  
- Notes are reloaded from disk in each loop iteration for consistency and file sync

## 📃 License

This project is provided as-is for educational or personal use.
