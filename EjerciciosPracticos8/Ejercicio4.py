from operator import index


matrix = []
numColRow = int(input("Cuantas lineas y columnas desea que tenga la matriz de identidad?: "))

for row in range(0,numColRow):
    matrix.append([])
    for column in range(0,numColRow):
        if column == row:
            matrix.append(1)
        else:
            matrix.append(0)
        
print(matrix)