import unittest

from translator import englishToFrench, frenchToEnglish

class TestEng2Fr(unittest.TestCase):
    def test1(self):
         self.assertEqual(englishToFrench('Hello'), 'Bonjour')
            #test case for the world Hello, shold translate to Bonjour
         self.assertNotEqual(englishToFrench('Hello'), 'Hello')
            #test case for the world Hello, shold translate to Bonjour

class TestFr2Eng(unittest.TestCase):
     def test2(self):
          self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
             #test case for the world Bonjour, shold translate to Hello
          self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
            #test case for the world Hello, shold translate to Bonjour

unittest.main()