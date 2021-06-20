from text_transformer import *

def test_transform_text_pdf():

    text = """La estimulación de los receptores muscarínicos puede mediar,
a través de mecanismos directos o indirectos, distintas acciones
despolarizantes o hiperpolarizantes de la neurona postsináptica.
Por ejemplo, los receptores del grupo M2 pueden alterar la permeabilidad"""


    textResult = """La estimulación de los receptores muscarínicos puede mediar, a través de mecanismos directos o indirectos, distintas acciones despolarizantes o hiperpolarizantes de la neurona postsináptica.
Por ejemplo, los receptores del grupo M2 pueden alterar la permeabilidad"""

    # print (transform_text_pdf(text))

    print('\n\n')

    # print (textResult)

    print('\n\n')

    assert transform_text_pdf(text) == textResult, "Should be text without unnecessary newlines"


def test_transform_text_social_media():
    text = """Alberto Blanco, [02.06.21 17:28]
[En resposta a Josep]
Y como queda eso?

Alberto Blanco, [02.06.21 17:28]
Como justificó ese valor

Alberto Blanco, [02.06.21 17:30]
Queda solo 1 hora"""

    textResult = transform_text_social_media(text)

    # print(textResult)

    assert textResult.find("Josep") == -1

    text = """(incluyendo un diagrama de cajas para las invocaciones):"""

    textResult = transform_text_social_media(text)

    assert textResult == text, "should not strip this line but failed"


if __name__ == "__main__":
    test_transform_text_social_media()

    test_transform_text_pdf()

    print("Everything passed")