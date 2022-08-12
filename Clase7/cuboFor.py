#escriba un programa que lea un numero mayor que 1
#e imprime el cubo de todos los numeros entre 1 y el 
#numero leido
# usar el for
numero = int(input("Escriba un numero mayor que 1"))

for cubo in range(1,numero):
    print(cubo ** 3)