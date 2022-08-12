a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el tercer numero: "))

if a > b:
    if a > c:
        print("El numero ", a, " es el mayor.")
    else:
        print("El numero ", c, " es el mayor.")
else:
    if b > c:
        print("El numero ", b, " es el mayor.")
    else:
        print("El numero ", c, " es el mayor.")
