from service import get_user_input, add_note_prompt, remove_note_prompt
from clases import NoteBook

'''
Caso Práctico 5: Aplicación de Notas
Una aplicación para tomar, editar y borrar notas
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
if __name__ == '__main__':
    app()
