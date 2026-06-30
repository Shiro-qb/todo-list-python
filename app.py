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
#Input field
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

#Button
add_button = tk.Button(root, text = 'Add task', command = add_task)
add_button.pack(padx=15, pady=5)

delete_button = tk.Button(root, text = "Delete task", command = delete_task)
delete_button.pack(padx=20, pady=5)
#List of tasks
listbox = tk.Listbox(root, width=50, height=20)
listbox.pack(pady=10)

root.mainloop()