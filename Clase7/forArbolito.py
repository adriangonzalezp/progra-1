# un programa que lee un numero e imprime 
# tantas lineas de asteriscos como el numero ingresado
# PERO imprime un asterisco mas en cada linea

numero = int(input("Introduzca el numero:"))

for linea in range(numero):
    contador = 0
    salida = ""
    while contador <= linea:
        salida = salida + "*"
        contador =  contador + 1
    print(salida)