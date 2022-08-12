# Escriba un programa que lea varios numeros de
# usuario. Los numeros vienen separados por coma y los mete en un set.
# Luego el programa saca del set los valores mas grandes y mas peque;os.

input = input("Digite los numeros separados por una coma: ")

conjunto = set(map(int,input.split(",")))

# Esta funcion map() es equivalente a recorrer todos los elementos del resultado de input.split()
# Entonces al recorrerlos a cada uno le aplica la funcion int
# map() ademas de aplicar la funcion me retorna todos los resultados y los guarda en el conjunto definido por la funcion "set".

menor = None
mayor = None

for elemento in conjunto:
    if menor == None:
        menor = elemento
    if mayor == None:
        mayor = elemento
    if menor != None and elemento < menor:
        menor = elemento
    if mayor != None and elemento > mayor:
        mayor = elemento
print("El valor maximo del conjunto es:", mayor)
print("El valor minimo del conjunto es:", menor)

# Investigar min() and max()
print("El valor maximo del conjunto es:", max(conjunto))
print("El valor minimo del conjunto es:", min(conjunto))