#-----------------------------------------#
# Ejercicio 2
# Sumar los los numeros pares del 1 al 5
#-----------------------------------------#

# Problema

sumatoria = 0

for x in range(0,5):
    if(x % 2 == 0):
        sumatoria = sumatoria + x
print(sumatoria)
