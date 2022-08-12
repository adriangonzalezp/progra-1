temperatura = float(input("Ingrese la temperatura en grados."))

if temperatura < 10:
    print("Hace mucho frio.")
elif 10 <= temperatura <= 15:
    print("Hce poco frio.")
elif 15 < temperatura <= 24:
    print("Hace una temperatura normal.")
elif 24 < temperatura <= 30:
    print("Hace poco calor.")
else:
    print("Hace mucho calor")