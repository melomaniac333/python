'''import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x300")

tk.Label(root, text="Student Registration",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Age").pack()
age = tk.Entry(root)
age.pack()

tk.Label(root, text="Email").pack()
email = tk.Entry(root)
email.pack()

def register():
    n = name.get().strip()
    a = age.get().strip()
    e = email.get().strip()

    if n == "" or a == "" or e == "":
        messagebox.showerror("Error", "Fill all fields")
    elif not n.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Enter a valid name")
    elif not a.isdigit() or int(a) < 1 or int(a) > 120:
        messagebox.showerror("Error", "Enter a valid age")
    elif "@" not in e or "." not in e:
        messagebox.showerror("Error", "Enter a valid email")
    else:
        messagebox.showinfo("Success", "Registration Successful!")

tk.Button(root, text="Register",
          command=register).pack(pady=15)

root.mainloop()'''

'''from tkinter import Tk, Label, Entry, IntVar, Checkbutton, Button
from tkinter import messagebox

root = Tk()
root.title("Student Form")
root.geometry("300x300")

Label(root, text="Student Form",
      font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Student Name").pack()
name = Entry(root)
name.pack()

Label(root, text="Roll Number").pack()
roll = Entry(root)
roll.pack()

Label(root, text="Select Subjects").pack(pady=5)

s1 = IntVar()
s2 = IntVar()
s3 = IntVar()

Checkbutton(root, text="Python", variable=s1).pack()
Checkbutton(root, text="Java", variable=s2).pack()
Checkbutton(root, text="Database", variable=s3).pack()

def submit():
    subjects = []

    if s1.get():
        subjects.append("Python")
    if s2.get():
        subjects.append("Java")
    if s3.get():
        subjects.append("Database")

    messagebox.showinfo(
        "Student Details",
        f"Name: {name.get()}\n"
        f"Roll No: {roll.get()}\n"
        f"Subjects: {', '.join(subjects)}"
    )

Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()'''

import tkinter as tk
from tkinter import filedialog, messagebox


root = tk.Tk()
root.title("My Notepad")
root.geometry("1000x600")
root.configure(bg="white")

menu = tk.Menu(root)

file_menu = tk.Menu(menu, tearoff=0)

def new_file():
    editor.delete("1.0", tk.END)
    root.title("My Notepad")

def open_file():
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r") as f:
            editor.delete("1.0", tk.END)
            editor.insert("1.0", f.read())
        root.title(file)

def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt"
    )
    if file:
        with open(file, "w") as f:
            f.write(editor.get("1.0", tk.END))
        messagebox.showinfo("Saved", "File saved successfully!")

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

menu.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu, tearoff=0)

edit_menu.add_command(
    label="Cut",
    command=lambda: editor.event_generate("<<Cut>>")
)
edit_menu.add_command(
    label="Copy",
    command=lambda: editor.event_generate("<<Copy>>")
)
edit_menu.add_command(
    label="Paste",
    command=lambda: editor.event_generate("<<Paste>>")
)
edit_menu.add_command(
    label="Select All",
    command=lambda: editor.tag_add("sel", "1.0", "end")
)

menu.add_cascade(label="Edit", menu=edit_menu)

# View Menu
view_menu = tk.Menu(menu, tearoff=0)
view_menu.add_command(
    label="Clear Text",
    command=lambda: editor.delete("1.0", tk.END)
)
menu.add_cascade(label="View", menu=view_menu)

root.config(menu=menu)

toolbar = tk.Frame(root, bg="#eeeeee")
toolbar.pack(fill="x")

tk.Button(
    toolbar, text="H1",
    command=lambda: editor.config(font=("Arial", 18))
).pack(side="left", padx=5, pady=5)

tk.Button(
    toolbar, text="B",
    command=lambda: editor.config(font=("Arial", 12, "bold"))
).pack(side="left", padx=5)

tk.Button(
    toolbar, text="I",
    command=lambda: editor.config(font=("Arial", 12, "italic"))
).pack(side="left", padx=5)

tk.Button(
    toolbar, text="Default",
    command=lambda: editor.config(font=("Arial", 12))
).pack(side="left", padx=5)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

editor = tk.Text(
    frame,
    font=("Arial", 12),
    wrap="word",
    undo=True,
    yscrollcommand=scrollbar.set,
    bg="white",
    fg="black",
    padx=8,
    pady=8
)
editor.pack(fill="both", expand=True)

scrollbar.config(command=editor.yview)

status = tk.Label(
    root,
    text="Ln 1, Col 1 | 0 characters | Plain text | UTF-8",
    anchor="w",
    bg="#eeeeee",
    fg="#555555",
    padx=10,
    pady=5
)
status.pack(side="bottom", fill="x")

def update_status(event=None):
    text = editor.get("1.0", "end-1c")
    position = editor.index("insert")
    line, column = position.split(".")

    status.config(
        text=f"Ln {line}, Col {int(column)+1} | "
             f"{len(text)} characters | Plain text | UTF-8"
    )

# Keyboard Shortcuts
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())

# Update status when typing or clicking
editor.bind("<KeyRelease>", update_status)
editor.bind("<ButtonRelease-1>", update_status)

# Start Application
editor.focus_set()
root.mainloop()