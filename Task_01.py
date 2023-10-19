#****TASK 01****
#****TO-DO-LIST****
import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the to-do list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task = listbox.get(listbox.curselection())
        listbox.delete(listbox.curselection())
    except:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget for task input
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack()

# Create buttons for adding and deleting tasks
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)

add_button.pack()
delete_button.pack()

# Run the application
root.mainloop()
