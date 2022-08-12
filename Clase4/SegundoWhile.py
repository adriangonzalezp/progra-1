# hacer un programa que lea un numero entero e imprima
# todos los multiplos de 3 menores que el numero leido.

numeroEntero = int(input("Escriba un numero Entero Positivo: "))
contador = 0

while contador < numeroEntero:
    if contador % 3 == 0:
        print("El numero", contador, "es multiplo de 3")
    contador = contador + 1

