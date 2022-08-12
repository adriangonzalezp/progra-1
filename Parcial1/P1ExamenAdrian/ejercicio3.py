#-----------------------------------------#
# Ejercicio 3
# Explicar donde esta el error en este codigo
#-----------------------------------------#

# Problema

numero = int(input("inserte numero "))
if numero == 1:
    print("Llegue aqui")

# Parece que al no especificar que tipo de dato se va a recolectar de la terminal para la variable "numero",
# se guarda como texto en vez de como un numero entero o decimal con el que se puede hacer aritmetica y operaciones condicionales.
# Si se le agrega el codigo que guarda el input como int o float, ya logra comparar un numero con un numero en vez de un numero
# con texto en el if.