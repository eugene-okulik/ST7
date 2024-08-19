from tkinter import END


def set_placeholder(entry, placeholder: str) -> None:
    """
    Set a placeholder text in an entry widget and manage its behavior.
    """
    entry.insert(0, placeholder)
    entry.config(foreground='grey')

    def on_focus_in(event) -> None:
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(foreground='black')

    def on_focus_out(event) -> None:
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(foreground='grey')

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def check_horizontal_scroll(context_text, scrollbar_horizontal) -> None:
    """
    Check if horizontal scrolling is needed for the context text widget and adjust scrollbar visibility.
    """
    context_text.update_idletasks()
    bbox = context_text.bbox("end-1c")
    if bbox and bbox[2] < context_text.winfo_width():
        scrollbar_horizontal.grid_remove()
    else:
        scrollbar_horizontal.grid()


def check_vertical_scroll(context_text, scrollbar_vertical) -> None:
    """
    Check if vertical scrolling is needed for the context text widget and adjust scrollbar visibility.
    """
    context_text.update_idletasks()
    bbox = context_text.bbox("end-1c")
    if bbox and bbox[3] < context_text.winfo_height():
        scrollbar_vertical.grid_remove()
    else:
        scrollbar_vertical.grid()


def on_vertical_scroll(file_names_text, line_numbers_text, context_text, *args) -> None:
    """
    Synchronize vertical scrolling for text widgets.
    """
    file_names_text.yview(*args)
    line_numbers_text.yview(*args)
    context_text.yview(*args)


def on_horizontal_scroll(context_text, *args) -> None:
    """
    Synchronize horizontal scrolling for the context text widget.
    """
    context_text.xview(*args)


def on_mouse_wheel(file_names_text, line_numbers_text, context_text, event) -> str:
    """
    Handle mouse wheel events for scrolling.
    """
    file_names_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
    line_numbers_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
    context_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
    return "break"
