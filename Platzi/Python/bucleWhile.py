def forImplementation():
    LIMITE = 1000000
    for contador in range(0, LIMITE):
        potencia_2 = 2**contador
        if potencia_2 > LIMITE:
            break
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))


def mientras():
    LIMITE = 1000000
    contador = 0
    potencia_2 = 1;
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador

def menu():
    print("Seleccione una opción de ejecución")
    print("1. For")
    print("2. Mientras")
    opcion = input("Elige una opción: ")
    opcion = int(opcion)
    if opcion == 1:
        forImplementation()
    elif opcion == 2:
        mientras()

if __name__ == '__main__':
    menu()
