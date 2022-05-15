import os

isDev = os.getenv("ENV") == "dev"

if isDev:
    from dotenv import load_dotenv

    load_dotenv()


class AppConfig:
    # db_tracking_charset = os.getenv("DB_TRACKING_CHARSET")

    isDev = isDev
