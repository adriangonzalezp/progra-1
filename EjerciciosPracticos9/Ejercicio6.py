def main():
    mx = [[10,11,14,16],[20,18,16,14],[18,20,23,24],[12,10,8,6]]
    printMatrix(mx)
    mx = rotateMatrix(mx)
    printMatrix(mx)

def printMatrix(mx):
    for line in mx:
        print(line)
    print("\n")

def rotateMatrix(mx):
    tempMx = []
    col = len(mx) -1

    for col in range(len(mx)-1,-1,-1):
        temp = []
        for line in range(len(mx)):
            temp.append(mx[line][col])
        tempMx.append(temp)

    for x in range(len(mx)):
        for y in range(len(mx)):
            mx[x][y] = tempMx[x][y]
    return mx

main()