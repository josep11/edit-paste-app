import tkinter as tk
import pyperclip

from tkinter import *
from text_transformer import *

HEIGHT = 20
TITLE = "Paste Text From Chats to Strip The Sender"

# defaultTransformFunction = transform_text_pdf
defaultTransformFunction = transform_text_social_media

def changeDefaultFunction(fn):
    print(1)
    global defaultTransformFunction
    defaultTransformFunction = fn
    print(defaultTransformFunction)

def handle_clipboard(event):

    cb =pyperclip.paste() # root.clipboard_get()

    if not isinstance(cb, str):
        print("clipboard is not string")
        return "break"

    root.clipboard_clear()
    print(cb)
    cb_transformed = defaultTransformFunction(cb)

    pyperclip.copy(cb_transformed)
    # root.clipboard_append(cb_transformed)

    text.delete("0.0", tk.END)
    text.insert("0.0", cb_transformed)
    text.insert(tk.END, "\n\n\n\n\t\t\t\tCOPIED TO CLIPBOARD")

    return "break"



root = tk.Tk()
root.title(TITLE)
text = tk.Text(height=HEIGHT)
text.pack(side="top", fill="x")

menubar = Menu(root)
modeMenu = Menu(menubar, tearoff=0)
modeMenu.add_command(label="Transform PDF text", command=lambda: changeDefaultFunction(transform_text_pdf))
modeMenu.add_command(label="Transform Telegram/Whats text", command=lambda: changeDefaultFunction(transform_text_social_media))
menubar.add_cascade(label="Edit", menu=modeMenu)

for i in range(int(HEIGHT / 2)):
    text.insert("end", "\n")

text.insert("end", "\t\t\t\tPaste content to transform")

root.bind_all("<<Paste>>", handle_clipboard)

root.config(menu=menubar)

root.mainloop()
