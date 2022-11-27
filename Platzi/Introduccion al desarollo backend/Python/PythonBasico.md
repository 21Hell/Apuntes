# Objetos = DataTypes

Numéricos
    Int
    Float
    Complex
    Bool
String
List
Tuple
Dictionary


# Parsear
```python
numero = input("escribe un numero:")
str(numero)
int(numero)
```
# Operadores Logicos
```python
and
or
not
```

# Operadores de comparacion

```python
== # igual
!= # diferente
< # menor que
> # mayor que
<= # menor o igual que
>= # mayor o igual que
```

# Condicionales
```python
if condicion:
    codigo
elif condicion:
    codigo
else:
    codigo
```
## Uso de pass
// Si no se quiere que se ejecute nada en el if, se usa pass
// similar al switch

```python
if condicion:
    pass
else:
    codigo
```


# Funciones

Para no repetir codigo, se pueden crear funciones
```python
def nombre_funcion(parametros):
    codigo 
    return valor
```
Ej suma
```python
def suma(a,b):
    resultado = a + b
    return resultado
```
Ej suma con parametros por defecto
```python
def suma(a=0,b=0):
    return a+b
```

# Strings

##Metodos
```python
nombre = "Juan"
# Mayusculas
nombre.upper() # JUAN

# Minusculas
nombre.lower() # juan

# Capitalizar
nombre.capitalize() 
# Reemplazar
nombre.replace("a","e") # Juen

# Contar
nombre.count("a") # 1

# Longitud
len(nombre) # 4

# Indice
nombre[0] # J

# Indice inverso
nombre[-1] # n

# Slice
nombre[0:2] # Ju

# Slice inverso
nombre[-2:] # an

```

## Slices mas complejos
```python

nombre = "123456789"

nombre[::2] # 13579

# Slice con saltos
nombre[0:7:3] # 147

# Slice con saltos inversos
nombre[9:0:-2] # 8642

# Slice con saltos inversos y sin limite
nombre[::-1] # 987654321

```

# Bucles
## While
```python
while condicion:
    codigo
```
### Ejemplo
```python
contador = 0
while contador < 10:
    print(contador) # 0 1 2 3 4 5 6 7 8 9
    contador += 1
```

## For
```python
for elemento in iterable:
    codigo
```
### Ejemplo
```python
for i in range(10):
    print(i) # 0 1 2 3 4 5 6 7 8 9
```
### Stings
```python
for letra in "Hola":
    print(letra) # H o l a
```
### Listas
```python
for elemento in [1,2,3,4,5]:
    print(elemento) # 1 2 3 4 5
```

# Break y Continue
```python
for i in range(10):
    if i == 5:
        break
    print(i) # 0 1 2 3 4
```
```python
for i in range(10):
    if i == 5:
        print("Se encontro un 5")
        continue
    print(i) # 0 1 2 3 4 Se encontro un 6 7 8 9
```

# Listas
```python
lista = [1,2,3,4,5]
lista[0] # 1
lista[-1] # 5
lista[0:3] # [1,2,3]

# Agregar elementos
lista.append(6) # [1,2,3,4,5,6]

# Eliminar elementos
lista.pop() # [1,2,3,4,5]
lista.pop(0) # [2,3,4,5]

# Eliminar elementos por valor
lista.remove(3) # [1,2,4,5]

# Ordenar
lista.sort() # [1,2,4,5]

# Invertir
lista.reverse() # [5,4,2,1]

# Longitud
len(lista) # 4

# Iterar
for elemento in lista:
    print(elemento) # 1 2 3 4 5

# Iterar con indice
for i in range(len(lista)):
    print(lista[i]) # 1 2 3 4 5

# Buscar indice
lista.index(3) # 2

# Contar elementos
lista.count(3) # 1

# Copiar
lista2 = lista.copy() # [1,2,3,4,5]

# Unir listas
lista3 = lista + lista2 # [1,2,3,4,5,1,2,3,4,5]

# Unir listas
lista.extend(lista2) # [1,2,3,4,5,1,2,3,4,5]

# Limpiar lista
lista.clear() # []

# Eliminar lista
del lista # []

# Listas anidadas
lista = [1,2,3,4,5]
lista_anidada = [lista,lista,lista]
lista_anidada[0][0] # 1
print(lista_anidada) # [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

# Lista * 2
lista = [1,2,3,4,5]
lista * 2 # [1,2,3,4,5,1,2,3,4,5]
```

# Tuplas
```python
tupla = (1,2,3,4,5)
tupla[0] # 1
tupla[-1] # 5
tupla[0:3] # (1,2,3)
# No se pueden modificar

# Desempaquetado de tuplas

tupla = (1,2,3,4,5)
a,b,c,d,e = tupla
print(a,b,c,d,e) # 1 2 3 4 5

# Iterar tuplas
for elemento in tupla:
    print(elemento) # 1 2 3 4 5

toupla.append(6) # Error
toupa.pop() # Error
#No se pueden modificar

```
# Diccionarios
```python
diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 28
}
print(diccionario) # {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 28}
print(diccionario["nombre"]) # Juan
print(diccionario["apellido"]) # Perez
print(diccionario["edad"]) # 28
