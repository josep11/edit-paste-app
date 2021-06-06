import tkinter as tk

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

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        logging.info("hi there")

initLogger()
root = tk.Tk()
app = Application(master=root)
app.mainloop()