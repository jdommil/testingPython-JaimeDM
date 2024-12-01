# test_charfun.py

"""
test_charfun.py

Script de pruebas unitarias para la función esPalindromo.

Última Modificación: 29/11/2024
Autor: Jaime Domínguez Millón
Dependencias: unittest, charfun
"""

import unittest
from app.scripts.charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):
    """Clase de pruebas para la función esPalindromo."""

    def test_simple_palindrome(self):
        """Prueba con un palíndromo simple."""
        self.assertTrue(esPalindromo('Anita lava la tina'))

    def test_non_palindrome(self):
        """Prueba con una frase que no es palíndroma."""
        self.assertFalse(esPalindromo('Esto no es un palíndromo'))

    def test_palindrome_with_accents(self):
        """Prueba con palíndromo que contiene acentos."""
        self.assertTrue(esPalindromo('Dábale arroz a la zorra el abad'))

    def test_palindrome_with_uppercase(self):
        """Prueba con palíndromo que contiene mayúsculas."""
        self.assertTrue(esPalindromo('No traces en ese cartón'))

    def test_palindrome_with_punctuation(self):
        """Prueba con palíndromo que contiene puntuación."""
        self.assertTrue(esPalindromo('¿Acaso hubo búhos acá?'))

    def test_empty_string(self):
        """Prueba con cadena vacía."""
        self.assertTrue(esPalindromo(''))

    def test_single_character(self):
        """Prueba con un solo carácter."""
        self.assertTrue(esPalindromo('a'))

    def test_numeric_palindrome(self):
        """Prueba con palíndromo numérico."""
        self.assertTrue(esPalindromo('12321'))

    def test_numeric_non_palindrome(self):
        """Prueba con número que no es palíndromo."""
        self.assertFalse(esPalindromo('12345'))

    def test_palindrome_with_symbols(self):
        """Prueba con palíndromo que contiene símbolos."""
        self.assertTrue(esPalindromo('A man, a plan, a canal: Panama'))

if __name__ == '__main__':
    unittest.main()
