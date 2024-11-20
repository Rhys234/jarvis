import os

def open_file(file_path):
    """Öffnet eine Datei oder Anwendung."""
    if os.path.exists(file_path):
        os.startfile(file_path)
        return f"Opening {file_path}."
    else:
        return "File not found."

def play_music(music_folder="C:\\Users\\Public\\Music"):
    """Spielt Musik aus einem angegebenen Ordner."""
    files = os.listdir(music_folder)
    if files:
        os.startfile(os.path.join(music_folder, files[0]))
        return "Playing music."
    else:
        return "No music files found."
