listaLeida = input("Escriba la lista de numeros separados por coma: ")

listaNumeros = listaLeida.split(",")

print(listaLeida)
print(listaNumeros)

listaEnteros = []
for i in listaNumeros:
    listaEnteros.append(int(i))

print(listaEnteros)
