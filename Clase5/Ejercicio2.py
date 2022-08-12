nota = float(input("Ingrese la nota"))

if nota >= 70:
    print("Aprobo el curso")
elif 70 > nota >= 60:
    print("A convocatoria")
else:
    print("Reprobo")