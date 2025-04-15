import re

def is_palindrome(texto):#definimos is_palindrome 
    texto_limpio = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ]', '', texto).lower()
    return False