import unittest

from translator import englishToFrench, frenchToEnglish

class TestEng2Fr(unittest.TestCase):
    def test1(self):
         self.assertEqual(englishToFrench('Hello'), 'Bonjour')
            #test case for the world Hello, shold translate to Bonjour

class TestFr2Eng(unittest.TestCase):
     def test1(self):
          self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
             #test case for the world Bonjour, shold translate to Hello

unittest.main()