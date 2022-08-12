listTuples = [(11, 12), (56, 32), (78, 44)]
listLists = []

listProv = []
for tuple in listTuples:
    listProv = [tuple[0],tuple[1]]
    listLists.append(listProv)

print(listLists)