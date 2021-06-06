import tkinter as tk
# import clipboard
from clipboard_manager import *

from text_transformer import *
import logging
import os

home = os.path.expanduser("~")

def initLogger():

    # TODO: make this file a class and create a global variable for the log path or another best practice

    # https://docs.python.org/3/howto/logging.html
    logFileDir = home+'/Library/Logs/EditPasteApp/' # create logs directory if not exists
    logFile = logFileDir + 'editpasteapp.log'
    try:
        os.makedirs(logFileDir)
    except FileExistsError as e:
        pass
    logging.basicConfig(filename=logFile,
                        encoding='utf-8',
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s'
                        )


def log(stri):
    # logging.warning("I'm a warning!")
    logging.info(stri)
    # logging.debug("I'm a debug message!")


initLogger()

root = tk.Tk()
text = tk.Text(height=6)
text.pack(side="top", fill="x")



for i in range(10):
    text.insert("end", "this is line #%d\n" % i)

entrys = []
for i in range(10):
    entry = tk.Entry(root)
    entry.pack(side="top", fill="x")
    entrys.append(entry)

def handle_clipboard(event):
    text.delete('1.0', tk.END)

    for entry in entrys:
        entry.delete(0, "end")
        entry.insert(0, "")

    lines = getClipboardData()

    log('getting cb data')

    lines = lines.decode()
    log(lines)

    lines = transform_text_social_media(lines)

    log('after transform cb data')
    log(lines)

     # lines = root.clipboard_get().split("\n")
    for entry, line in zip(entrys, lines):
        entry.insert(0, line)
     # convert str to bytes
    # type(bytes(lines, 'utf-8'))
    linesBytes = bytes(lines, 'utf-8')


    log(f'setting cb data {linesBytes}')
    setClipboardData(linesBytes )

    return "break"


root.bind_all("<<Paste>>", handle_clipboard)

root.mainloop()