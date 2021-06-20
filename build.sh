#!/bin/bash
# aqui hace falta comprobar si tenemos instalado el
# pyinstall y si no es el caso instalarlo y preguntarle
# al usuario si quiere instalarlo
# Tambien tiene que leer el primer parametro que se
# encarga de añadir el nombre a la aplicacion

# pyinstaller --noconfirm --clean --onefile --noconsole --name $1 main.py


echo APP VERSION $(cat edit-paste-app/__init__.py | grep version | awk '{split($0,a,"="); print a[2]}')
python -V
echo


pyinstaller --noconfirm --clean --onefile --noconsole \
    --osx-bundle-identifier=com.josepalsina.editpasteapp \
    --icon=paste.icns \
    --name EditPasteApp \
    tkinter_editpasteapp.py text_transformer.py


exit

echo build w debug options

pyinstaller --noconfirm --clean --onefile --noconsole \
    --osx-bundle-identifier=com.josepalsina.editpasteapp \
    --icon=paste.icns \
    --name EditPasteApp \
    --debug=imports \
    --log-level=DEBUG \
    tkinter_editpasteapp.py text_transformer.py