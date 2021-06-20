#text_editor.py
import re

def transform_text_social_media(text):
    # Text received:
    #   [0:16, 10/2/2021] Joana: Hola, com va això?
    # Text returned:
    #   Hola, com va això?
    regex = r"\[.*\].*:\s"  # whatsapp: remove sender and date
    text = re.sub(regex, "", text, 0, re.MULTILINE)

    regex2 = r"\n\n"  # telegram: rm 1 line (useful for Telegram version < 2.5.9)
    text = re.sub(regex2, "\n", text, 0, re.MULTILINE)

    regex3 = r".*\[(\d+([.]|:|-| )){4}\d{2}](\n|\s)" # telegram: (useful for Telegram version = 2.5.9) MATCHES: "<name of contact>, [18.02.21 22:47]\n"
    text = re.sub(regex3, "", text, 0, re.MULTILINE)

    regex4_telegram_forward = r"\[.*(resposta|respuesta|response).(a|to).*\]\n" # telegram: MATCHES: "[En resposta a <name>]\n" or similars
    text = re.sub(regex4_telegram_forward, "", text, 0, re.MULTILINE)

    regexFbMessenger = r".* sent.*\d{2}:\d{2}\n"
    text = re.sub(regexFbMessenger, "", text, 0, re.MULTILINE)
    return text

# removes unnecessary newlines from pdf
def transform_text_pdf(text):
    # print(text)
    # print('\n')
    regex = r"(?<!\.)\n" # remove newline if is not preceded by a dot
    text = re.sub(regex, " ", text, 0, re.MULTILINE)

    # print(text)

    return text
