numero = str(input("Ingrese un numero mayor a 99999: "))
impares = 0

for x in numero:
    digito = int(x)
    if digito % 2 != 0:
        impares = impares + 1

print(numero, "tiene", impares, "digitos impares.")
