def main():
    mx = [[1,12,13,40],[50,66,72,80],[9,10,22,33],[4,5,6,7]]
    printMatrix(mx)
    col = readColumn()
    dir = readDirection()
    resMx = rotateMxColumn(mx,col,dir)
    printMatrix(resMx)

# Imprime una matriz dada.
def printMatrix(mx):
    for line in mx:
        print(line)
# Lee el numero de la columna.
def readColumn():
    n = int(input("Ingrese el numero de columna que quiere rotar (1,2,3 o 4): ")) - 1
    return n

# Lee la direccion de rotacion.
def readDirection():
    d = input("Ingrese en que direccion la desea rotar (arriba o abajo): ")
    return d

# Recibe una matriz, numero de columna y direccion de rotacion.
def rotateMxColumn(mx,col,dir):
    # Pasa los parametros a las funciones de rotacion dependiendo de la direccion.
    if dir == "arriba":
        resMx = rotateUp(mx,col)
    elif dir == "abajo":
        resMx = rotateDown(mx,col)
    # Retorna una matriz con una columna rotada.
    return resMx

# Recibe una matriz y columna.
def rotateUp(mx,col):
    temp = None
    # Rota la columna dada hacia arriba.
    for line in range(0,len(mx)-1):
        if temp == None:
            temp = mx[line][col]
        mx[line][col] = mx[line + 1][col]
    mx[len(mx)-1][col] = temp
    # Retorna la matriz alterada.
    return mx

def rotateDown(mx,col):
    temp = mx[len(mx)-1][col]
    # Rota la columna dada hacia arriba.
    for line in range(len(mx)-1,0,-1):
        mx[line][col] = mx[line - 1][col]
    mx[0][col] = temp
    # Retorna la matriz alterada.
    return mx

main()