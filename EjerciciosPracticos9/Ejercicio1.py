def main():
    matrix1 = [[1,12,13,40],[50,66,72,80],[9,10,22,33],[4,5,6,7]]
    matrix2 = [[10,11,14,16],[20,18,16,14],[18,20,23,24],[12,10,8,6]]
    resMatrix = addMatrixes(matrix1,matrix2)
    print(resMatrix)

# Recibe dos matrices.
def addMatrixes(matrix1,matrix2):
    resMatrix = [[],[],[],[]]
    # Suma las matrices.
    for line in range(0,len(matrix1)):
        for column in range(0,len(matrix2)):
            resMatrix[line].append(matrix1[line][column] + matrix2[line][column])
    # Retorna una matriz resultado.        
    return(resMatrix)

main()