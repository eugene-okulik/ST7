import os
from pathlib import Path
from typing import List, Tuple

import ttkbootstrap as ttk
from ttkbootstrap.constants import CENTER
from tkinter import filedialog, messagebox, END

from search import search_text_in_file
from utils import set_placeholder, check_horizontal_scroll, on_vertical_scroll, on_horizontal_scroll, on_mouse_wheel


def display_results(results: List[Tuple[str, int, str]], search_text: str) -> None:
    """
    Display the search results in the text widgets.

    Args:
        results (List[Tuple[str, int, str]]): List of tuples containing file name, line number, and context.
        search_text (str): The text that was searched for.
    """
    clear_and_enable_text_widgets()
    update_text_widgets(results, search_text)
    line_numbers_text.tag_configure("center", justify='center')
    check_horizontal_scroll(context_text, scrollbar_horizontal)
    disable_text_widgets()


def clear_and_enable_text_widgets() -> None:
    """
    Clear the content of text widgets and enable them for editing.
    """
    file_names_text.config(state='normal')
    line_numbers_text.config(state='normal')
    context_text.config(state='normal')

    file_names_text.delete(1.0, END)
    line_numbers_text.delete(1.0, END)
    context_text.delete(1.0, END)


def update_text_widgets(results: List[Tuple[str, int, str]], search_text: str) -> None:
    """
    Update the text widgets with search results.

    Args:
        results (List[Tuple[str, int, str]]): List of tuples containing file name, line number, and context.
        search_text (str): The text that was searched for.
    """
    if results:
        for file, line_number, context in results:
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

        theme_combobox.grid(padx=80)
    else:
        file_names_text.insert(END, "No results found\n")
        line_numbers_text.insert(END, "No results found\n", "center")
        context_text.insert(END, "No results found\n")


def disable_text_widgets() -> None:
    """
    Disable the text widgets to prevent further editing.
    """
    file_names_text.config(state='disabled')
    line_numbers_text.config(state='disabled')
    context_text.config(state='disabled')


def search_logs() -> None:
    """
    Search for the specified text in log files located in the directory specified by the user.
    """
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


def browse_directory() -> None:
    """
    Open a directory selection dialog and insert the selected directory path into the path entry widget.
    """
    directory = filedialog.askdirectory()
    if directory:
        path_entry.delete(0, END)
        path_entry.insert(0, directory)


def change_theme(event=None) -> None:
    """
    Change the theme of the application based on the selected value from the theme combobox.

    Args:
        event: Optional event argument, default is None.
    """
    selected_theme = theme_combobox.get()
    text_entry.config(foreground='white' if selected_theme in ['cyborg', 'superhero'] else 'black')
    root.style.theme_use(selected_theme)
    theme_combobox.selection_clear()


def configure_text_widgets() -> None:
    """
    Configure the text widgets for synchronized scrolling and other behaviors.
    """
    file_names_text.config(yscrollcommand=scrollbar_vertical.set)
    line_numbers_text.config(yscrollcommand=scrollbar_vertical.set)
    context_text.config(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

    context_text.bind('<Configure>', lambda e: check_horizontal_scroll(context_text, scrollbar_horizontal))
    context_text.bind('<KeyRelease>', lambda e: check_horizontal_scroll(context_text, scrollbar_horizontal))
    context_text.bind('<MouseWheel>', lambda e: check_horizontal_scroll(context_text, scrollbar_horizontal))

    file_names_text.bind(
        "<MouseWheel>", lambda e: on_mouse_wheel(file_names_text, line_numbers_text, context_text, e)
    )
    line_numbers_text.bind(
        "<MouseWheel>", lambda e: on_mouse_wheel(file_names_text, line_numbers_text, context_text, e)
    )
    context_text.bind(
        "<MouseWheel>", lambda e: on_mouse_wheel(file_names_text, line_numbers_text, context_text, e)
    )

    context_text.tag_configure('highlight', foreground='red', font=('Helvetica', 10, 'bold'))


def create_output_frame(parent) -> None:
    """
    Create the output frame containing file, line, and context text widgets.
    """
    global file_names_text, line_numbers_text, context_text, scrollbar_vertical, scrollbar_horizontal

    output_frame = ttk.Frame(parent)
    output_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

    ttk.Label(
        output_frame, text="File", font=('Helvetica', 10, 'bold'), anchor=CENTER).grid(
        row=0, column=0, sticky='nsew', padx=(0, 2)
    )
    ttk.Label(
        output_frame, text="Line", font=('Helvetica', 10, 'bold'), anchor=CENTER).grid(
        row=0, column=1, sticky='nsew', padx=(0, 2)
    )
    ttk.Label(
        output_frame, text="Context", font=('Helvetica', 10, 'bold'), anchor=CENTER).grid(
        row=0, column=2, sticky='nsew'
    )

    file_names_text = ttk.Text(
        output_frame, width=30, height=30, wrap=ttk.NONE, borderwidth=0, highlightthickness=0, relief='solid'
    )
    file_names_text.grid(row=1, column=0, sticky='nsew', padx=(0, 2))
    file_names_text.configure(state='disabled')

    line_numbers_text = ttk.Text(
        output_frame, width=10, height=30, wrap=ttk.NONE, borderwidth=0, highlightthickness=0, relief='solid'
    )
    line_numbers_text.grid(row=1, column=1, sticky='nsew', padx=(0, 2))
    line_numbers_text.configure(state='disabled')

    context_text = ttk.Text(
        output_frame, width=100, height=30, wrap=ttk.NONE, borderwidth=0, highlightthickness=0, relief='solid'
    )
    context_text.grid(row=1, column=2, sticky='nsew')
    context_text.configure(state='disabled')

    scrollbar_vertical = ttk.Scrollbar(
        output_frame, orient='vertical', command=lambda *args: on_vertical_scroll(
            file_names_text, line_numbers_text, context_text, *args)
    )
    scrollbar_vertical.grid(row=1, column=3, sticky='ns')

    scrollbar_horizontal = ttk.Scrollbar(
        output_frame, orient='horizontal', command=lambda *args: on_horizontal_scroll(context_text, *args)
    )
    scrollbar_horizontal.grid(row=2, column=2, sticky='ew')

    configure_text_widgets()


def create_path_frame(parent) -> None:
    """
    Create the frame for the log directory path entry and browse button.

    Args:
        parent: The parent widget.
    """
    global path_entry

    ttk.Label(parent).grid(row=2, column=0, padx=10, pady=5, sticky='e')
    path_frame = ttk.Frame(parent)
    path_frame.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky='w')
    path_entry = ttk.Entry(path_frame, width=50)
    path_entry.pack(side=ttk.LEFT, fill=ttk.X, expand=True)
    browse_button = ttk.Button(path_frame, text="Browse", command=browse_directory)
    browse_button.pack(side=ttk.RIGHT, padx=10)

    set_placeholder(path_entry, "Enter log directory path")


def create_text_frame(parent) -> None:
    """
    Create the frame for the search text entry and search button.

    Args:
        parent: The parent widget.
    """
    global text_entry

    ttk.Label(parent).grid(row=3, column=0, padx=10, pady=5, sticky='e')
    text_frame = ttk.Frame(parent)
    text_frame.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky='w')
    text_entry = ttk.Entry(text_frame, width=50)
    text_entry.pack(side=ttk.LEFT, fill=ttk.X, expand=True)
    search_button = ttk.Button(text_frame, text="Search", command=search_logs)
    search_button.pack(side=ttk.RIGHT, padx=10)

    set_placeholder(text_entry, "Enter text to search")


def create_options(parent) -> None:
    """
    Create the options section including first occurrence checkbox and theme combobox.

    Args:
        parent: The parent widget.
    """
    global first_occurrence, theme_combobox

    first_occurrence = ttk.BooleanVar()
    first_occurrence_check = ttk.Checkbutton(parent, text="Only the first", variable=first_occurrence)
    first_occurrence_check.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky='w')

    themes = ["superhero", "cyborg", "minty", "flatly", "journal"]
    theme_combobox = ttk.Combobox(parent, values=themes, state='readonly')
    theme_combobox.grid(row=4, column=1, columnspan=1, padx=5, pady=10)

    theme_combobox.bind("<<ComboboxSelected>>", change_theme)
    theme_combobox.set("Theme")


def run_app() -> None:
    global root

    root = ttk.Window(themename="flatly")
    root.title("LogSea")
    root.resizable(False, False)

    icon_path = Path(__file__).resolve().parent / 'ico_ser.ico'
    root.iconbitmap(icon_path)

    create_output_frame(root)
    create_path_frame(root)
    create_text_frame(root)
    create_options(root)

    root.mainloop()
