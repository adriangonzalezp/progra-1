conjunto = {[], [1,2,3]}

lista = [[], [1,2,3]]

lista.append([1,2,3,4])

# Vamos a ver el tamano del conjunto:
print(len(conjunto))

# Vamos a agregar un valor, no se pueden agregar listas:
conjunto.add(3)
print(len(conjunto))
print(conjunto)

# Vamos a agregar un valor repetido?
conjunto.add(3)
print(len(conjunto))
print(conjunto)