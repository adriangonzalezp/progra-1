# Un programa que lea una serie de datos, los guarda en una tupla, y luego mete la tupla en una lista.

print("Bienvenido al almacen de datos.")

opcion = input("Presione S para salir, o cualquier tecla para comenzar.")
listaPersonas = []
while opcion != "S":
    cedula = int(input("Numero de cedula: "))
    nombre = input("Nombre de la persona:")
    fechaNacimiento = input("Fecha de nacimiento(yyyy-MM-dd): ")
    miTupla = (cedula, nombre, fechaNacimiento)
    listaPersonas.append(miTupla)
    opcion = input("Presione S para salir, o cualquier tecla para comenzar.")

print("Personas ingresadas: ")
print(listaPersonas)
