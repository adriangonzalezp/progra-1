hipotenusa = float(input("Digite la hipotenusa: "))
cateto1 = float(input("Digite el primer cateto: "))
cateto2 = float(input("Digite el segundo cateto: "))

cuadradoH = hipotenusa ** 2
cuadradosC = ((cateto1) ** 2) + ((cateto2) ** 2)

if cuadradoH == cuadradosC:
    print("El triangulo es una terna pitagorica.")
else:
    print("El triangulo no es una terna pitagorica.")