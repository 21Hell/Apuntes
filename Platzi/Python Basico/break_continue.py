def run():
    while True:
        numero = int(input('Escribe un número: '))
        if numero < 0:
            break
    print(f'El cuadrado de {numero} es {numero**2}')

    

if __name__ == '__main__':
    run()