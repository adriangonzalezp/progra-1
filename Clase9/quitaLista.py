nombre = ""
lista = []

while nombre != "STOP":
    nombre = input("Escriba un nombre, o STOP para salir: ")
    if nombre != "STOP": 
        lista.append(nombre)

print(lista)
lista.reverse()
print(lista)