import unittest

from translator import english_2_french, french_2_english

class TestEng2Fr(unittest.TestCase):
    def test1(self):
         self.assertEqual(english_2_french('Hello'), 'Bonjour')
            #test case for the world Hello, shold translate to Bonjour

class TestFr2Eng(unittest.TestCase):
     def test1(self):
          self.assertEqual(french_2_english('Bonjour'), 'Hello')
             #test case for the world Bonjour, shold translate to Hello

unittest.main()