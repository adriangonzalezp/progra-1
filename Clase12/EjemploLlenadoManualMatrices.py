# Programa que pida las lineas y columnas que tendra la matriz
# y llene dicha matriz numero por numero.
# Al final la imprime.

lineas = int(input("Cuantas lineas tendra la matriz?: "))
columnas = int(input("Cuantas columnas tendra la matriz?: "))

matriz = []

for lineaActual in range(0,lineas):
    matriz.append([]) #agregamos la nueva linea
    for columnaActual in range(0,columnas):
        nuevoNumero = int(input(f"cual numero ira en [{lineaActual},{columnaActual}]"))
        matriz[lineaActual].append(nuevoNumero) # en la ultima linea agregada
        # ponemos el numero recien leido.