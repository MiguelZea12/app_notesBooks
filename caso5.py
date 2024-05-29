'''
Caso Práctico 5: Aplicación de Notas
Una aplicación para tomar, editar y borrar notas
'''

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f'::::::::::Titulo::::::::::\n{self.title}\n::::::::::Contenido::::::::::\n{self.content}'
    
class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        print(f'Nota "{note.title}" agregada.')

    def remove_note_by_title(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print(f'La nota "{title}" ha sido eliminada.')
                return
        print(f'La nota "{title}" no está en la lista de tareas.')

    def list_notes(self):
        if not self.notes:
            print("No hay notas en el cuaderno.")
        else:
            for note in self.notes:
                print(note)

#Funcion para obtener la opcion del usuario.
def get_user_input():
    return input('Ingresa la opción que deseas realizar: add, remove, view all, o exit: ').strip().lower()

#Funcion por si el usuario escoge añadir, y pueda colocar el nombre y la descripcion.
def add_note_prompt(notebook):
    title = input('Ingresa el título de la nota: ')
    content = input('Ingresa el contenido de la nota: ')
    notebook.add_note(Note(title, content))

#Funcion por si el usuario escoge eliminar, y pueda eliminar la nota con el titulo especifico.
def remove_note_prompt(notebook):
    title = input('Ingresa el título de la nota a eliminar: ')
    notebook.remove_note_by_title(title)


'''
Creacion de bucle para la funcionalidad de la app. Solo termina si el usuario quiere salir con Exit
'''
def app():
    notebook = NoteBook()
    while True:
        response = get_user_input()
        if response == 'add':           #Si decide añadir una nota, debe de escribir add
            add_note_prompt(notebook)
        elif response == 'remove':      #Si decide eliminar una nota, debe de escribir remove
            remove_note_prompt(notebook)
        elif response == 'view all':    #Si decide ver todas las notas, debe de escribir view all
            notebook.list_notes()
        elif response == 'exit':        #Si decide salir de la app, debe de escribir exit
            print('Saliendo de la aplicación de notas.')
            break
        else:
            print('Opción no válida. Inténtalo de nuevo.')

# Ejecutar la aplicación
app()



