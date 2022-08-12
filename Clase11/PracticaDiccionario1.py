# Haga un programa que lea numeros de la consola hasta que el usuario ingrese el 0.
# Guarde los numeros en un diccionario, tal que si el numero es par, lo guarda en la lista de pares.
# Pero si es un impar lo guarda en la lista de impares. Ambas listas deben estar en un diccionario.

miDiccionario = {"pares": [], "impares": []}

opcion = int(input("Esctiba un numero entero diferente de cero: "))

while opcion != 0:
    if opcion % 2 == 0:
        miDiccionario["pares"].append(opcion)
    else:
        miDiccionario["impares"].append(opcion)
    opcion = int(input("Esctiba un numero entero diferente de cero: "))

print(miDiccionario)

