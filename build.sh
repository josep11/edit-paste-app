#!/bin/bash
# aqui hace falta comprobar si tenemos instalado el
# pyinstall y si no es el caso instalarlo y preguntarle
# al usuario si quiere instalarlo
# Tambien tiene que leer el primer parametro que se
# encarga de añadir el nombre a la aplicacion

# pyinstaller --noconfirm --clean --onefile --noconsole --name $1 main.py

pyinstaller --noconfirm --clean --onefile --noconsole --name EditPasteApp tkinter-editpasteapp.py text_transformer.py