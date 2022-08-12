print("Turnos: Mañana (1)     Tarde (2)     Noche (3)")
turno = int(input("Ingrese el turno del trabajador:"))

print("Categorias: Asociate (1)     Senior (2)")
categoria = int(input("Ingrese la categoria del trabajador:"))

salario = int(input("Ingrese el salario del trabajador:"))

if turno == 1:
    print("El trabajdor califica para ser promovido.")
elif categoria == 1 or salario <= 350000:
    print("El trabajdor califica para ser promovido.")
else:
    print("El trabajdor no califica para ser promovido.")