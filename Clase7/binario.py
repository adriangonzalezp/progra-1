numero = int(input("Digite un numero: "))
binario = ""

residuo = numero % 2

while numero != 1:
    binario = str(residuo) + binario
    numero = numero // 2
    residuo = numero % 2

binario = str(numero) + binario

print(binario)
