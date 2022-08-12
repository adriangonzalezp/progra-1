#programa lee un numero N menor que 100
# e los N multiplos de 7 menores de 1000

cantidad = int(input("Cantidad de multiplos: "))

contador = 0
for numero in range(1000):
    if numero % 7 == 0 and contador < cantidad:
        print(numero)
        contador = contador + 1
    
 