class Node:
    def __init__(self, title, description, start_date, end_date, teacher, author, task_type, delivery, exam, github):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.teacher = teacher
        self.author = author
        self.task_type = task_type
        self.delivery = delivery       
        self.exam = exam               
        self.github = github           
        self.next = None               


class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, title, description, start_date, end_date, teacher, author, task_type, delivery, exam, github):
        new_node = Node(title, description, start_date, end_date, teacher, author, task_type, delivery, exam, github)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("\n Tarea agregada con éxito.\n")

    def show_tasks(self):
        if self.head is None:
            print("\n No hay tareas registradas.\n")
        else:
            print("\n Historial de tareas:\n")
            current = self.head
            i = 1
            while current:
                print(f"Tarea {i}: {current.title}")
                print(f"   Qué debe hacer: {current.description}")
                print(f"   Fecha inicio: {current.start_date}")
                print(f"   Fecha fin: {current.end_date}")
                print(f"   Profesor: {current.teacher}")
                print(f"   Autor: {current.author}")
                print(f"   Tipo: {current.task_type}")
                print(f"   Entrega: {current.delivery}")
                print(f"   Tiene examen: {current.exam}")
                print(f"   Repositorio GitHub: {current.github}\n")
                current = current.next
                i += 1

    def search_task(self, title):
        if self.head is None:
            print("\n No hay tareas registradas.\n")
            return

        current = self.head
        while current:
            if current.title.lower() == title.lower():
                print("\n Tarea encontrada:\n")
                print(f"    Título: {current.title}")
                print(f"    Qué debe hacer: {current.description}")
                print(f"    Fecha inicio: {current.start_date}")
                print(f"    Fecha fin: {current.end_date}")
                print(f"    Profesor: {current.teacher}")
                print(f"    Autor: {current.author}")
                print(f"    Tipo: {current.task_type}")
                print(f"    Entrega: {current.delivery}")
                print(f"    Tiene examen: {current.exam}")
                print(f"    Repositorio GitHub: {current.github}\n")
                return
            current = current.next

        print("\n No se encontró ninguna tarea con ese título.\n")


# Programa principal con menú (menú sigue en español)
def menu():
    task_list = TaskList()

    while True:
        print("===== MENÚ DE GESTIÓN DE TAREAS =====")
        print("1. Agregar tarea")
        print("2. Mostrar historial de tareas")
        print("3. Buscar tarea")
        print("4. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            title = input("Ingrese el título de la tarea: ")
            description = input("Ingrese qué debe hacer: ")
            start_date = input("Ingrese la fecha de inicio (dd/mm/aaaa): ")
            end_date = input("Ingrese la fecha de fin (dd/mm/aaaa): ")
            teacher = input("Ingrese el nombre del profesor: ")
            author = input("Ingrese el autor de la tarea: ")
            task_type = input("¿La tarea es individual o grupal?: ")
            delivery = input("¿Debe subirse al Campus o al WhatsApp?: ")
            exam = input("¿La actividad tiene examen? (Sí/No): ")
            github = input("Ingrese el nombre/URL del repositorio en GitHub: ")

            task_list.add_task(title, description, start_date, end_date, teacher, author, task_type, delivery, exam, github)

        elif option == "2":
            task_list.show_tasks()
        elif option == "3":
            title = input("Ingrese el título de la tarea a buscar: ")
            task_list.search_task(title)
        elif option == "4":
            print("\n Saliendo del programa...")
            break
        else:
            print("\n Opción no válida, intente de nuevo.\n")


# Ejecutar menú
menu()


