# 4.	Haga un programa que toma una de esas matrices, lee un numero (1 2 3 o 4) y una direccion: arriba o abajo. 
# Luego el programa cambia de lugar los numeros en esa columna. 

# Por ejemplo, 1 - arriba haria que la matriz 1 quedara:
# 50 12  13  40
# 9  66  72  80
# 4  10  22  33
# 1  5   6   7


matriz = [[1,12,13,40],
          [50,66,72,80],
          [9,10,22,33],
          [4,5,6,7]]

columna = int(input("Digite la columna que quiere elegir(de 1 a 4): "))


direccion = input("Digite la direccion que desea (arriba o abajo): ")

auxiliar = None

for linea in range(0,len(matriz)):
    print(f"linea {linea}, columna {columna}: {matriz[linea][columna-1]}")
