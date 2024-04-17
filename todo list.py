import tkinter as tk
from tkinter import messagebox

# Class to represent a task
class Task:
  def __init__(self, title, description="", is_done=False):
    self.title = title
    self.description = description
    self.is_done = is_done

# Function to add a task to the listbox
def add_task():
  title = entry_title.get()
  description = entry_description.get("1.0", tk.END)
  if title != "":
    task = Task(title, description)
    tasks.append(task)
    display_tasks()
    entry_title.delete(0, tk.END)
    entry_description.delete("1.0", tk.END)

# Function to display tasks in the listbox
def display_tasks():
  listbox.delete(0, tk.END)
  for task in tasks:
    if task.is_done:
      listbox.insert(tk.END, f"[DONE] {task.title}", foreground="green")  # Green for done tasks
    else:
      listbox.insert(tk.END, task.title)

# Function to mark a task as done/undone
def mark_done():
  selected = listbox.curselection()
  if selected:
    index = selected[0]
    tasks[index].is_done = not tasks[index].is_done
    display_tasks()

# Function to edit a task
def edit_task():
  selected = listbox.curselection()
  if selected:
    index = selected[0]
    title = entry_title.get()
    description = entry_description.get("1.0", tk.END)
    if title != "":
      tasks[index].title = title
      tasks[index].description = description
      display_tasks()
    else:
      messagebox.showerror("Error", "Please enter a title for the task")

# Function to delete a task
def delete_task():
  selected = listbox.curselection()
  if selected:
    message = messagebox.askquestion("Confirm", "Are you sure you want to delete?")
    if message == "yes":
      listbox.delete(selected[0])
      tasks.pop(selected[0])

# Main window
window = tk.Tk()
window.title("To-Do List")
window.config(bg="lightblue")  # Set background color of the window

# Task list (initially empty)
tasks = []

# Labels and entry fields for title and description
label_title = tk.Label(window, text="Title:", bg="lightblue")  # Match label background to window
label_title.pack()
entry_title = tk.Entry(window, width=50, bg="white")  # White background for entry field
entry_title.pack()

label_description = tk.Label(window, text="Description:", bg="lightblue")  # Match label background to window
label_description.pack()
entry_description = tk.Text(window, width=50, height=5, bg="white")  # White background for text field
entry_description.pack()

# Buttons for adding, marking done, editing, and deleting tasks
button_add = tk.Button(window, text="Add Task", command=add_task, bg="lightgreen")  # Green button
button_add.pack()

button_done = tk.Button(window, text="Mark Done", command=mark_done, bg="lightyellow")  # Yellow button
button_done.pack()

button_edit = tk.Button(window, text="Edit Task", command=edit_task, bg="lightcoral")  # Coral button
button_edit.pack()

button_delete = tk.Button(window, text="Delete Task", command=delete_task, bg="lightpink")  # Pink button
button_delete.pack()

# Listbox to display tasks
listbox = tk.Listbox(window, width=50, bg="lightgray")  # Light gray background for listbox
listbox.pack()

# Display initially empty list
display_tasks()

window.mainloop()
