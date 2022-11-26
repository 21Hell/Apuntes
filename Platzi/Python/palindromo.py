def run():
    print('Bienvenido al programa para detectar palíndromos')
    palabra = input('Escribe una palabra: ')
    es_palindromo(palabra)
    if es_palindromo(palabra) == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

def es_palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

if __name__ == '__main__':
    run()