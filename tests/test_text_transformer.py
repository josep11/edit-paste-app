from edit_paste_app.text_transformer import *
import unittest

res = transform_text_pdf(
    "La estimulación de los receptores muscarínicos puede mediar")


class TestTransformText(unittest.TestCase):

    def test_transform_text_pdf(self):

        text = """La estimulación de los receptores muscarínicos puede mediar,
a través de mecanismos directos o indirectos, distintas acciones
despolarizantes o hiperpolarizantes de la neurona postsináptica.
Por ejemplo, los receptores del grupo M2 pueden alterar la permeabilidad"""

        textResult = """La estimulación de los receptores muscarínicos puede mediar, a través de mecanismos directos o indirectos, distintas acciones despolarizantes o hiperpolarizantes de la neurona postsináptica.
Por ejemplo, los receptores del grupo M2 pueden alterar la permeabilidad"""

        self.assertEqual(textResult, transform_text_pdf(
            text), "Should be text without unnecessary newlines")

    def test_transform_text_social_media(self):
        text = """Alberto Blanco, [02.06.21 17:28]
    [En resposta a Josep]
    Y como queda eso?

    Alberto Blanco, [02.06.21 17:28]
    Como justificó ese valor

    Alberto Blanco, [02.06.21 17:30]
    Queda solo 1 hora"""

        textResult = transform_text_social_media(text)

        # print(textResult)
        self.assertEqual(textResult.find("Josep"), -1)

        text = """(incluyendo un diagrama de cajas para las invocaciones):"""

        textResult = transform_text_social_media(text)

        self.assertEqual(textResult, text,
                         "should not strip this line but failed")

        # Telegram version 3.4.8
        text = """Fl Alex UMH, [1/2/22 11:16]
El 6 digo
Fl Alex UMH, [1/2/22 11:16]
Para aprobar"""
        textResult = transform_text_social_media(text)

        self.assertEqual(textResult.find("Alex UMH"), -1)


if __name__ == "__main__":
    unittest.main()

    print("Everything passed")
