"""
charfun.py

Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.

Última Modificación: 21/11/2024
Autor: Jaime Domín Domínguez Millón
Dependencias: unicodedata
"""

import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    """
    # Convertir a minúsculas
    cadena = cadena.lower()
    # Eliminar acentos y diacríticos
    cadena = ''.join(
        char for char in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(char) != 'Mn'
    )
    # Eliminar caracteres no alfanuméricos
    cadena_limpia = ''.join(char for char in cadena if char.isalnum())
    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

if __name__ == '__main__':
    while True:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
        if frase.lower() == "salir":
            print("Programa finalizado.")
            break
        else:
            # Comprobar si es palíndromo
            if esPalindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")
