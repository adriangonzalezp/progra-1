lista = []

contador = 0

# leemos 10 numeros
while contador < 10:
    numero = int(input("Indique el numero que desea guardar: "))
    lista.append(numero)
    contador = contador + 1
numero = int(input("Cual numero desea revisar: "))

# vamos a usar la funcion index
posicion = lista.index(numero)

print("El numero", numero, "esta en la posicion", posicion)
