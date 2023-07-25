"""
Translator to translate from english to french and vice versal
"""


from deep_translator import MyMemoryTranslator


def english_to_french(english_text: str) -> str:
    """
    Translate English to French
    @param english_text: desired english text to translate
    @type english_text: str
    @return: str
    """

    translator = MyMemoryTranslator(source="en-GB", target="fr-FR")
    return translator.translate(text=english_text)


def french_to_english(french_text) -> str:
    """
    Translate French to English
    @param french_text: desired french text to translate
    @type french_text: str
    @return: str
    """

    translator = MyMemoryTranslator(source="fr-FR", target="en-GB")
    return translator.translate(text=french_text)
