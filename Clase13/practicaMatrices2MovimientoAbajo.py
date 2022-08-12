matriz1 = [[1, 12, 13, 40], [50, 66, 72, 80], 
           [9, 10, 22, 33], [4, 5, 6, 7]]

#vamos a hacer primero un programa que imprime solo una columna

columna = int(input("Cual columna desea mover? (1-4)")) - 1

print(matriz1)
respaldo = matriz1[len(matriz1)-1][columna]
for linea in range(len(matriz1)-1, 0, -1):
    matriz1[linea][columna] = matriz1[linea-1][columna]
matriz1[0][columna] = respaldo

print(matriz1)
print(respaldo)