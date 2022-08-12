def main():
    mx = [[1,12,13,40],
          [50,66,72,80],
          [9,10,22,33],
          [4,5,6,7]]
    printMatrix(mx)
    splitMxs = splitMatrix(mx)
    printMatrix((splitMxs)[0])
    printMatrix((splitMxs)[1])

# Imprime una matriz dada.
def printMatrix(mx):
    for n in mx:
        print(n)
    print("\n")

# Recibe una matriz.
def splitMatrix(mx):
    splitMx1 = [[],[],[],[]]
    splitMx2 = [[],[],[],[]]

    # Guarda los valores superiores de la diagonal en una matriz.
    for line in range(0,len(mx)):
        for col in range(0,len(mx)):
            if line <= col:
                splitMx1[line].append(mx[line][col])
            else:
                splitMx1[line].append(0)

    # Guarda los valores inferiores de la diagonal en una matriz.
    for line in range(0,len(mx)):
        for col in range(0,len(mx)):
            if line > col:
                splitMx2[line].append(mx[line][col])
            else:
                splitMx2[line].append(0)
    # Retorna las dos matrices creadas.
    return(splitMx1,splitMx2)

main()
