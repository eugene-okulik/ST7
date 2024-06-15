import os
from pathlib import Path

import ttkbootstrap as ttk
from ttkbootstrap.constants import CENTER
from tkinter import filedialog, messagebox, END
from typing import List, Tuple

from search import search_text_in_file


def display_results(results: List[Tuple[str, int, str]], search_text: str):
    file_names_text.config(state='normal')
    line_numbers_text.config(state='normal')
    context_text.config(state='normal')

    file_names_text.delete(1.0, END)
    line_numbers_text.delete(1.0, END)
    context_text.delete(1.0, END)

    if results:
        longest_file_name_length = 0
        for file, line_number, context in results:
            if len(file) > longest_file_name_length:
                longest_file_name_length = len(file)
            file_names_text.insert(END, f"{file}\n")
            line_numbers_text.insert(END, f"{line_number}\n", "center")

            start_idx = context.lower().find(search_text.lower())
            while start_idx != -1:
                end_idx = start_idx + len(search_text)
                context_text.insert(END, context[:start_idx])
                context_text.insert(END, context[start_idx:end_idx], 'highlight')
                context = context[end_idx:]
                start_idx = context.lower().find(search_text.lower())
            context_text.insert(END, context + "\n")

        file_names_text.config(width=longest_file_name_length)
        theme_combobox.grid(padx=80)
    else:
        file_names_text.insert(END, "No found\n")
        line_numbers_text.insert(END, "No found\n", "center")
        context_text.insert(END, "No found\n")

    line_numbers_text.tag_configure("center", justify='center')
    check_horizontal_scroll()

    file_names_text.config(state='disabled')
    line_numbers_text.config(state='disabled')
    context_text.config(state='disabled')


def search_logs():
    log_files_path = path_entry.get()
    search_text = text_entry.get()
    first_only = first_occurrence.get()

    if not os.path.isdir(log_files_path):
        messagebox.showerror("Error", f"The path {log_files_path} is not a valid directory.")
        return

    results = []
    for root, _, files in os.walk(log_files_path):
        for file in files:
            file_path = os.path.join(root, file)
            matches = search_text_in_file(file_path, search_text, first_only)
            for line_number, context in matches:
                results.append((file, line_number, context))

    display_results(results, search_text)


def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        path_entry.delete(0, END)
        path_entry.insert(0, directory)


def on_vertical_scroll(*args):
    file_names_text.yview(*args)
    line_numbers_text.yview(*args)
    context_text.yview(*args)


def on_horizontal_scroll(*args):
    context_text.xview(*args)


def on_mouse_wheel(event):
    file_names_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
    line_numbers_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
    context_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
    return "break"


def set_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(foreground='grey')

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(foreground='black')

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(foreground='grey')

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def check_horizontal_scroll(event=None):
    context_text.update_idletasks()
    bbox = context_text.bbox("end-1c")
    if bbox and bbox[2] < context_text.winfo_width():
        scrollbar_horizontal.grid_remove()
    else:
        scrollbar_horizontal.grid()


def change_theme(event=None):
    selected_theme = theme_combobox.get()
    if selected_theme == 'cyborg' or selected_theme == 'superhero':
        text_entry.config(foreground='white')
    else:
        text_entry.config(foreground='black')
    root.style.theme_use(selected_theme)
    theme_combobox.selection_clear()


def run_app():
    global file_names_text, line_numbers_text, context_text, path_entry, \
        text_entry, first_occurrence, scrollbar_horizontal, root, theme_combobox

    root = ttk.Window(themename="flatly")
    root.title("LogSea")
    root.resizable(False, False)

    base_dir = Path(__file__).resolve().parent.parent.parent.parent
    filepath = base_dir / 'evgeny_shit' / 'Homework_19' / 'logsea' / 'ico_ser.ico'

    icon_path = filepath
    root.iconbitmap(icon_path)

    output_frame = ttk.Frame(root)
    output_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

    ttk.Label(output_frame, text="File", font=('Helvetica', 10, 'bold'), anchor=CENTER).grid(row=0, column=0,
                                                                                             sticky='nsew', padx=(0, 2))
    ttk.Label(output_frame, text="Line", font=('Helvetica', 10, 'bold'), anchor=CENTER).grid(row=0, column=1,
                                                                                             sticky='nsew', padx=(0, 2))
    ttk.Label(output_frame, text="Context", font=('Helvetica', 10, 'bold'), anchor=CENTER).grid(row=0, column=2,
                                                                                                sticky='nsew')

    file_names_text = ttk.Text(output_frame, height=30, wrap=ttk.WORD, borderwidth=0, highlightthickness=0,
                               relief='solid')
    file_names_text.grid(row=1, column=0, sticky='nsew', padx=(0, 2))
    file_names_text.configure(state='disabled')

    line_numbers_text = ttk.Text(output_frame, width=10, height=30, wrap=ttk.WORD, borderwidth=0, highlightthickness=0,
                                 relief='solid')
    line_numbers_text.grid(row=1, column=1, sticky='nsew', padx=(0, 2))
    line_numbers_text.configure(state='disabled')

    context_text = ttk.Text(output_frame, width=100, height=30, wrap=ttk.NONE, borderwidth=0, highlightthickness=0,
                            relief='solid')
    context_text.grid(row=1, column=2, sticky='nsew')
    context_text.configure(state='disabled')

    scrollbar_vertical = ttk.Scrollbar(output_frame, orient='vertical', command=on_vertical_scroll)
    scrollbar_vertical.grid(row=1, column=3, sticky='ns')

    scrollbar_horizontal = ttk.Scrollbar(output_frame, orient='horizontal', command=on_horizontal_scroll)
    scrollbar_horizontal.grid(row=2, column=2, sticky='ew')

    file_names_text.config(yscrollcommand=scrollbar_vertical.set)
    line_numbers_text.config(yscrollcommand=scrollbar_vertical.set)
    context_text.config(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

    context_text.bind('<Configure>', check_horizontal_scroll)
    context_text.bind('<KeyRelease>', check_horizontal_scroll)
    context_text.bind('<MouseWheel>', check_horizontal_scroll)

    file_names_text.bind("<MouseWheel>", on_mouse_wheel)
    line_numbers_text.bind("<MouseWheel>", on_mouse_wheel)
    context_text.bind("<MouseWheel>", on_mouse_wheel)

    context_text.tag_configure('highlight', foreground='red', font=('Helvetica', 10, 'bold'))

    ttk.Label(root).grid(row=2, column=0, padx=10, pady=5, sticky='e')
    path_frame = ttk.Frame(root)
    path_frame.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky='w')
    path_entry = ttk.Entry(path_frame, width=50)
    path_entry.pack(side=ttk.LEFT, fill=ttk.X, expand=True)
    browse_button = ttk.Button(path_frame, text="Browse", command=browse_directory)
    browse_button.pack(side=ttk.RIGHT, padx=10)

    set_placeholder(path_entry, "Enter log directory path")

    ttk.Label(root).grid(row=3, column=0, padx=10, pady=5, sticky='e')
    text_frame = ttk.Frame(root)
    text_frame.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky='w')
    text_entry = ttk.Entry(text_frame, width=50)
    text_entry.pack(side=ttk.LEFT, fill=ttk.X, expand=True)
    search_button = ttk.Button(text_frame, text="Search", command=search_logs)
    search_button.pack(side=ttk.RIGHT, padx=10)

    set_placeholder(text_entry, "Enter text to search")

    first_occurrence = ttk.BooleanVar()
    first_occurrence_check = ttk.Checkbutton(root, text="Only the first", variable=first_occurrence)
    first_occurrence_check.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky='w')

    # Добавление выпадающего списка тем
    themes = ["superhero", "cyborg", "minty", "flatly", "journal"]
    theme_combobox = ttk.Combobox(root, values=themes, state='readonly')
    theme_combobox.grid(row=4, column=1, columnspan=1, padx=5, pady=10)

    theme_combobox.bind("<<ComboboxSelected>>", change_theme)
    theme_combobox.set("Theme")

    root.mainloop()
