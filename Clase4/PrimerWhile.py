numero = int(input("Escriba un numero par: "))

while numero % 2 == 0:
    print("El numero ", numero, " es par")
    numero = int(input("Escriba el OTRO numero par: "))

print("El numero", numero, "NO ES PAR")