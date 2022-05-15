import logging
import os
import tkinter as tk
import traceback

from tkinter import Menu
from tkinter import messagebox

from richxerox import copy, paste, available
from .text_transformer import transform_text_pdf, transform_text_social_media
import platform
from .app_config import AppConfig

home = os.path.expanduser("~")

HEIGHT = 25
TITLE = "Paste Text From Chats to Strip The Sender"

defaultTransformFunction = transform_text_social_media  # transform_text_pdf

from .__init__ import get_version

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DEBUG_FILENAME = "debug.log"

# TODO: make this file a class and create a global variable for the log path or another best practice
# https://docs.python.org/3/howto/logging.html
logFileDir = home + "/Library/Logs/EditPasteApp/"  # create logs directory if not exists
logFile = logFileDir + "editpasteapp.log"
try:
    os.makedirs(logFileDir)
except FileExistsError as e:
    pass

if AppConfig.isDev:
    logging.basicConfig(filename=DEBUG_FILENAME, encoding="utf-8", level=logging.DEBUG)
else:
    logging.basicConfig(
        filename=logFile, encoding="utf-8", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
logger.info("1st")


# def get_version():
#     return __version__
#     fn = os.path.join(os.path.dirname(__file__), "edit_paste_app", "__init__.py")
#     with open(fn) as f:
#         res=re.findall("__version__ = \"([\d.\w]+)\"", f.read())
#         return res[0]


def changeDefaultFunction(fn):
    # print(1)
    global defaultTransformFunction
    defaultTransformFunction = fn
    # messagebox.showinfo("changed default fn", defaultTransformFunction)
    logger.info(f"defaultTransformFunction  {defaultTransformFunction}")


def handle_clipboard(event):
    try:
        # cb = pyperclip.paste() # root.clipboard_get() # cb = clipboard.paste() # none of them working with ó í á à
        # root.clipboard_append(cb_transformed) # clipboard.copy(cb_transformed)

        clipboard = paste()

        if not "text" in available():
            logger.info(f"Clipboard is not string. Available types {available()}")
            return "break"

        # logging.debug(f'{cb}')

        cb_transformed = defaultTransformFunction(clipboard)
        copy(cb_transformed)

        text.delete("0.0", tk.END)
        text.insert("0.0", cb_transformed)
        text.insert(tk.END, "\n\n\n\n\t\t\t\tCOPIED TO CLIPBOARD")

    except Exception as e:
        logging.error(traceback.format_exc())

    return "break"


# to bring the window to the front on opening
def raise_above_all(window):
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(root.attributes, "-topmost", False)


def main():
    logger.info(f"running with py version {platform.python_version()}...")

    try:
        global root, text
        root = tk.Tk()
        root.title(TITLE)
        text = tk.Text(height=HEIGHT, fg="white", bg="black")
        text.pack(side="top", fill="x")

        menubar = Menu(root)
        modeMenu = Menu(menubar, tearoff=0)
        modeMenu.add_command(label="Transform PDF text", command=lambda: changeDefaultFunction(transform_text_pdf))
        modeMenu.add_command(
            label="Transform Telegram/Whats text", command=lambda: changeDefaultFunction(transform_text_social_media)
        )
        menubar.add_cascade(label="Edit", menu=modeMenu)
        # Adding Help Menu
        help_ = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_)
        logger.info(get_version())
        help_.add_command(
            label="About", command=lambda: messagebox.showinfo("Versió", f"EditPasteApp v{get_version()}")
        )

        for i in range(int(HEIGHT / 2)):
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
