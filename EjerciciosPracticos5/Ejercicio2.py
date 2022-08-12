numero1 = int(input("Introduzca un numero: "))
numero2 = int(input("Introduzca otro numero: "))

mayor = 0
menor = 0
acumulador = 0

if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1

for i in range(menor, mayor+1):
    acumulador = acumulador + i

print("La suma de los numeros entre", menor, "y", mayor, "es", acumulador)

