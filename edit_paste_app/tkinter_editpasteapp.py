import tkinter as tk
import traceback
import platform

from tkinter import Menu
from tkinter import messagebox

from richxerox import copy, paste, available
from edit_paste_app.text_transformer import transform_text_pdf, transform_text_social_media
from edit_paste_app.logger_wrapper import logger
from edit_paste_app.__init__ import get_version

HEIGHT = 25
TITLE = "Paste Text From Chats to Strip The Sender"

default_transform_function = transform_text_social_media  # transform_text_pdf


def change_default_function(fn):
    # print(1)
    global default_transform_function
    default_transform_function = fn
    # messagebox.showinfo("changed default fn", default_transform_function)
    logger.info(f"default_transform_function  {default_transform_function}")


# receives an event
def handle_clipboard(_):
    try:
        # cb = pyperclip.paste() # root.clipboard_get() # cb = clipboard.paste() # none of them working with ó í á à
        # root.clipboard_append(cb_transformed) # clipboard.copy(cb_transformed)

        clipboard = paste()

        if not "text" in available():
            logger.info(f"Clipboard is not string. Available types {available()}")
            return "break"

        # logger.debug(f'{cb}')

        cb_transformed = default_transform_function(clipboard)
        copy(cb_transformed)

        text.delete("0.0", tk.END)
        text.insert("0.0", cb_transformed)
        text.insert(tk.END, "\n\n\n\n\t\t\t\tCOPIED TO CLIPBOARD")

    except Exception as e:
        logger.error(traceback.format_exc())

    return "break"


# to bring the window to the front on opening


def raise_above_all(window):
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(root.attributes, "-topmost", False)


def create_help_submenu(menubar: Menu, version: str):
    help_ = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_)
    logger.info(version)
    help_.add_command(label="About", command=lambda: messagebox.showinfo("Versió", f"EditPasteApp v{version}"))


def main():
    logger.info(f"running with py version {platform.python_version()}...")

    try:
        global root, text
        root = tk.Tk()
        root.title(TITLE)
        text = tk.Text(height=HEIGHT, fg="white", bg="black")
        text.pack(side="top", fill="x")

        menubar = Menu(root)
        mode_menu = Menu(menubar, tearoff=0)
        mode_menu.add_command(label="Transform PDF text", command=lambda: change_default_function(transform_text_pdf))
        mode_menu.add_command(
            label="Transform Telegram/Whats text", command=lambda: change_default_function(transform_text_social_media)
        )
        menubar.add_cascade(label="Edit", menu=mode_menu)

        # Adding Help Menu
        create_help_submenu(menubar, get_version())

        for _ in range(int(HEIGHT / 2)):
            text.insert("end", "\n")

        text.insert("end", "\t\t\t\tPaste content to transform")

        root.bind_all("<<Paste>>", handle_clipboard)

        root.config(menu=menubar)

        raise_above_all(root)

        root.mainloop()
    except Exception as e:
        logger.error(e, exc_info=True)


if __name__ == "__main__":
    main()
