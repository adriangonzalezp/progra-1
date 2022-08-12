lista1 = input("Escriba la lista 1 de numeros separados por coma: ")
lista2 = input("Escriba la lista 2 de numeros separados por coma: ")

# convertimos la lista 1
listaNumeros1 = []
listaNumeros2 = []

# convertimos la lista 1
listaIntermedia = lista1.split(",")
for caracteresNumero in listaIntermedia:
    listaNumeros1 = int(caracteresNumero)

# convertimos la lista 2
listaIntermedia = lista2.split(",")
for caracteresNumero in listaIntermedia:
    listaNumeros2 = int(caracteresNumero)

