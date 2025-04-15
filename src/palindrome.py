import re

def is_palindrome(texto):  # definimos is_palindrome 
    texto_limpio = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ]', '', texto).lower()
    return texto_limpio == texto_limpio[::-1]


if __name__ == '__main__':
    try:
        while True:
            entrada = input("Ingrese una palabra o frase: ")
            if is_palindrome(entrada):
                print(f'"{entrada}" es un palíndromo\n')
            else:
                print(f'"{entrada}" no es un palíndromo\n')
    except KeyboardInterrupt:
        print("\nPrograma terminado.")
