class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f'::::::::::Titulo::::::::::\n{self.title}\n::::::::::Contenido::::::::::\n{self.content}'
    
class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note (self, note):
        self.notes.append(note)
        print(f'Nota "{note.title}" agregada.')

    def remove_note_by_title (self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print(f'La nota "{title}" ha sido eliminada.')
                return
        print(f'La nota "{title}" no está en la lista de tareas.')

    def list_notes (self):
        if not self.notes:
            print("No hay notas en el cuaderno.")
        else:
            for note in self.notes:
                print(note)
