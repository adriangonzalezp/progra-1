#Escriba un programa en Python para calcular la suma
# de todos los elementos de cada tupla almacenada dentro de una lista de tuplas.
# Lista de tuplas:
#  [(11, 22, 66), (21, 13, -6), (31, 34), (21, 21, 21, 21)]
# Resultados esperado [99,28,65,84]

listaTuplas = [(11, 22, 66), (21, 13, -6), (31, 34), (21, 21, 21, 21)]

listaResultado = []

for tupla in listaTuplas:
    resultado = 0
    for numero in tupla:
        resultado = resultado + numero
    listaResultado.append(resultado)

print(listaResultado)