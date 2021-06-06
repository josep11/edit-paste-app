#!/bin/bash
# aqui hace falta comprobar si tenemos instalado el
# pyinstall y si no es el caso instalarlo y preguntarle
# al usuario si quiere instalarlo
# Tambien tiene que leer el primer parametro que se
# encarga de añadir el nombre a la aplicacion

# pyinstaller --noconfirm --clean --onefile --noconsole --name $1 main.py

python -V
echo

pyinstaller --noconfirm --clean --onefile --noconsole \
    --osx-bundle-identifier=com.josepalsina.editpasteapp \
    --icon=paste.icns \
    --name EditPasteApp \
    tkinter-editpasteapp.py text_transformer.py