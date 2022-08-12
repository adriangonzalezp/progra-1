palabraLeida = ""
lista = []

#aqui leemos palabra por palabra hasta que el usuario escribe STOP
while palabraLeida != "STOP":
    palabraLeida = input("Escriba una palabra, o STOP para salir: ")
    if palabraLeida != "STOP": 
        lista.append(palabraLeida)

#imprimir todas las palabras de la lista
for unaPalabra in lista:
    print(unaPalabra)

#imprimir usando la funcion upper
for unaPalabra in lista:
    print(unaPalabra.upper())
