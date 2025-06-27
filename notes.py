import json

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def __str__(self):
        return f'{self.title}: {self.content}'

notes = {
}

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump({title: note.__dict__ for title, note in notes.items()}, file, indent=4)

def load_notes():
        try:
            with open('notes.json', 'r') as file:
                data = json.load(file)
                for title,note_data in data.items():
                    notes[title] = Note(note_data["title"], note_data["content"])
        except FileNotFoundError:
            pass

while True:
    load_notes()
    print("Notes")
    print("Type 1 to create a new note")
    print("Type 2 to view all notes")
    print("Type 3 to delete a note")
    print("Type 4 to edit an existing note")
    print("Type 5 to quit")
    reply = input("")
    if reply == "1":
        title = input("Enter title: ")
        if title in notes:
            print("Note with that name already exists")
        else:
            content = input("Enter content: ")
            note = Note(title, content)
            notes[title] = note
            save_notes()
    elif reply == "2":
        for note in notes.values():
            print(note)
    elif reply == "3":
        print("Enter title to delete")
        delete = input("")
        try:
            notes.pop(delete)
            print("Note deleted")
            save_notes()
        except KeyError:
            print("Note not found")
    elif reply == "4":
        print("Enter title to edit an existing note")
        edit = input("")
        editcontent = input("Enter content: ")
        try:
            notes[edit].content = editcontent
            print("Note edited")
            save_notes()
        except KeyError:
            print("Note not found")
    elif reply == "5":
        print("Quitting")
        break
    else:
        print("Invalid input")

