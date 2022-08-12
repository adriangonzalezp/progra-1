def main():
    mx1 = [[1,12,13,40],[50,66,72,80],[9,10,22,33],[4,5,6,7]]
    mx2 = [[10,11,14,16],[20,18,16,14],[18,20,23,24],[12,10,8,6]]
    resMx = chooseLargerNumber(mx1, mx2)
    print(resMx)

# Recibe dos matrices. 
def chooseLargerNumber(mx1, mx2):
    resMx = [[],[],[],[]]
    larger = None
    # Llena una matriz resultado de los elementos mayores de cada matriz.
    for line in range(0,len(mx1)):
        for col in range(0,len(mx2)):
            n1 = mx1[line][col]
            n2 = mx2[line][col]
            if n1 > n2:
                larger = n1
            else:
                larger = n2
            resMx[line].append(larger)
    # Retorna la matriz resultado.
    return resMx
            
main()