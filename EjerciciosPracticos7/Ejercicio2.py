listTuples = [(11, 22, 66), (21, 13, -6), (31, 34), (21, 21, 21, 21)]
listResult = []

for tuple in listTuples:
    result = 0
    for numero in tuple:
        result = result + numero
    listResult.append(result)

print(listResult)