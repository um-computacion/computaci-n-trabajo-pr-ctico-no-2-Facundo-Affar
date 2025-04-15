import unittest
from src.palindrome import is_palindrome

class TestPalindromosSimples(unittest.TestCase):
    def test_palindromos_en_minusculas(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("salas"))
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("radar"))

    def test_palindromos_con_mayusculas(self):
        self.assertTrue(is_palindrome("Rotor"))
        self.assertTrue(is_palindrome("Reconocer"))
        self.assertTrue(is_palindrome("Arenera"))
