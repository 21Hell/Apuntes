
def conversor(entrada,cuanto,salida):
    cuanto = float(cuanto)
    moneda = asignarMoneda(entrada)
    cambio = asignarMoneda(salida)
    if moneda == "COP":
        if cambio == "COP":
            return cuanto
        elif cambio == "ARS":
            return cuanto * 0.03
        elif cambio == "MXN":
            return cuanto * 0.004
        elif cambio == "USD":
            return cuanto * 0.0003
    elif moneda == "ARS":
        if cambio == "COP":
            return cuanto * 29.5
        elif cambio == "ARS":
            return cuanto
        elif cambio == "MXN":
            return cuanto * 0.11
        elif cambio == "USD":
            return cuanto * 0.0060
    elif moneda == "MXN":
        if cambio == "COP":
            return cuanto * 251.59
        elif cambio == "ARS":
            return cuanto * 8.54
        elif cambio == "MXN":
            return cuanto
        elif cambio == "USD":
            return cuanto * 0.051
    elif moneda == "USD":
        if cambio == "COP":
            return cuanto * 4865
        elif cambio == "ARS":
            return cuanto * 165.30
        elif cambio == "MXN":
            return cuanto * 19.34
        elif cambio == "USD":
            return cuanto
    else:
        return "Moneda no disponible"


def asignarMoneda(moneda):
    if moneda == 1:
        return "COP"
    elif moneda == 2:
        return "ARS"
    elif moneda == 3:
        return "MXN"
    elif moneda == 4:
        return "USD"
    else:
        return "Moneda no disponible"


def menu():
    print("Bienvenido al conversor de monedas")
    print("1. COP")
    print("2. ARS")
    print("3. MXN")
    print("4. USD")
    entrada = int(input("Ingrese la moneda de entrada: "))
    cuanto = input("Ingrese la cantidad de moneda: ")
    salida = int(input("Ingrese la moneda de salida: "))
    print("El resultado es: " + str(conversor(entrada,cuanto,salida)) + " " + asignarMoneda(salida))

menu()