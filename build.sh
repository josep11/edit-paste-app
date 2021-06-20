#!/bin/bash
# aqui hace falta comprobar si tenemos instalado el
# pyinstall y si no es el caso instalarlo y preguntarle
# al usuario si quiere instalarlo
# Tambien tiene que leer el primer parametro que se
# encarga de añadir el nombre a la aplicacion

# pyinstaller --noconfirm --clean --onefile --noconsole --name $1 main.py



echo APP VERSION $(cat edit-paste-app/__init__.py | grep version | awk '{split($0,a,"="); print a[2]}' | sed "s/'//g")
python -V
echo

pyinstaller --noconfirm --clean --onefile --noconsole \
    --osx-bundle-identifier=com.josepalsina.editpasteapp \
    --icon=paste.icns \
    --name EditPasteApp \
    entry.py

#    --add-binary edit_paste_app:edit_paste_app \

exit

echo build w debug options

pyinstaller --noconfirm --clean --onefile --noconsole \
    --osx-bundle-identifier=com.josepalsina.editpasteapp \
    --icon=paste.icns \
    --name EditPasteApp \
    --debug=imports \
    --log-level=DEBUG \
    entry.py