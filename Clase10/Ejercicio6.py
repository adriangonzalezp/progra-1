lista = []

contador = 0

# leemos 10 numeros
while contador < 10:
    numero = int(input("Indique el numero que desea guardar: "))
    lista.append(numero)
    contador = contador + 1

numero = int(input("Cual numero desea revisar: "))

posicion = 0

for numeroEnLista in lista:
    if numeroEnLista == numero:
        print("El numero esta en la posicion", posicion)
        break
    posicion = posicion + 1