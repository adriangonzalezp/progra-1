#lea entero y lo comvierte a binario

numero = int(input("Digite el numero que quiere convertir a binario: "))
residuo = numero % 2
binario = ""

while numero > 1:
    binario = str(residuo) + binario
    numero = numero // 2
    residuo = numero % 2

binario = str(numero) + binario

print(binario)