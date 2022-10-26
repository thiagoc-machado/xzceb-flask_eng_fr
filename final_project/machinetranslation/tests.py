import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """ This class is for unit testing english_to_french """
    def tests_1(self):
        """ tests for english_to_french """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNotNone(english_to_french(" "), "Value can not be None")

class TestFrenchToEnglish(unittest.TestCase):
    """ This class is for unit testing french_to_english """
    def tests_1(self):
        """ tests for french_to_english """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNotNone(french_to_english(" "), "Value can not be None")

unittest.main()