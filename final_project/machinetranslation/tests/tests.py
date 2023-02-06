import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('How are you?'), 'Au revoir?')
    
    def test_french_to_english(self):
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Good night.'), 'Oui.')
        
if __name__ == "__main__":
    unittest.main()
