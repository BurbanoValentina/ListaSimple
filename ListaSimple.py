import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext


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
        messagebox.showinfo("Éxito", "Tarea agregada con éxito.")

    def get_tasks_text(self):
        if self.head is None:
            return "No hay tareas registradas."

        tasks = ""
        current = self.head
        i = 1
        while current:
            tasks += (f"Tarea {i}: {current.title}\n"
                      f"   Qué debe hacer: {current.description}\n"
                      f"   Fecha inicio: {current.start_date}\n"
                      f"   Fecha fin: {current.end_date}\n"
                      f"   Profesor: {current.teacher}\n"
                      f"   Autor: {current.author}\n"
                      f"   Tipo: {current.task_type}\n"
                      f"   Entrega: {current.delivery}\n"
                      f"   Tiene examen: {current.exam}\n"
                      f"   Repositorio GitHub: {current.github}\n\n")
            current = current.next
            i += 1
        return tasks

    def search_task(self, title):
        if self.head is None:
            messagebox.showinfo("Buscar", "No hay tareas registradas.")
            return

        current = self.head
        while current:
            if current.title.lower() == title.lower():
                result = (f"Título: {current.title}\n"
                          f"Qué debe hacer: {current.description}\n"
                          f"Fecha inicio: {current.start_date}\n"
                          f"Fecha fin: {current.end_date}\n"
                          f"Profesor: {current.teacher}\n"
                          f"Autor: {current.author}\n"
                          f"Tipo: {current.task_type}\n"
                          f"Entrega: {current.delivery}\n"
                          f"Tiene examen: {current.exam}\n"
                          f"Repositorio GitHub: {current.github}\n")
                messagebox.showinfo("Tarea encontrada", result)
                return
            current = current.next

        messagebox.showwarning("Buscar", "No se encontró ninguna tarea con ese título.")


def main_gui():
    task_list = TaskList()

    def add_task_gui():
        title = simpledialog.askstring("Agregar tarea", "Ingrese el título de la tarea:")
        description = simpledialog.askstring("Agregar tarea", "Ingrese qué debe hacer:")
        start_date = simpledialog.askstring("Agregar tarea", "Ingrese la fecha de inicio (dd/mm/aaaa):")
        end_date = simpledialog.askstring("Agregar tarea", "Ingrese la fecha de fin (dd/mm/aaaa):")
        teacher = simpledialog.askstring("Agregar tarea", "Ingrese el nombre del profesor:")
        author = simpledialog.askstring("Agregar tarea", "Ingrese el autor de la tarea:")
        task_type = simpledialog.askstring("Agregar tarea", "¿La tarea es individual o grupal?")
        delivery = simpledialog.askstring("Agregar tarea", "¿Debe subirse al Campus o al WhatsApp?")
        exam = simpledialog.askstring("Agregar tarea", "¿La actividad tiene examen? (Sí/No)")
        github = simpledialog.askstring("Agregar tarea", "Ingrese el nombre/URL del repositorio en GitHub:")

        if title and description and start_date and end_date:
            task_list.add_task(title, description, start_date, end_date, teacher, author, task_type, delivery, exam, github)

    def show_tasks_gui():
        tasks = task_list.get_tasks_text()
        win = tk.Toplevel(root)
        win.title("Historial de tareas")
        win.geometry("500x400")

        text_area = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=60, height=20, font=("Arial", 10))
        text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        text_area.insert(tk.END, tasks)
        text_area.config(state=tk.DISABLED)

    def search_task_gui():
        title = simpledialog.askstring("Buscar tarea", "Ingrese el título de la tarea a buscar:")
        if title:
            task_list.search_task(title)

    root = tk.Tk()
    root.title("Gestión de Tareas")
    root.geometry("400x300")

    tk.Label(root, text="MENÚ DE GESTIÓN DE TAREAS", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(root, text="Agregar tarea", width=30, command=add_task_gui).pack(pady=5)
    tk.Button(root, text="Mostrar historial de tareas", width=30, command=show_tasks_gui).pack(pady=5)
    tk.Button(root, text="Buscar tarea", width=30, command=search_task_gui).pack(pady=5)
    tk.Button(root, text="Salir", width=30, command=root.quit).pack(pady=5)

    root.mainloop()


main_gui()
