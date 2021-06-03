# EditPasteApp

This App is for stripping the user from Chats copied to the clipboard from Whatsapp/Telegram/Messenger. Usage: Run the App paste the conversation:

    user1: hello
    user1: how are you doing today?

Will be transformed and copied to the clipboard back again like so:

    hello
    how are you doing today?

## How to install

1. Install the Python that it is working:

2. cd to the project folder and make it the default local python version:
    ```bash
    pyenv local 3.9.0
    ```
## Hot to run tests

python test_text_transformer.py

## How to run

Linux:

    python3 tkinter-editpasteapp.py

Windows:

    python ma

## How to compile

1. For compiling we need two things:
    - On MacOSX the python version needs to be installed as such:
    
    ```bash
    env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.9.0
    ```

    - pip install pyinstaller

2. Then simply run ./build.sh

3. If more files are added that need to be deployed they need to be specified inside build.sh

## Deploy to Applications

```bash
cp -r dist/EditPasteApp.app /Applications/
```