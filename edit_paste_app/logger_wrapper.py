import logging
import os
from edit_paste_app.app_config import AppConfig

home = os.path.expanduser("~")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DEBUG_FILENAME = "debug.log"

# TODO: make this file a class and create a global variable for the log path or another best practice
# https://docs.python.org/3/howto/logging.html
logFileDir = home + "/Library/Logs/EditPasteApp/"  # create logs directory if not exists
logFile = logFileDir + "editpasteapp.log"
try:
    os.makedirs(logFileDir)
except FileExistsError as e:
    pass

if AppConfig.isDev:
    logging.basicConfig(filename=DEBUG_FILENAME, encoding="utf-8", level=logging.DEBUG)
else:
    logging.basicConfig(
        filename=logFile, encoding="utf-8", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
logger.info("1st")
