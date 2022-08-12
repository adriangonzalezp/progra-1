def main():
    matrix = [[8,3,24],
          [12,13,-11],
          [14,12,-6]]
    printMatrix(matrix)
    line1 = readNumber()
    line2 = readNumber()
    matrix = switchLines(matrix,line1,line2)
    printMatrix(matrix)

def printMatrix(matrix):
    for line in matrix:
        print(line)
    print("\n")

def readNumber():
    isValid = True
    l = int(input("Digite el numero de una linea (1, 2, o 3): ")) -1
    if l == 0 or l == 1 or l == 2:
        return l
    else:
         print("Ese numero de linea no existe.")

def switchLines(matrix, line1,line2):
    temp = []
    temp.append(matrix[line1])
    matrix[line1] = matrix[line2]
    matrix[line2] = temp
    return matrix
    
main()