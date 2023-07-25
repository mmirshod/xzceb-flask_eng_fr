import unittest
from ..translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):

    # Test cases for englishToFrench method
    def test_english_to_french_hello(self):
        # Test translation of the word 'Hello' to French
        english_text = "Hello"
        expected_result = "Bonjour"
        result = english_to_french(english_text)
        self.assertEqual(result, expected_result)

    def test_english_to_french_bonjour(self):
        # Test translation of the word 'Bonjour' to French
        english_text = "Bonjour"
        expected_result = "Bonjour"  # The translation should remain the same
        result = english_to_french(english_text)
        self.assertEqual(result, expected_result)

    # Test cases for frenchToEnglish method
    def test_french_to_english_bonjour(self):
        # Test translation of the word 'Bonjour' to English
        french_text = "Bonjour"
        expected_result = "Hello"
        result = french_to_english(french_text)
        self.assertEqual(result, expected_result)

    def test_french_to_english_hello(self):
        # Test translation of the word 'Hello' to English
        french_text = "temps"  # 'Hello' is the same in English
        expected_result = "time"
        result = french_to_english(french_text)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
