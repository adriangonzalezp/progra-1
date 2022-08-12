numero = int(input("Escriba un numero"))

salida = ""

while numero > 0:
    if numero % 2 == 0: 
        salida = salida + "+" + str(numero)
    else:
        salida = salida + "-" + str(numero)
    numero = numero - 1

print(salida)