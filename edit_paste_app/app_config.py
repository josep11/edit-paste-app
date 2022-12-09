import os
from edit_paste_app.text_transformer import transform_text_social_media

isDev = os.getenv("ENV") == "dev"

if isDev:
    from dotenv import load_dotenv

    load_dotenv()


class AppConfig:
    # db_tracking_charset = os.getenv("DB_TRACKING_CHARSET")
    APP_NAME = "EditPasteApp"

    isDev = isDev

    default_transform_function = transform_text_social_media  # transform_text_pdf
