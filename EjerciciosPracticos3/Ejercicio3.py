# Ingreso del dia del mes como entero.
n = int(input("Ingrese el numero del mes: "))

# Revisar que el numero ingresado sea del 1 al 12. 
if 1 <= n <= 12:
    # Si el mes es 1,3,4,5,7,8,10 o 12, imprime 31 dias.
    if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
        print("31 dias")
    # Si el mes es 4,6,9 o 11, imprime 30 dias.
    elif n == 4 or n == 6 or n == 9 or n == 11:
        print("30 dias")
    # En los demas casos (el mes es 2), imprime 28 dias.
    else:
        print("28 dias")
# Si el numero ingresado no es del 1 al 12 imprime un mensaje de error.
else:
    print(n, "no es el numero de un mes.")