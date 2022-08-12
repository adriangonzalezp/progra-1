def main():
    mx = [[1,12,13,40],
          [50,66,72,80],
          [9,10,22,33],
          [4,5,6,7]]
    printMatrix(mx)
    rotMx = rotateMatrix(mx)
    printMatrix(rotMx)

def printMatrix(mx):
    for line in mx:
        print(line)
    print("\n")

def rotateMatrix(mx):
    rotMx = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    for col in range(0,len(mx)):

        for line in range(0,len(mx)):
            rotMx[line][col] = mx[line][col]
            
    return rotMx

main()