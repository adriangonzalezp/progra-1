# Leer los valores de los coeficientes.
a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))
c = int(input("Digite el valor de c: "))

# Verificar que 'a' no sea igual a 0.
if a != 0:
    # Calcular el valor del discriminante.
    discriminante = (b ** 2) - (4 * a * c)
    
    #Imprimir el resultado.
    print("El discriminante de la funcion "
       , a, "x^2 +", b, "x +", c, "= 0  es ", discriminante)

# Imprimir un mensaje de error en caso de que 'a' sea igual a 0.
else:
    print("El valor de 'a' no puede ser 0")


