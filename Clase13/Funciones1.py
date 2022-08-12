#solucion sin funciones
from cmath import sqrt

coeficienteA = int(input("Escriba el coeficiente A: "))
coeficienteB = int(input("Escriba el coeficiente B: "))
coeficienteC = int(input("Escriba el coeficiente C: "))

discriminante = (coeficienteB * coeficienteB) - \
                  (4 * coeficienteA * coeficienteC)
print(discriminante)
if discriminante < 0:
    print("No hay soluciones")
elif discriminante == 0:
    print("Hay una solucion")
    solucion = (-1 * coeficienteB)/ (2 * coeficienteA)
    print(f"La solucion unica es: {solucion}")
else: 
    print("Hay 2 soluciones")
    solucion1 = ((-1 * coeficienteB) + (sqrt(discriminante))) \
                    / (2*coeficienteA)
    solucion2 = ((-1 * coeficienteB) - (sqrt(discriminante))) \
                    / (2*coeficienteA)
    print(f"las soluciones son {solucion1}, {solucion2}")