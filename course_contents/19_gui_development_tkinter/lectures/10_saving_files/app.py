import tkinter as tk
from tkinter import ttk, filedialog


def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)

    notebook.add(text_area, text="Untitled")
    notebook.pack(fill="both", expand=True)
    notebook.select(text_area)


def save_file():
    file_path = filedialog.asksaveasfilename()

    try:
        filename = file_path.split("/")[-1]
        current = root.nametowidget(notebook.select())
        content = current.get("1.0", "end-1c")

        with open(file_path, "w") as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    notebook.tab("current", text=filename)


root = tk.Tk()
root.title("Teclado Text Editor")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=(1), pady=(4, 0))

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)

menubar.add_cascade(menu=file_menu, label="File")

file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Save", command=save_file)

notebook = ttk.Notebook(main)

create_file()

root.mainloop()
