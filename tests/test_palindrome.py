import unittest

from src_palindrome import is_palindrome

class TestPalindromos(unittest.TestCase):
    
    def test_palindromos_en_minusculas(self):

        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("salas"))
        self.assertTrue(is_palindrome("nivel"))
        self.assertTrue(is_palindrome("radar"))

if __name__ == '__main__':
    unittest.main()