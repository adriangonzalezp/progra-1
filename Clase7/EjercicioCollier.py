# Escribe un programa que lea un numero. Van a calcular su serie de collier.
# Mientras el resultado sea diferente de 1:
# Si el numero es par, lo dividen entre 2, si el numero es impar, lo multiplican por 3 y le suman 1.
# Imprime el resultado parcial y el numero de de paso cada vez.

resultado = int(input("Digite un numero: "))
paso = 0
while resultado != 1:
    if resultado % 2 == 0:
        resultado = resultado / 2    
    else:
        resultado = (resultado * 3) + 1

    paso = paso + 1
    print("Paso", paso, ":", resultado)
