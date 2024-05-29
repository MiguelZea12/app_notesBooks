# Caso Práctico 2: Aplicación de Seguimiento de Tareas
# Una aplicación que permite a los usuarios crear, actualizar y eliminar tareas.

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.complete = False

    def completed(self):
        self.complete = True

    def __str__(self):
        status = "Completed" if self.complete else "Pending"
        return f"{self.title} - {status}\n{self.description}"
    

class ManageTask:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f'No se encuentra {task.title}')

    def list_task(self):
        for task in self.tasks:
            print(task)

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
    
manage = ManageTask()
task1 = Task("Hacer la tarea de calidad de software", "La tarea se trata de las ISO")
task2 = Task('Hacer la tarea de desarrollo de sistema informatico', 'La tarea de realizar el diseño del proyecto')

manage.add_task(task1)
manage.add_task(task2)
manage.list_task()
task1.completed()


print("\nDespués de completar la tarea 1:")
manage.list_task()


