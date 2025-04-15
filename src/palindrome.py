import re
import unicodedata

def is_palindrome(text):
    # Normalizar texto (eliminar tildes, pasar a minúsculas)
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text.lower())
        if unicodedata.category(c) != 'Mn'
    )
    text = re.sub(r'[^a-z0-9]', '', text)
    
    return text == text[::-1]


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
