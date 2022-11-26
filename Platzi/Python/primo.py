def run():
    numero = int(input('Escribe un número: '))
    print(es_primo(numero))

def es_primo(numero):
    rangoImpar = range(3, numero, 2)
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in rangoImpar:
            if numero % i == 0:
                return False
        return True

    

if __name__ == '__main__':
    run()