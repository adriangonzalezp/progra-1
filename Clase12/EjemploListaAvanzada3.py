# Un programa que dadas 2 matrices
matriz1 = [[1,2],
           [3,4]]
matriz2 = [[6,7],
           [8,9]]

# Un programa que sume las matrices y haga una nueva matriz.
# Resultado esperado seria [[7,9][11,13]].

matrizResultado = [[],[]]
for linea in range(0,len(matriz1)):
    for columna in range(0,len(matriz1)):
        matrizResultado[linea].append(matriz1[linea][columna]+ matriz2[linea][columna])
                
print(matrizResultado)                
