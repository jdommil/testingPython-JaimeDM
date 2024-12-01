from app.scripts.charfun import esPalindromo

def main():
    #Aquí va el código del main
   while True:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")

        if frase.lower() == "salir":
            print("Programa finalizado.")
            break
        else:
            # Comprobar si es palíndromo
            if esPalindromo(frase):
                print("La frase es un palíndromo.")
            else:
                print("La frase no es un palíndromo.")