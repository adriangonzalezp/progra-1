numero = int(input("Hasta cual numero quiere sumar?"))

contador = 1
suma = 0
while(contador <= numero):
    suma = suma + contador
    contador = contador + 1

print("La suma total es: ", suma)