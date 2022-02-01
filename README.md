# EditPasteApp

This App is for stripping the user from Chats copied to the clipboard from Whatsapp/Telegram/Messenger. Usage: Run the App paste the conversation:

    user1: hello
    user1: how are you doing today?

Will be transformed and copied to the clipboard back again like so:

    hello
    how are you doing today?

## How to install

> Note, it is not working on Mac M1

1. Install the Python that it is working. If you are going to build it check the [How to Compile section](#how-to-compile) now.

2. cd to the project folder and make it the default local python version:

    ```shell
    pyenv local 3.9.0
    ```

3. `pip install -r requirements.txt`

## Hot to run tests

Will find all tests named test*.py inside tests director

    ```shell
    python -m unittest discover
    ```

## How to run

Linux:

    python entry.py

Windows:

    python ma

## How to compile

1. For compiling we need two things:
    - On MacOSX the python version needs to be installed as such:

        ```shell
        env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.9.0
        ```

    - `pip install pyinstaller`

2. Then simply run ./build.sh

3. If more files are added that need to be deployed they need to be specified inside build.sh

## Deployment

```./deploy.sh```

### Build and run the build version

```./build.sh && open dist/EditPasteApp.app```

### See Logs

```subl ~/Library/Logs/EditPasteApp/editpasteapp.log```
