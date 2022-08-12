# Ingreso de los resultados de los dados como enteros.
a = int(input("Ingrese el resultado del primer dado: "))
b = int(input("Ingrese el resultado del segundo dado: "))
c = int(input("Ingrese el resultado del tercer dado: "))

# Revisar que los numeros ingresados sean del 1 al 6.
if 1 <= a <= 6 and 1 <= b <= 6 and 1 <= c <= 6:
    # Si todos los lados son 6. Imprime excelente.
    if a == 6 and b == 6 and c == 6:
        print("Excelente.")
    # Si dos lados son 6 (la suma de ambos da 12), imprime muy bueno.
    elif (a + b == 12) or (a + c == 12) or (b + c == 12):
        print("Muy bueno.")
    # Si uno es 6, imprime regular.
    elif a == 6 or b == 6 or c == 6:
        print("Regular")
    # Si ninguno es 6, imprime pesimo,
    else:
        print("Pesimo.")
# Si los numeros ingresados no son del 1 al 6 imprime un mensaje de error.
else:
    print("Los numeros ingresados no son del 1 al 6")