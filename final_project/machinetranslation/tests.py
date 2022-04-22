import unittest

from translator import englishToFrench, frenchToEnglish

class TestEng2Fr(unittest.TestCase):
    def test1(self):
         self.assertEqual(englishToFrench('Hello'), 'Bonjour')
            #test case for the word "Hello", shold translate to Bonjour
         self.assertNotEqual(englishToFrench('Hello'), 'Hello')
            #test case for the word "Hello", function should not return Hello

class TestFr2Eng(unittest.TestCase):
     def test2(self):
          self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
             #test case for the word "Bonjour", shold translate to Hello
          self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
            #test case for the word "Bonjour", function shold not return Bonjour

unittest.main()