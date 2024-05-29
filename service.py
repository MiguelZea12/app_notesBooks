from clases import Note, NoteBook

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
