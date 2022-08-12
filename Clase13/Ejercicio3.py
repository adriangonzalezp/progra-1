matriz1 = [[1,12,13,40],
           [50,66,72,80],
           [9,10,22,33],
           [4,5,6,7]]

matriz2 = [[10,11,14,16],
           [20,18,16,14],
           [18,20,23,24],
           [12,10,8,6]]  

matrizResultado = []

mayor = None
for linea in range(0,len(matriz1)):
    matrizResultado.append([])
    for columna in range(0,len(matriz1[linea])):
        if matriz1[linea][columna] > matriz2[linea][columna]:
            mayor = matriz1[linea][columna]
        else:
            mayor = matriz2[linea][columna]
        matrizResultado[linea].append(mayor)

print(matrizResultado)

