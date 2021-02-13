import tkinter as tk
import re

HEIGHT = 20
TITLE = "Paste Text From Chats to Remove The Sender"

root = tk.Tk()
root.title(TITLE)
text = tk.Text(height=HEIGHT)
text.pack(side="top", fill="x")

for i in range(int(HEIGHT / 2)):
    text.insert("end", "\n")

text.insert("end", "\t\t\t\tPaste content to transform")


def transform_text(text):
    # Text received:
    #   [0:16, 10/2/2021] Joana: Hola, com va això?
    # Text returned:
    #   Hola, com va això?
    regex = r".*\:\s"  # whatsapp: remove sender and date
    text = re.sub(regex, "", text, 0, re.MULTILINE)
    regex2 = r"\n\n"  # telegram: rm 1 line
    text = re.sub(regex2, "\n", text, 0, re.MULTILINE)
    regexFbMessenger = r".* sent.*\d{2}:\d{2}\n" 
    text = re.sub(regexFbMessenger, "", text, 0, re.MULTILINE)
    return text


def handle_clipboard(event):
    cb = root.clipboard_get()
    if not isinstance(cb, str):
        print("clipboard is not string")
        return "break"

    root.clipboard_clear()
    cb_transformed = transform_text(cb)
    root.clipboard_append(cb_transformed)

    text.delete("0.0", tk.END)
    text.insert("0.0", cb_transformed)
    text.insert(tk.END, "\n\n\n\n\t\t\t\tCOPIED TO CLIPBOARD")

    return "break"


root.bind_all("<<Paste>>", handle_clipboard)

root.mainloop()
