from edit_paste_app.app_config import AppConfig
import unittest

class TestTransformText(unittest.TestCase):

    def test_AppConfig_constructor(self):
        app_config = AppConfig()

        assert app_config is not None
        assert app_config.APP_NAME is not None
        assert app_config.isDev is not None