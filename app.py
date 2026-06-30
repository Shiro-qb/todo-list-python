import tkinter as tk
from Task import Task

tasks = []
def add_task():
    title = entry.get( )
    if title is None:
        return
    task = Task(title, False, "", "")
    tasks.append(task)
    listbox.insert(tk.END, task.title)
    entry.delete(0, tk.END)

def delete_task():
    selection = listbox.curselection()
    if not selection:
        return
    index = selection[0]
    tasks.pop(index)
    listbox.delete(index)






root = tk.Tk()
root.title("To Do List")
root.mainloop()