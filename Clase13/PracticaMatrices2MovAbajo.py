matriz = [[1,12,13,40],
          [50,66,72,80],
          [9,10,22,33],
          [4,5,6,7]]

columna = int(input("Digite la columna que quiere elegir(de 1 a 4): ")) - 1
#direccion = input("Digite la direccion que desea (arriba o abajo): ")

respaldo = None

for linea in range(0,len(matriz)-1):
    if respaldo == None:
        respaldo = matriz[linea][columna]
    matriz[linea][columna] = matriz[linea+1][columna]
matriz[len(matriz)-1][columna] = respaldo

print(matriz)

