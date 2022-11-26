def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")



def menu():
    print("Bienvenido al conversor de monedas")
    print("1. Pesos colombianos")
    print("2. Pesos argentinos")
    print("3. Pesos mexicanos")
    opcion = input("Elige una opción: ")
    opcion = int(opcion)

    if opcion == 1:
        conversor("colombianos", 3875)
    elif opcion == 2:
        conversor("argentinos", 65)
    elif opcion == 3:
        conversor("mexicanos", 24)
    else:
        print("Ingresa una opción correcta")




menu()