# Ingreso de la medida de cada lado como floats.
a = float(input("Ingrese la medida del primer lado: "))
b = float(input("Ingrese la medida del segundo lado: "))
c = float(input("Ingrese la medida del tercer lado: "))

# Si todos los lados son iguales, imprime Equilatero.
if a == b == c:
    print("Euquilatero.")
# Si ningun lado es igual, imprime Escaleno.
elif a != b != c:
    print("Escaleno.")
# En los demas casos (dos lados son iguales), imprime Isosceles.
else:
    print("Isosceles.")