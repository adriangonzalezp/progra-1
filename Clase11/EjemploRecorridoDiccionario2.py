miDiccionario = {1: (1,2,3,4), 2: (2,3,4,5)}

for llave in miDiccionario:
    print(llave)
    for elemento in miDiccionario[llave]:
        print("\t", elemento)

