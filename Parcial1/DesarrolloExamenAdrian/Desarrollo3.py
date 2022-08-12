numero1 = int(input("Ingrese un numero:"))

if numero1 > 0:
    numero2 = int(input("Ingrese otro numero: "))

    while numero2 != numero1:

        if numero2 < numero1:
            print(numero2)
        elif numero2 > numero1:
            print("Es mayor.")
       
        numero2 = int(input("Ingrese otro numero: "))
    
    
    
