import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

app = tk.Tk()
app.title("To-Do List")
app.configure(bg="#EFEFEF")

task_entry = tk.Entry(app)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
add_button.pack()

remove_button = tk.Button(app, text="Remove Task", command=remove_task, bg="#F44336", fg="white")
remove_button.pack()

task_list = tk.Listbox(app, bg="white")
task_list.pack()

app.mainloop()