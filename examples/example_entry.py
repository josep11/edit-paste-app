# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from edit_paste_app.logger_wrapper import logger

# import time

root = tk.Tk()
ttk.Button(root, text="Print ok", command=lambda: print("ok")).pack()
logger.info("hola")
# root.mainloop()
logger.info("adeu")
