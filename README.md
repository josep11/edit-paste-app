# EditPasteApp

This App is for stripping the user from Chats copied to the clipboard from Whatsapp/Telegram/Messenger. Usage: Run the App paste the conversation:

    user1: hello
    user1: how are you doing today?

Will be transformed and copied to the clipboard back again like so:

    hello
    how are you doing today?

## How to install

1. Install the Python that it is working. WARNING: If you are going to build it check the [How to Compile section](#how-to-compile) now.

2. cd to the project folder and make it the default local python version:

    ```shell
    pyenv local 3.10.1
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

### Build and run the built version

Make sure that the .env file includes all variables like in `.env.example`.
Make sure that the shebang on all the `./*.sh` is the same as your default shell. To get it: `echo $SHELL`. Then

```bash
./build.sh && source .env && open dist/$APP_NAME.app
```

## Deployment

Warning: before deploying make sure that you delete the previous build file from /Applications as I found there may be traces that will cause conflicts with newer builds.

```bash
./build.sh && ./deploy.sh && source .env && terminal-notifier -message "deployed" -title "$APP_NAME"       
```

### See Logs

See them:
```subl ~/Library/Logs/EditPasteApp/editpasteapp.log```

Tail them:

```bash
tail -f ~/Library/Logs/EditPasteApp/editpasteapp.log
```

## Issues template

```txt
Python version: 
Mac OS version:
pyinstaller version to compile: 
problems experienced: 
logs: 
```

## Future lines

[Nice tutorial to build executables with pyinstaller](https://www.youtube.com/watch?v=3xuN9JQ7j1Q&ab_channel=CodingEntrepreneurs)

## Development

Upgrade dependencies. Run `make pip/check` (you will need to have installed `pip install pip-check` before).
