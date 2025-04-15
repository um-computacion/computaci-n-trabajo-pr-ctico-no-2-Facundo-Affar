def is_palindrome(text):
    text = text.replace(" ", "").lower()  
    return text == text[::-1]  

if __name__ == '__main__':
    entrada = input("Ingrese una palabra o frase: ")
    if is_palindrome(entrada):
        print(f'"{entrada}" es un palíndromo')
    else:
        print(f'"{entrada}" no es un palíndromo')
