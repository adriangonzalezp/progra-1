matriz = [[1,12,13,40],
          [50,66,72,80],
          [9,10,22,33],
          [4,5,6,7]]

columna = int(input("Digite la columna que quiere elegir(de 1 a 4): ")) - 1

print(matriz)
respaldo = matriz[len(matriz)-1][columna]
for linea in range(len(matriz),-1,0,-1):
    matriz[linea][columna] = matriz[linea][columna-1]
matriz[0][columna] = respaldo

print(matriz)
print(respaldo)
