def eh_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    #invertido = texto_limpo[::-1]

    invertido = ''
    for letra in texto_limpo:
        invertido = letra + invertido

    if texto_limpo == invertido:
        return True
    else:
        return False
    
texto = input("Digite um texto: ")
resultado = eh_palindromo(texto)
print(f"{texto} é um palíndromo? {resultado}")