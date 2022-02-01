#!/bin/bash
# aqui hace falta comprobar si tenemos instalado el
# pyinstall y si no es el caso instalarlo y preguntarle
# al usuario si quiere instalarlo
# Tambien tiene que leer el primer parametro que se
# encarga de añadir el nombre a la aplicacion

# pyinstaller --noconfirm --clean --onefile --noconsole --name $1 main.py



echo APP VERSION $(cat edit_paste_app/__init__.py | grep version | awk '{split($0,a,"="); print a[2]}' | sed "s/'//g")
python -V
echo

# If using python 3.10.x use "--exclude-module _bootlocale"
PYTHON_VERSION=$(python -V)
if [[ "$PYTHON_VERSION" == *"3.10"* ]]; then
    excluded_modules+=" _bootlocale"
fi

pyinstaller --noconfirm --clean --onefile --noconsole \
    --osx-bundle-identifier=com.josepalsina.editpasteapp \
    --icon=paste.icns \
    --name EditPasteApp \
    --exclude-module $excluded_modules \
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