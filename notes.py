import os

notes_file = "notes.txt"

def show_menu():
    print("\n--- SIMPLE NOTES APP ---")
    print("1. View Notes")
    print("2. Add Note")
    print("3. Delete All Notes")
    print("4. Exit")

def view_notes():
    if not os.path.exists(notes_file):
        print("\nNo notes found.")
        return
    print("\n--- Your Notes ---")
    with open(notes_file, "r") as file:
        notes = file.read()
        print(notes if notes else "No notes yet.")

def add_note():
    note = input("\nEnter your note: ")
    with open(notes_file, "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")

def delete_notes():
    if os.path.exists(notes_file):
        os.remove(notes_file)
        print("\nAll notes deleted.")
    else:
        print("\nNo notes to delete.")

while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        view_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")